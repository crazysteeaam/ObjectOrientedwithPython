import sys
import PIL.Image
import PIL.ImageFilter

#2.3图像的基本操作
im = PIL.Image.open(sys.argv[1])
width, height = im.size

res = PIL.Image.new(im.mode, (2*width, 2*height))

res.paste(im, (0, 0, width, height))

contour = im.filter(PIL.ImageFilter.CONTOUR)
res.paste(contour, (width, 0, 2*width, height))

emboss = im.filter(PIL.ImageFilter.EMBOSS)
res.paste(emboss, (0, height, width, 2*height))

edges = im.filter(PIL.ImageFilter.FIND_EDGES)
res.paste(edges, (width, height, 2*width, 2*height))

res.show()
