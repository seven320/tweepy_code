#encoding:utf-8
import os,glob
from PIL import Image

files=glob.glob("/Users/kenkato/Pictures/forbot/*.jpg")

for file in files:
    while True:
        photobyte=os.path.getsize(file)
        if photobyte>5*(2**10)**2:
            img=Image.open(file)
            img_resize=img.resize((int(img.width/2),int(img.height/2)),Image.LANCZOS)
            ftitle,fext=os.path.splitext(file)
            img_resize.save(ftitle+fext)
        else:
            break
