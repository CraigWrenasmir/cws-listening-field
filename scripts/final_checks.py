from pathlib import Path
import subprocess,json,argparse
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pieces';WORK=ROOT/'work';cat=json.loads((ROOT/'data/catalog.json').read_text())
(WORK/'qa').mkdir(parents=True,exist_ok=True)
parser=argparse.ArgumentParser();parser.add_argument('--opus',type=int,nargs='+');args=parser.parse_args()
for p in cat:
 if args.opus is not None and p['op'] not in args.opus:continue
 d=OUT/p['folder'];stem=p['stem']
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(d/(stem+'.mp3')),'-f','f32le','-acodec','pcm_f32le','-'])
 x=np.frombuffer(raw,dtype=np.float32);peak=float(np.max(np.abs(x)));rms=float(np.sqrt(np.mean(x*x)))
 assert .01<rms<.25 and peak<.99,(stem,peak,rms)
 print(p['title'],'decoded MP3 peak',round(peak,3),'RMS',round(rms,3))
 subprocess.run(['pdftoppm','-scale-to','1500','-png',str(d/(stem+'.pdf')),str(WORK/'qa'/f'final_{p["op"]}')],check=True)
