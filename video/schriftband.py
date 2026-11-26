#!/usr/bin/env python3
"""Kontaktblatt mit einer LINIE auf der Schrift-Oberkante.

Entstanden aus drei Runden an derselben Beschwerde. Eine Zahl am Lineal
abzulesen hat zweimal 120-150 px Fehler gebracht; eine durchgezogene Linie
auf der Hoehe, auf der die Schrift steht, macht die Frage binaer: liegt sie
auf seinem Kiefer oder darunter. Gezeichnet wird aus der NACKTEN Fassung,
sonst verdeckt die Schrift genau das, was man sehen will.

Achtung, der Fehler, den dieses Skript schon einmal hatte: die Linie muss
UNABHAENGIG vom Lineal-Raster gezeichnet werden. Stand 1010 nicht auf dem
Raster, wurde sie stillschweigend gar nicht gezeichnet - und dann schaetzt
man wieder.

    python3 video/schriftband.py nackt.mp4 blatt.png
"""
import subprocess, os, tempfile, imageio_ffmpeg, sys
from PIL import Image, ImageDraw
FF=imageio_ffmpeg.get_ffmpeg_exe()
quelle=sys.argv[1]; ziel=sys.argv[2]
VON,BIS=760,1180
grenzen=[(0.3,18.6),(19.0,31.0),(31.3,46.1),(46.5,70.3)]
proben=4
PB,PH=540,(BIS-VON)//2
ims=[]
with tempfile.TemporaryDirectory() as t:
    for si,(a,b) in enumerate(grenzen,1):
        for k in range(proben):
            tt=a+(b-a)*k/(proben-1)
            p=os.path.join(t,f'{si}_{k}.png')
            subprocess.run([FF,'-nostdin','-v','error','-y','-ss',f'{tt:.3f}','-i',quelle,
                '-frames:v','1','-vf',f'crop=1080:{BIS-VON}:0:{VON},scale={PB}:{PH}',p],
                capture_output=True)
            im=Image.open(p).convert('RGB'); zg=ImageDraw.Draw(im); s=PH/(BIS-VON)
            for v in range(800,BIS,50):                       # Lineal
                y=(v-VON)*s
                zg.line([(0,y),(26,y)],fill=(60,255,60),width=1)
                zg.text((30,y-5),str(v),fill=(160,255,160))
            for v,f in ((1010,(255,40,40)),(1075,(255,140,40))):   # Schriftband
                y=(v-VON)*s
                zg.line([(0,y),(PB,y)],fill=f,width=1)
            zg.text((PB-150,3),f"E{si} {tt:.1f}s",fill=(255,230,0))
            ims.append(im)
bl=Image.new('RGB',(proben*PB,4*PH),(10,10,10))
for c,im in enumerate(ims): bl.paste(im,((c%proben)*PB,(c//proben)*PH))
bl.save(ziel); print(ziel, bl.size)
