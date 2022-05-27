from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import re
import faker
import json
import csv
import codecs
from PIL import Image

fake = faker.Factory.create()
headers = {'Connection': 'keep-alive', 'User-Agent': fake.user_agent()}
_content = {}
driver = ''


def download_parse():
    global _content
    global driver
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         + '.*?<img.+?src="(.+?)"'
                         + '.*?<p class="name"><a.*?">(.+?)</a>'
                         + '.*?<p class="star">(.+?)</p>'
                         + '.*?<p class="releasetime">(.+?)</p>'
                         + '.*?<p class="score"><i class="integer">(.+?)</i>'
                         + '.*?<i class="fraction">(.*?)</i>.*?</dd>'
                         , re.S)
    data = driver.page_source
    items = re.findall(pattern, data)
    for item in items:
        board_index = item[0]
        image_url = item[1]
        name = item[2]
        star = item[3].replace('\n', '').replace('\r', '').replace(' ', '')
        time = item[4].strip()[5:]
        score = item[5] + item[6]
        _content[board_index] = [name, star, time, score, image_url]
        print(_content[board_index])


def save_json(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(_content, ensure_ascii=False))


def save_csv(filename):
    with open(filename, 'wb') as f:
        f.write(codecs.BOM_UTF8)
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f, dialect='excel', )
        f_csv.writerow(['排名', '影片名词', '主演', '上演时间', '得分', '电影海报URL'])
        for (k, v) in _content.items():
            f_csv.writerow([k, v[0], v[1], v[2], v[3], v[4]])


def get_pic():
    driver.switch_to.frame('tcaptcha_iframe')

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


def main():
    global driver
    driver = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver.exe')
    driver.maximize_window()  # 最大化窗口
    driver.get('https://www.maoyan.com/')
    driver.refresh()
    time.sleep(6)
    # get_pic()
    # time.sleep(5)
    print("ok")
    aclick = driver.find_element(by=By.XPATH,
                                 value='//div[@class="top100-wrapper"]/div[@class="panel"]/div[@class="panel-header"]/span[@class="panel-more"]/a[@class="textcolor_orange"]')
    ActionChains(driver).click(on_element=aclick).perform()
    time.sleep(6)
    a = 8
    for i in range(10):
        download_parse()
        save_json('maoyan_top100.json')
        save_csv('maoyan_top100.csv')
        if i == 1:
            a += 1
        if i == 4:
            a += 2
        if i == 6:
            a -= 2
        if i == 9:
            break
        nextclick = driver.find_element(by=By.XPATH,
                                        value='//ul[@class="list-pager"]/li[' + str(a) + ']/a[@class="page_' + str(
                                            i + 2) + '"]')
        ActionChains(driver).click(on_element=nextclick).perform()


if __name__ == '__main__':
    main()
