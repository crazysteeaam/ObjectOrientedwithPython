import sys
import os
import glob
import PIL.Image

# 批量创建缩略图
img_path = sys.argv[1]+"/*."+sys.argv[2]
size = (128, 128)
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f+"_s."+sys.argv[2]
    img = PIL.Image.open(infile)
    img.thumbnail(size, PIL.Image.ANTIALIAS)
    img.save(outfile)
