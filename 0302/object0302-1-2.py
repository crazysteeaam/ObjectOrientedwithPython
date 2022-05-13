import sys
import os
import glob
from PIL import Image, ImageDraw, ImageFont

img_path = sys.argv[1]+"/*."+sys.argv[2]
img_suffix = sys.argv[2]
txt_log = sys.argv[3]
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f+"_w."+img_suffix
    im = Image.open(infile)
    im_log = Image.new("RGBA", im.size)
    fnt = ImageFont.truetype("C:/Windows/fonts/Tahoma.ttf", 20)
    d = ImageDraw.ImageDraw(im_log)
    d.text((0, 0), txt_log, font=fnt)
    im_out = Image.composite(im_log, im, im_log)
    im_out.save(outfile)
