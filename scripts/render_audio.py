from pathlib import Path
import json, math, subprocess, wave, argparse, os
import mido
from bisect import bisect_right
from meter_plan import bar_plan
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work'
cat=json.loads((ROOT/'data/catalog.json').read_text())
style=json.loads((ROOT/'data/library_style.json').read_text())
reverb=style['reverb']
WORK.mkdir(exist_ok=True)
TPB=960
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
for p in cat:
    if args.opus is not None and p['op'] not in args.opus:continue
    d=OUT/p['folder'];stem=p['stem']
    metres,bar_lengths,bar_starts,beats=bar_plan(p);bpb=bar_lengths[0]
    performance=p.get('performance',{})
    mid=mido.MidiFile(type=1,ticks_per_beat=TPB)
    conductor=mido.MidiTrack();mid.tracks.append(conductor)
    conductor.append(mido.MetaMessage('track_name',name=f'CWS Op. {p["op"]}: {p["title"]}',time=0))
    numerator,denominator=map(int,p['meter'].split('/'))
    conductor.append(mido.MetaMessage('time_signature',numerator=numerator,denominator=denominator,time=0))
    midi_key=p['key'][0].upper()+p['key'][1:]+('m' if p['key'][0].islower() else '')
    conductor.append(mido.MetaMessage('key_signature',key=midi_key,time=0))
    # Every bar has a tempo event so the exact demo timeline is recoverable.
    bar_bpms=[]
    for mi in range(1,p['bars']+1):
        if performance:
            assert len(performance['rubato'])==p['bars']
            bpm=performance['rubato'][mi-1]
            if mi==p['bars']:bpm*=.8
            bar_bpms.append(bpm)
            continue
        bpm=p['bpm']
        # Small phrase-end relaxation, with no random timing or hidden repeated sections.
        if mi%4==0 and mi<p['bars']-1:bpm*=.96
        if str(mi) in p['tempo_changes']:bpm=p['tempo_changes'][str(mi)]
        if mi==p['bars']:bpm*=.75 # the notated final fermata
        bar_bpms.append(bpm)
    tempo_map=[]
    positions=sorted(set(np.arange(0,beats,.5))|set(bar_starts)) if performance else bar_starts
    conductor_events=[]
    for i,signature in enumerate(metres[1:],1):
        if signature!=metres[i-1]:
            numerator,denominator=map(int,signature.split('/'))
            conductor_events.append((round(bar_starts[i]*TPB),0,mido.MetaMessage('time_signature',numerator=numerator,denominator=denominator)))
    for beat in positions:
        bpm=float(np.interp(beat,bar_starts,bar_bpms)) if performance else bar_bpms[bisect_right(bar_starts,beat)-1]
        microseconds=mido.bpm2tempo(bpm);tick=round(float(beat)*TPB)
        conductor_events.append((tick,1,mido.MetaMessage('set_tempo',tempo=microseconds)))
        tempo_map.append(dict(beat=float(beat),microseconds=microseconds))
    last_tick=0
    for tick,_,message in sorted(conductor_events,key=lambda event:(event[0],event[1])):
        message.time=tick-last_tick;conductor.append(message);last_tick=tick
    conductor.append(mido.MetaMessage('end_of_track',time=round(beats*TPB)-last_tick))
    def seconds_at(beat):
        total=0
        for i,mark in enumerate(tempo_map):
            stop=tempo_map[i+1]['beat'] if i+1<len(tempo_map) else beats
            portion=max(0,min(beat,stop)-mark['beat'])
            total+=portion*mark['microseconds']/1_000_000
        return total
    velocities={'pp':43,'p':54,'mp':62,'mf':70}
    sections={int(k):v for k,v in p['sections'].items()}
    for hi,hand in enumerate(['rh','lh']):
        hand_sections={int(k):v for k,v in p['lower_sections'].items()} if hand=='lh' and p.get('lower_sections') else sections
        tr=mido.MidiTrack();mid.tracks.append(tr)
        tr.append(mido.MetaMessage('track_name',name='Right hand' if hi==0 else 'Left hand',time=0))
        tr.append(mido.Message('program_change',program=0,channel=hi,time=0))
        tr.append(mido.Message('control_change',control=7,value=100,channel=hi,time=0))
        tr.append(mido.Message('control_change',control=10,value=65 if hi==0 else 61,channel=hi,time=0))
        scheduled=[]
        prev=None
        for ev in [e for e in p['events'] if e['hand']==hand]:
            dyn=hand_sections[max(k for k in hand_sections if k<=ev['bar'])]
            base=velocities[dyn]
            # Lower part is a singing line. It comes forward at thematic entries.
            voice_adjust=-8 if hi==1 else 0
            if ev.get('voice')=='inner':
                voice_adjust=-7
                if performance and any(start<=ev['offset']<end for start,end in performance.get('inner_entries',[])):voice_adjust=-1
            if performance and hi==1 and any(start<=ev['offset']<end for start,end in performance['lower_entries']):voice_adjust=-2
            if hi==1 and ((p['op'] in [2,6] and ev['bar']<=4) or (p['op']==3 and 13<=ev['bar']<=14) or (p['op']==4 and 9<=ev['bar']<=10) or (p['op']==5 and 13<=ev['bar']<=14)):voice_adjust=-2
            if ev.get('voice')=='tenor':
                voice_adjust=-6
                if performance and any(start<=ev['offset']<end for start,end in performance.get('tenor_entries',[])):voice_adjust=-1
            phrase_pos=((ev['bar']-1)%4*bpb+(ev['offset']%bpb))/(4*bpb)
            swell=round(2*math.sin(phrase_pos*math.pi))
            if performance:
                swell=sum(round(amount*math.sin(math.pi*(ev['offset']-start)/(end-start))) for start,end,amount in performance['phrase_arcs'] if start<=ev['offset']<=end)
            for kind,startbar,endbar in p['hairpins']:
                startbeat=bar_starts[startbar-1];endbeat=bar_starts[endbar-1]
                if startbeat<=ev['offset']<=endbeat:
                    position=(ev['offset']-startbeat)/(endbeat-startbeat)
                    if kind=='crescendo':swell+=round(7*position)
                    else:
                        paired=any(k=='crescendo' and en==startbar for k,st,en in p['hairpins'])
                        swell+=round(7*(1-position) if paired else -7*position)
            offbeat=(-1 if ev['offset']%1 else 0) if performance else (-2 if ev['offset']%1 else 0)
            vel=int(max(25,min(82,base+voice_adjust+swell+offbeat)))
            start=round(ev['offset']*TPB)
            gate=.97 if hi==0 else .94
            if performance:gate=performance.get('gate',.99)
            if ev['bar']==p['bars']:gate=1
            end=round((ev['offset']+ev['duration']*gate)*TPB)
            for pitch in ev['pitches']:
                pitch_velocity=vel-(4 if performance and len(ev['pitches'])>1 and pitch<max(ev['pitches']) else 0)
                scheduled.append((start,1,mido.Message('note_on',channel=hi,note=pitch,velocity=pitch_velocity)))
                scheduled.append((end,0,mido.Message('note_off',channel=hi,note=pitch,velocity=0)))
            # Ratios such as sevenths do not divide the MIDI tick grid exactly.
            # Follow the actual scheduled attack and the quantised score release.
            ev['seconds']=round(seconds_at(start/TPB),6)
            ev['end_seconds']=round(seconds_at(round((ev['offset']+ev['duration'])*TPB)/TPB),6)
            ev['velocity']=vel
            if p.get('lower_sections'):ev['notated_dynamic']=dyn
        # Explicit spans match the printed pedal marks. Earlier works retain
        # their existing per-bar rendering unchanged.
        pedal_spans=p.get('pedal_spans')
        if pedal_spans is None:
            pedal_spans=[(bar_starts[mi-1]+.1,bar_starts[mi-1]+bar_lengths[mi-1]-performance.get('pedal_lift',.04))
                         for mi in range(1,p['bars']+1)
                         if ((mi in performance.get('pedal_bars',[])) if performance else (mi%4==0 or mi==p['bars']))]
        for startbeat,endbeat in pedal_spans:
            scheduled.append((round(startbeat*TPB),2,mido.Message('control_change',control=64,value=80,channel=hi)))
            scheduled.append((round(endbeat*TPB),-1,mido.Message('control_change',control=64,value=0,channel=hi)))
        scheduled.sort(key=lambda x:(x[0],x[1]))
        last=0
        for tick,_,message in scheduled:
            message.time=tick-last;tr.append(message);last=tick
        tr.append(mido.Message('control_change',control=64,value=0,channel=hi,time=max(0,round(beats*TPB)-last)))
        tr.append(mido.MetaMessage('end_of_track',time=TPB*3))
    mid.save(d/(stem+'.mid'))
    # Raw render stays in work/. The MP3 is the user-facing listening copy.
    raw=WORK/(stem+'_raw.wav');mp3=d/(stem+'.mp3')
    soundfont=os.environ.get('CWS_SOUNDFONT',str(WORK/'audio-assets/GeneralUser-GS.sf2'))
    subprocess.run(['fluidsynth','-ni','-g','0.8','-r','44100','-o','synth.reverb.active=1','-o',f'synth.reverb.room-size={reverb["room_size"]}','-o',f'synth.reverb.damp={reverb["damp"]}','-o',f'synth.reverb.level={reverb["level"]}','-o','synth.chorus.active=0','-F',str(raw),soundfont,str(d/(stem+'.mid'))],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    with wave.open(str(raw),'rb') as f:
        sr=f.getframerate();sig=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).reshape(-1,f.getnchannels()).astype(float)/32768
    peak=float(np.max(np.abs(sig)))
    assert peak<.999,('raw clipping',p['title'],peak)
    # One gain setting preserves the composed dynamics; gentle EQ softens the sample's edge.
    gain_db=min(12,20*math.log10(.86/max(peak,1e-5)))
    duration=seconds_at(beats)+2.8
    fade=max(0,duration-2.3)
    filters=f'volume={gain_db:.3f}dB,lowpass=f=8500,afade=t=out:st={fade:.3f}:d=2.3'
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(raw),'-af',filters,'-t',f'{duration:.4f}','-codec:a','libmp3lame','-q:a','2','-metadata',f'title={p["title"]}','-metadata',f'artist=CWS Library | Studies with Maple','-metadata',f'album=CWS First Studies','-metadata',f'track={p["op"]}',str(mp3)],check=True)
    p['duration_seconds']=round(duration,2);p['performance_seconds']=round(seconds_at(beats),2)
    p['bar_tempos']=bar_bpms
    if performance:p['tempo_map']=tempo_map
    p['audio_reverb']=dict(reverb)
    (d/(stem+'.json')).write_text(json.dumps(p,indent=2)+'\n')
    print(stem,'audio',p['duration_seconds'],'seconds; peak',round(peak,3),'gain',round(gain_db,2))
(ROOT/'data/catalog.json').write_text(json.dumps(cat,indent=2)+'\n')
