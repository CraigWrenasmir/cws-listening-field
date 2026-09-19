"""Engraving defaults for individually authored Further Weather studies."""

def make_study(*,op,title,key,fifths,meter,bpm,parent,source,motif,rh,lh,description,technical,tempos,phrases,sections,pedal=None,**extras):
    """Shared engraving defaults only; pitches, rhythms and forms are explicit."""
    n=len(rh.strip().splitlines());beats=int(meter.split('/')[0])*4/int(meter.split('/')[1])
    assert len(lh.strip().splitlines())==n and len(tempos)==n
    p=dict(op=op,title=title,key=key,fifths=fifths,meter=meter,bpm=bpm,parent_opus=parent,ancestry=source,motif=motif,rh=rh,lh=lh,
      description=description,difficulty='Advanced expressive study',technical_note=technical,
      technique_limits=dict(chord_span=12,melodic_leap=16,rapid_leap=9),
      system_starts=list(range(1,n+1,2)),page_starts=list(range(9,n+1,8)),
      engraving=dict(spacing_system=19,spacing_staff=19,pedal_offset_y=610),
      sections=sections,lower_sections={1:'p'},words={1:'cantabile'},slurs=phrases,lower_phrases=[],hairpins=[],tempo_changes={},group=3,final_fermata=False,
      performance=dict(rubato=tempos,phrase_arcs=[[(a-1)*beats,b*beats,3] for a,b in phrases],lower_entries=[],pedal_lift=.2,gate=.97,note='Authored phrase breathing and melodic voicing; independent rhythm is written in the score, with a shared tempo map.'),pedal_spans=sorted(pedal or []))
    p.update(extras)
    if p.get('meters'):
        lengths=[int(m.split('/')[0])*4/int(m.split('/')[1]) for m in p['meters']];assert len(lengths)==n
        offsets=[sum(lengths[:i]) for i in range(n+1)]
        p['performance']['phrase_arcs']=[[offsets[a-1],offsets[b],3] for a,b in phrases]
    return p

