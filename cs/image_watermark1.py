#模块：c:/pythonpa/cs/image_watermark1.py
#命令行：python image_watermark1.py c:/pythonpa/cs/img jpg "Python"
#功能：把c:/pythonpa/cs/img下的所有*.jpg文件加"Python"水印并另存为*_w.jpg
import sys
import os
import glob
from PIL import Image, ImageDraw, ImageFont
img_path = sys.argv[1] + "/*." + sys.argv[2]
img_suffix = sys.argv[2]
txt_log = sys.argv[3]
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f + "_w." + img_suffix
    im = Image.open(infile)
    im_mark = Image.new('RGBA', im.size)
    fnt = ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
    d = ImageDraw.ImageDraw(im_mark)
    d.text((0, 0), txt_log, font = fnt)
    im_out = Image.composite(im_mark, im, im_mark)
    im_out.save(outfile)