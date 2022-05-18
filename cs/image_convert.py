#模块：c:/pythonpa/cs/image_convert.py
#命令行：#python image_convert.py c:/pythonpa/cs/img jpg png
#功能：把c:/pythonpa/cs/img下的所有jpg文件转换为png文件
import sys
import os
import glob
import PIL.Image
img_path = sys.argv[1] + "/*." + sys.argv[2]
for infile in glob.glob(img_path):
    f,e = os.path.splitext(infile)
    outfile = f + "." + sys.argv[3]
    PIL.Image.open(infile).save(outfile)
