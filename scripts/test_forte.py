"""Check the first forte arrival against its score and actual MIDI attack."""
from pathlib import Path
import json, xml.etree.ElementTree as ET
import mido
root=Path(__file__).resolve().parents[1]
p=next(p for p in json.loads((root/'data/catalog.json').read_text()) if p['op']==310)
folder=root/'pieces'/p['folder'];stem=p['stem']
event=next(e for e in p['events'] if e['hand']=='rh' and e['offset']==96)
assert event['notated_dynamic']=='f' and event['velocity']==78
score=ET.parse(folder/(stem+'.musicxml'))
assert score.find('.//measure[@number="25"]/direction/direction-type/dynamics/f') is not None
midi=mido.MidiFile(folder/(stem+'.mid'));attacks={}
for track in midi.tracks:
 tick=0
 for message in track:
  tick+=message.time
  if message.type=='note_on' and message.velocity and message.channel==0 and tick==96*midi.ticks_per_beat:attacks[message.note]=message.velocity
assert attacks=={65:74,69:74,74:78},attacks
print('Op. 310 forte verified: printed f, MIDI top voice 78, supporting chord tones 74.')
