from PIL import Image


def crop(im, box):
    x1, y1, x2, y2 = box
    width, height = x2-x1, y2-y1
    im_new = Image.new(im.mode, (width, height))
    for i in range(width):
        for j in range(height):
            pix = im.getpixel((x1+i, y1+j))
            im_new.putpixel((i, j), pix)
    return im_new


if __name__ == '__main__':
    im = Image.open('D:/20212022s/objectoriented2022/0309/1.png')
    newwidth, newheight = im.size
    box = 0, 0, 10*newwidth, 10*newheight
    crop(im, box).show
