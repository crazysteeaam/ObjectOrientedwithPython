#模块：c:/pythonpa/cs/image_process.py
import PIL.Image

def copy(im):
    """返回拷贝后的图像对象"""

    # 创建与原始图像相同模式和大小的新图像对象
    im_new = PIL.Image.new(im.mode, im.size)
    width, height = im.size
    # 使用嵌套循环，把旧图像位置(i, j)的像素复制到新图像的位置(i, j)
    for i in range(width):
        for j in range(height):
            pix = im.getpixel((i,j))
            im_new.putpixel((i,j), pix)
    return im_new

def crop(im, box):
    """返回使用矩形框剪切后的图像对象"""
    
    # 剪切框定义左上角和右下角坐标位置
    x1,y1,x2,y2 = box
    # 计算新图像的宽度width和高度height，并创建新图像
    width,height = x2-x1, y2-y1
    im_new = PIL.Image.new(im.mode, (width, height))
    # 使用嵌套循环，把旧图像剪切框内的像素拷贝到新图像
    for i in range(width):
        for j in range(height):
            pix = im.getpixel((x1+i,y1+j))
            im_new.putpixel((i,j), pix)
    return im_new

def flip(im, orient="H"):
    """返回水平或垂直翻转后的图像对象"""
    
    # 获取图像的宽度width和高度height，并创建新图像
    width,height = im.size
    im_new = PIL.Image.new(im.mode, im.size)
    # 使用嵌套循环，把旧图像的像素拷贝到新图像对应位置
    for i in range(width):
        for j in range(height):
            pix = im.getpixel((i,j))
            if orient == "H": #水平翻转时
                # 原始图像的像素(i,j)映射到目标图像的位置(width-i-1,j)
                im_new.putpixel((width-i-1,j), pix)
            else: #垂直翻转时
                # 原始图像的像素(i,j)映射到目标图像的位置(i,height-j-1)
                im_new.putpixel((i,height-j-1), pix)
    return im_new

def rotate(im, orient="CC"):
    """返回逆时针或顺时针旋转90度后的图像对象"""
    
    # 获取图像的宽度width和高度height，并创建新图像
    width,height = im.size
    im_new = PIL.Image.new(im.mode, im.size)
    # 使用嵌套循环，把旧图像的像素拷贝到新图像对应位置
    for i in range(0, width):
        for j in range(0, height):
            pixel = im.getpixel((i,j))
            if orient == "CC": #逆时针针旋转90度时
                # 原始图像的像素(i,j)映射到目标图像的位置(j,width-i-1)
                im_new.putpixel((j, width-i-1), pixel)
            else: #顺时针旋转90度时
                # 原始图像的像素(i,j)映射到目标图像的位置(height-j-1,i)
                im_new.putpixel((height-j-1, i), pixel)              
    return im_new


def smooth(im):
    """返回平滑后的图像"""
    # 获取图像的宽度width和高度height，并创建新图像
    width,height = im.size
    im_new = PIL.Image.new(im.mode, im.size)
    # 使用嵌套循环，把旧图像的像素拷贝到新图像对应位置
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = 0, 0, 0 #初始化
            numPixels = 0
            for c in range(max(0, i-1), min(width, i+2)):
                for r in range(max(0, j-1), min(height, j+2)):
                    numPixels +=1
                    pix = im.getpixel((c, r))
                    r += pix[0]
                    g += pix[1]
                    b += pix[2]
            # 计算平均值
            r = r // numPixels
            g = g // numPixels
            b = b // numPixels
            im_new.putpixel((i, j), (r, g, b))
    return im_new

#测试代码
if __name__ == "__main__":
    im = PIL.Image.open("c:/pythonpa/cs/img/mandrill.jpg")
#    copy(im).show()
#    crop(im, (50, 50, 100, 100)).show()
#    im1 = im.rotate(60)
#    flip(im, orient="H").show()
#    flip(im, orient="V").show()
#    rotate(im, orient="CC").show()
#    rotate(im, orient="CL").show()
    smooth(im).show()
    
