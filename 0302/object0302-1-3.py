import sys
import os
import glob
from PIL import Image

img_path = sys.argv[1]+"/*."+sys.argv[2]
img_suffix = sys.argv[2]
log_file = sys.argv[3]
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f+"_w."+img_suffix
    im = Image.open(infile)
    im_log = Image.open(log_file)
    im_mark = Image.new("RGBA", im.size)
    im_mark.paste(im_log, (0, 0))
    im_out = Image.composite(im_mark, im, im_mark)
    im_out.save(outfile)
