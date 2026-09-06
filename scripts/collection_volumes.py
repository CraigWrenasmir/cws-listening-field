"""Bounded score/recording volumes with stable links and a plain download index."""
from pathlib import Path
from html import escape
import json, zipfile
from pypdf import PdfReader, PdfWriter

VOLUME_SIZE=24
MAX_FILE_BYTES=90*1024*1024

def build_volumes(root, catalog, selected=None):
    downloads=root/'downloads';downloads.mkdir(exist_ok=True)
    manifest_path=downloads/'volumes.json'
    old={v['number']:v for v in json.loads(manifest_path.read_text())} if manifest_path.exists() else {}
    groups={}
    for p in catalog:groups.setdefault((p['op']-1)//VOLUME_SIZE+1,[]).append(p)
    volumes=[]
    for number,pieces in sorted(groups.items()):
        ops=[p['op'] for p in pieces]
        # Keep the original public URLs as the first volume grows and then closes.
        pdf_name='CWS_First_Studies_Scores.pdf' if number==1 else f'CWS_Volume_{number:02d}_Scores.pdf'
        zip_name='CWS_First_Studies.zip' if number==1 else f'CWS_Volume_{number:02d}.zip'
        pdf_path=downloads/pdf_name;zip_path=downloads/zip_name
        unchanged=(selected is not None and not set(ops).intersection(selected)
                   and old.get(number,{}).get('ops')==ops and pdf_path.exists() and zip_path.exists())
        if not unchanged:
            writer=PdfWriter();source_pages=[]
            for p in pieces:
                source=root/'pieces'/p['folder']/(p['stem']+'.pdf')
                writer.append(str(source),outline_item=f'CWS Op. {p["op"]} - {p["title"]}')
                source_pages.extend(PdfReader(source).pages)
            writer.add_metadata({'/Title':f'CWS First Studies - Volume {number} - Op. {ops[0]}–{ops[-1]}','/Author':'CWS Library - studies with Maple (AI)'})
            with pdf_path.open('wb') as f:writer.write(f)
            combined=PdfReader(pdf_path)
            assert len(combined.pages)==len(source_pages)
            # Appending must preserve every already-inspected page and its order.
            for actual,source in zip(combined.pages,source_pages):
                assert actual.get_contents().get_data()==source.get_contents().get_data(),('Changed score page',number)
            with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
                for p in pieces:
                    for path in sorted((root/'pieces'/p['folder']).glob('*')):
                        if path.is_file():archive.write(path,str(path.relative_to(root)))
                for name in ['data/STYLE.md','data/EXPERIMENTAL_ARC.md','licenses/Leipzig-OFL.txt','licenses/GeneralUser-GS.txt']:
                    archive.write(root/name,name)
                archive.write(pdf_path,pdf_name)
                listing='\n'.join(f'CWS Op. {p["op"]} — {p["title"]}' for p in pieces)
                archive.writestr('VOLUME.txt',f'CWS / FIRST STUDIES\nVolume {number:02d}\nOp. {ops[0]}–{ops[-1]}\n\n{listing}\n\nScores, recordings, MIDI, MusicXML and source metadata.\n')
            with zipfile.ZipFile(zip_path) as archive:assert archive.testzip() is None
        pages=sum(p['pages'] for p in pieces)
        volume=dict(number=number,first=ops[0],last=ops[-1],ops=ops,count=len(ops),pages=pages,
                    first_title=pieces[0]['title'],last_title=pieces[-1]['title'],
                    complete=len(ops)==VOLUME_SIZE,seconds=round(sum(p['duration_seconds'] for p in pieces),2),
                    pdf='downloads/'+pdf_name,zip='downloads/'+zip_name,
                    pdf_bytes=pdf_path.stat().st_size,zip_bytes=zip_path.stat().st_size)
        assert max(volume['pdf_bytes'],volume['zip_bytes'])<MAX_FILE_BYTES,('Reduce volume size before publishing',number)
        volumes.append(volume)
    assert [op for v in volumes for op in v['ops']]==[p['op'] for p in catalog]
    manifest_path.write_text(json.dumps(volumes,indent=2)+'\n')
    def mb(size):return f'{size/1024/1024:.1f} MB'
    rows=[]
    for v in volumes:
        status='' if v['complete'] else ' · growing volume'
        opus=str(v['first']) if v['first']==v['last'] else f'{v["first"]}–{v["last"]}'
        count=f'{v["count"]} work'+('' if v['count']==1 else 's')
        journey=escape(v['first_title']) if v['count']==1 else f'{escape(v["first_title"])} → {escape(v["last_title"])}'
        rows.append(f'''<section class="volume" aria-labelledby="volume-{v['number']}">
<span class="volume-number" aria-hidden="true">{v['number']:02d}</span><div>
<h2 id="volume-{v['number']}">Volume {v['number']:02d}</h2>
<p class="volume-range">CWS Op. {opus} · {count}{status}</p>
<p class="volume-journey">{journey}</p>
<div class="volume-links"><a href="{Path(v['pdf']).name}" download>Scores <span>PDF · {v['pages']} pages · {mb(v['pdf_bytes'])}</span></a>
<a href="{Path(v['zip']).name}" download>Complete volume <span>ZIP · {mb(v['zip_bytes'])}</span></a></div>
</div></section>''')
    page=f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark"><title>Collected volumes · CWS First Studies</title>
<link rel="stylesheet" href="../src/downloads.css"></head><body><main>
<header><span>CWS / FIRST STUDIES</span><a href="../index.html">Return to the field</a></header>
<h1>Collected volumes</h1><p class="introduction">Take the music with you. Each volume brings together up to 24 works, with printable scores, piano recordings, MIDI and MusicXML.</p>
<div class="volumes">{''.join(rows)}</div>
<footer>{len(catalog)} works · Individual scores and recordings are also available in <a href="../index.html">The Listening Field</a>.</footer>
</main></body></html>'''
    (downloads/'index.html').write_text(page)
    return volumes
