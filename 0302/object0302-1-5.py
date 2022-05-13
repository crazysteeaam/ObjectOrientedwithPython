import sys
import os
import PIL.Image
import glob

# 批量图像格式转换
img_path = sys.argv[1]+"/*."+sys.argv[2]
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f+"."+sys.argv[3]
    PIL.Image.open(infile).save(outfile)
