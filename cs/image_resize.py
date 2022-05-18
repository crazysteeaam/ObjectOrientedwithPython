#模块：c:/pythonpa/cs/image_resize.py
#命令行：python image_resize.py c:/pythonpa/cs/img jpg 640 480
#功能：把c:/pythonpa/cs/img下的所有*.jpg文件大小调整为640*480并另存为*_640.jpg
import sys
import os
import glob
import PIL.Image
img_path = sys.argv[1] + "/*." + sys.argv[2]
img_suffix = sys.argv[2]
img_size_width = int(sys.argv[3])
img_size_height = int(sys.argv[4])
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)
    outfile = f + "_" + str(img_size_width) + "." + img_suffix
    im = PIL.Image.open(infile)
    im_out = im.resize((img_size_width, img_size_height))
    im_out.save(outfile)