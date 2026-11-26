#!/usr/bin/env python3
"""Kinnhoehe je Einstellung im FERTIGEN Bildmass ablesen.

Warum das ein eigenes Werkzeug ist: zwei Fassungen hintereinander hatten die
Schrift rechnerisch auf einer Hoehe und im Bild um bis zu 295 px daneben,
weil die Kinnwerte in kastenrelativen Quellpixeln abgelesen und als absolute
Quellpixel weiterverrechnet wurden. Hier wird in derselben Zahl gemessen, in
der auch `lippe` steht: nach crop UND scale, 0..1920 im Ausgabebild.

Mehrere Proben je Einstellung, weil der Sprecher sich lehnt - eine Probe aus
der Mitte sagt nichts ueber die Raender. Und gross genug zum Ablesen: der
Fensterausschnitt 600-1250 auf 540 px Breite, Lineal alle 25 px, laesst sich
auf etwa 10 px genau lesen.

    python3 video/kinnhoehe.py plan.json 3 blatt.png

Danach `schriftlage.py` auf die fertige Datei - das ist die Gegenprobe.
"""
import subprocess, json, os, tempfile, imageio_ffmpeg, sys
from PIL import Image, ImageDraw
FF=imageio_ffmpeg.get_ffmpeg_exe()
plan=sys.argv[1]; proben=int(sys.argv[2]); ziel=sys.argv[3]
VON,BIS=600,1250                      # Fensterausschnitt im fertigen Bild
d=json.load(open(plan)); q=d['quelle']
PB,PH=540,(BIS-VON)//2
ims=[]
with tempfile.TemporaryDirectory() as t:
    for i,e in enumerate(d['einstellungen'],1):
        x,y,b,h=(int(v) for v in e['kasten'].split(':'))
        for k in range(proben):
            tt=e['start']+(e['ende']-e['start'])*(k+0.5)/proben
            p=os.path.join(t,f'{i}_{k}.png')
            subprocess.run([FF,'-nostdin','-v','error','-y','-ss',f'{tt:.3f}','-i',q,
                '-frames:v','1','-vf',
                f'crop={b}:{h}:{x}:{y},scale=1080:1920,crop=1080:{BIS-VON}:0:{VON},scale={PB}:{PH}',p],
                capture_output=True)
            im=Image.open(p).convert('RGB'); zg=ImageDraw.Draw(im); s=PH/(BIS-VON)
            for v in range(VON,BIS,25):
                yy=(v-VON)*s
                lang = 60 if v%100==0 else (30 if v%50==0 else 12)
                zg.line([(0,yy),(lang,yy)],fill=(60,255,60),width=1)
                if v%50==0: zg.text((64,yy-5),str(v),fill=(150,255,150))
            zg.text((PB-120,3),f"E{i}.{k+1} {tt:.0f}s",fill=(255,230,0))
            ims.append(im)
bl=Image.new('RGB',(proben*PB,4*PH),(10,10,10))
for c,im in enumerate(ims): bl.paste(im,((c%proben)*PB,(c//proben)*PH))
bl.save(ziel); print(ziel, bl.size)
