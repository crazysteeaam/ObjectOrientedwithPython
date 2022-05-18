#模块：c:/pythonpa/cs/image_test.py
#命令行：python image_test.py c:/pythonpa/cs/img/mandrill.jpg
#功能：把c:/pythonpa/cs/img/mandrill.jpg的4个副本排列成2×2网格并显示
import sys
import os
import PIL.Image
import PIL.ImageFilter

im = PIL.Image.open(sys.argv[1])
width, height = im.size

# 创建新图像，大小为原始图像的4倍
res = PIL.Image.new(im.mode, (2*width, 2*height))

# 把原始图像放置在左上角
res.paste(im, (0, 0, width, height))

# 把轮廓过滤CONTOUR的图像放置在右上角
contour = im.filter(PIL.ImageFilter.CONTOUR)
res.paste(contour, (width, 0, 2*width, height))

# 把浮雕过滤EMBOSS的图像放置在左下角
emboss = im.filter(PIL.ImageFilter.EMBOSS)
res.paste(emboss, (0, height, width, 2*height))

# 把边缘过滤FIND_EDGES的图像放置在右下角
edges = im.filter(PIL.ImageFilter.FIND_EDGES)
res.paste(edges, (width, height, 2*width, 2*height))
# 显示结果图像
res.show()

