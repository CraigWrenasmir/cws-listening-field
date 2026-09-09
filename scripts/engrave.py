from series_rules import series_for
from pathlib import Path
import json, io, argparse, xml.etree.ElementTree as ET
import verovio, cairosvg
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work';QA=WORK/'qa';QA.mkdir(exist_ok=True,parents=True)
cat=json.loads((ROOT/'data/catalog.json').read_text())
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
for p in cat:
    if args.opus is not None and p['op'] not in args.opus:continue
    d=OUT/p['folder'];stem=p['stem']
    tk=verovio.toolkit()
    engraving=p.get('engraving',{})
    tk.setOptions(dict(pageWidth=2100,pageHeight=3100,adjustPageHeight=True,pageMarginTop=15,pageMarginBottom=70,pageMarginLeft=120,pageMarginRight=90,
                       scale=40,breaks='encoded',header='none',footer='none',font='Leipzig',
                       spacingSystem=engraving.get('spacing_system',9),spacingStaff=engraving.get('spacing_staff',10),systemMaxPerPage=6,svgViewBox=True,
                       mnumInterval=0,justifyVertically=False,minLastJustification=0))
    if not tk.loadFile(str(d/(stem+'.musicxml'))): raise RuntimeError('Load failed')
    print(stem,tk.getPageCount(),'pages')
    writer=PdfWriter()
    for i in range(1,tk.getPageCount()+1):
        svg=tk.renderToSVG(i)
        # Flatten the nested SVG viewport for Cairo's vector PDF conversion.
        ns='{http://www.w3.org/2000/svg}'
        root=ET.fromstring(svg)
        inner=root.find(ns+'svg')
        root.set('viewBox',inner.get('viewBox'))
        root.set('preserveAspectRatio','xMidYMin')
        root.set('color','black');root.set('font-family','Times, serif')
        for child in list(inner):root.append(child)
        root.remove(inner)
        # Some long bass slurs need extra clearance above the pedal brackets.
        pedal_shift=engraving.get('pedal_offset_y',0)
        if pedal_shift:
            for group in root.findall('.//'+ns+'g[@class="pedal"]'):
                if len(group):group.set('transform',f'translate(0,{pedal_shift})')
        # Cairo does not use embedded webfonts: make the metronome glyph a path.
        for tg in root.findall('.//'+ns+'g[@class="tempo"]'):
            txt=tg.find(ns+'text')
            x,y=txt.get('x'),txt.get('y')
            for child in list(tg):tg.remove(child)
            mg=ET.SubElement(tg,ns+'g',transform=f'translate({x},{y})')
            glyph=ET.parse(Path(verovio.__file__).parent/'data/Leipzig/ECA5.xml').getroot()
            glyph.tag=ns+'g';glyph.set('transform','scale(0.72)')
            for el in glyph:el.tag=ns+'path'
            mg.append(glyph)
            compound=p['meter'] in ('6/8','9/8','12/8')
            if compound:ET.SubElement(mg,ns+'circle',cx='305',cy='-100',r='34',fill='black')
            bpm=int(p['bpm']/1.5) if compound else p['bpm']
            tt=ET.SubElement(mg,ns+'text',x='410' if compound else '300',y='0',attrib={'font-size':'405px','font-family':'Times, serif'})
            tt.text=f'= {bpm}'
        svg=ET.tostring(root,encoding='unicode')
        (d/f'{stem}_page_{i}.svg').write_text(svg)
        # The engraved body is vector-based and placed below a separate typographic header.
        raw=cairosvg.svg2pdf(bytestring=svg.encode(),output_width=A4[0]*4/3,output_height=708*4/3)
        musicpage=PdfReader(io.BytesIO(raw)).pages[0]
        buff=io.BytesIO();c=canvas.Canvas(buff,pagesize=A4)
        c.setTitle(p['title']+f' | CWS Op. {p["op"]}');c.setAuthor('CWS Library - studies with Maple (AI)')
        c.setFillColor(HexColor('#2f3b38'));c.setFont('Helvetica',9)
        c.drawString(35,807,' '.join(series_for(p['op'])['header']))
        c.setFillColor(HexColor('#151e1b'));c.setFont('Times-Roman',27)
        c.drawString(35,772,p['title'])
        c.setFont('Helvetica',10);c.drawRightString(A4[0]-35,775,f'CWS Op. {p["op"]}')
        c.setStrokeColor(HexColor('#c8d0ca'));c.setLineWidth(.5);c.line(35,751,A4[0]-35,751)
        c.setFillColor(HexColor('#5a6660'));c.setFont('Courier',8)
        c.drawString(35,22,p['composition_stamp'])
        if tk.getPageCount()>1:c.drawRightString(A4[0]-35,22,str(i))
        c.showPage();c.save()
        page=PdfReader(io.BytesIO(buff.getvalue())).pages[0]
        # 708-point notation area at y=28; its top is 736, immediately under rule.
        page.merge_translated_page(musicpage,0,28)
        writer.add_page(page)
    with (d/(stem+'.pdf')).open('wb') as f:writer.write(f)
    # A reflow can reduce the page count. Remove only obsolete generated
    # numbered SVG pages, after the replacement score has been written.
    for previous in d.glob(stem+'_page_*.svg'):
        page_number=previous.stem.removeprefix(stem+'_page_')
        if page_number.isdigit() and int(page_number)>tk.getPageCount():
            previous.unlink()
    (WORK/f'{stem}.mei').write_text(tk.getMEI())
    (WORK/f'{stem}_timemap.json').write_text(json.dumps(tk.renderToTimemap(),indent=2))
    p['pages']=tk.getPageCount()
    (d/(stem+'.json')).write_text(json.dumps(p,indent=2)+'\n')
(ROOT/'data/catalog.json').write_text(json.dumps(cat,indent=2)+'\n')
