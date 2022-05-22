from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests


def get_pic(url):
    driver = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver.exe')
    driver.maximize_window()  # 最大化窗口
    # 请求
    driver.get(url)
    time.sleep(3)
    print("ok")

    # driver.save_screenshot('quekou2.png')
    # element = driver.find_element(by=By.ID, value='tcaptcha_iframe')
    # left_iframe = element.location['x'] * 1.5  # location：获取元素位置
    # top_iframe = element.location['y'] * 1.5
    # print("iframe的位置：", left_iframe, top_iframe)
    # 找到图片
    driver.switch_to.frame('tcaptcha_iframe')
    # element = driver.find_element(by=By.ID, value='slideBg')
    # # 开始局部截图
    # # 计算截图范围
    # width = int(element.size['width'] * 1.5)
    # height = int(element.size['height'] * 1.5)
    # left = element.location['x'] * 1.5  # location：获取元素位置
    # right = (element.location['x'] + element.size['width']) * 1.5  # size：获取元素大小
    # top = (element.location['y']) * 1.5
    # bottom = (element.location['y'] + element.size['height']) * 1.5
    # print("缺口图宽度和高度", element.size['width'], element.size['height'])
    # print("缺口图在iframe中的位置", left, right, top, bottom)
    # # 打开图片
    # im = Image.open('quekou2.png')
    # # 开始局部截图
    # print("挖掘位置", left + left_iframe, top + top_iframe, right + left_iframe, bottom + top_iframe)
    # im = im.crop((left + left_iframe, top + top_iframe + 1, right + left_iframe, bottom + top_iframe + 1))
    # im.save('quekou_jubu.png')

    # 获取无缺图链接
    element = driver.find_element(by=By.ID, value='cdn1')
    quekou_picurl = element.get_attribute('src')
    get_quekou(quekou_picurl)
    wuque_list_picurl = list(quekou_picurl)
    wuque_list_picurl[-10] = '0'
    wuque_picurl = ''.join(wuque_list_picurl)
    get_wuque(wuque_picurl)
    resize_image('quekou_jubu.png', int(680 * 1.5), int(390 * 1.5))
    resize_image('wuque_jubu.png', int(680 * 1.5), int(390 * 1.5))
    wuque_jubu = Image.open('wuque_jubu.png')
    quekou_jubu = Image.open('quekou_jubu.png')
    distance = get_difference(wuque_jubu, quekou_jubu) / (680*1.5) * (196.46*1.5)
    print(distance)
    huakuai = driver.find_element(by=By.ID, value='tcaptcha_drag_thumb')
    ActionChains(driver).click_and_hold(on_element=huakuai).perform()
    tracks = get_tracks(distance-10)
    print(tracks)
    for track in tracks:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    time.sleep(1)
    ActionChains(driver).release().perform()
    time.sleep(15)
    return 0


def get_quekou(url):
    # 截取无缺口图片
    driver3 = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver.exe')
    driver3.maximize_window()  # 最大化窗口
    # 请求
    driver3.get(url)
    time.sleep(3)
    print("ok")
    driver3.save_screenshot('quekou2.png')
    # 开始局部截图
    # 计算截图范围
    left = 513.667 * 1.5  # location：获取元素位置
    right = (513.667 + 680) * 1.5  # size：获取元素大小
    top = 263 * 1.5
    bottom = (263 + 390) * 1.5

    im = Image.open('quekou2.png')
    # 开始局部截图
    im = im.crop((left, top, right, bottom))
    im.save('quekou_jubu.png')


def get_wuque(url):
    # 截取无缺口图片
    driver2 = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver.exe')
    driver2.maximize_window()  # 最大化窗口
    # 请求
    driver2.get(url)
    time.sleep(3)
    print("ok")
    driver2.save_screenshot('wuque.png')
    # 开始局部截图
    # 计算截图范围
    left = 513.667 * 1.5  # location：获取元素位置
    right = (513.667 + 680) * 1.5  # size：获取元素大小
    top = 263 * 1.5
    bottom = (263 + 390) * 1.5

    im = Image.open('wuque.png')
    # 开始局部截图
    im = im.crop((left, top, right, bottom))
    im.save('wuque_jubu.png')

    # 定义计算移动距离的函数


def get_difference(image1, image2):
    """
    循环每一个点，计算出对应的像素值
    """
    # 外层循环循环长度
    for i in range(10, image1.width):
        # 内层循环循环宽度
        for j in range(10, image1.height):
            # 找出缺口
            if not is_similar(image1, image2, i, j):
                return i  # 此时的i即为缺口距离


# 定义找出缺口位置的函数
def is_similar(image1, image2, x, y):
    # 计算RGB值
    pixel1 = image1.getpixel((x, y))
    pixel2 = image2.getpixel((x, y))
    # 设置一个容差范围，设置30位容差范围
    if abs(pixel1[0] - pixel2[0]) > 30 and abs(pixel1[1] - pixel2[1]) > 30 and abs(pixel1[2] - pixel2[2]) > 30:
        return False
    return True


# 修改图片大小
def resize_image(image, new_width=0, new_height=0):
    img = Image.open(image)
    out = img.resize((new_width, new_height), Image.ANTIALIAS)  # resize image with high-quality
    out.save(image)


def get_tracks(distance):
    """
    v = v0+at
    x = v0t+1/2at**2
    """
    # 定义存放运动轨迹的列表
    tracks = []
    # 定义初速度
    v = 0
    # 定义单位时间
    t = 0.5
    # 定义匀加速运动和匀减速运动的分界线
    mid = distance * 4 / 5
    # 定义当前位移
    current = 0
    # 为了一直移动，定义循环
    while current < distance:
        if mid > current:
            a = 2
        else:
            a = -3
        v0 = v
        # 计算位移
        x = v0 * t + 1 / 2 * a * t ** 2
        # 计算滑块当前位移
        current += x
        # 计算末速度
        v = v0 + a * t
        tracks.append(round(x))
    return tracks


if __name__ == '__main__':
    distance = get_pic("https://www.maoyan.com/board/4?timeStamp=1653152477741&channelId=40011&index=6&signKey=e568bfb6ef1bb961ee9cc12517a3f1c2&sVersion=1&webdriver=false")
