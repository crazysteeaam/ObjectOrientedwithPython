#模块：c:/pythonpa/cs/image_thumbnail.py
#命令行：python image_thumbnail.py c:/pythonpa/cs/img jpg
#功能：把c:/pythonpa/cs/img下的所有*.jpg文件转换为*_s.jpg缩略图
import sys
import os
import glob
import PIL.Image
img_path = sys.argv[1] + "/*." + sys.argv[2]
size = (128,128)
for infile in glob.glob(img_path):
    f,e = os.path.splitext(infile)
    outfile = f + "_s." + sys.argv[2]
    img = PIL.Image.open(infile)
    img.thumbnail(size, PIL.Image.ANTIALIAS)
    img.save(outfile)
