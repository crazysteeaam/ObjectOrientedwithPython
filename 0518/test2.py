from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests
import urllib.request
import re



if __name__ == '__main__':
    _content = {}
    driver = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver.exe')
    driver.maximize_window()  # 最大化窗口
    driver.get('https://www.maoyan.com/')
    driver.refresh()
    time.sleep(6)
    print("ok")

    aclick = driver.find_element(by=By.XPATH,
                                 value='//div[@class="top100-wrapper"]/div[@class="panel"]/div[@class="panel-header"]/span[@class="panel-more"]/a[@class="textcolor_orange"]')
    ActionChains(driver).click(on_element=aclick).perform()
    time.sleep(6)

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         + '.*?<img src="(.+?)"'
                         + '.*?<p class="name"><a.*?">(.+?)</a>'
                         + '.*?<p class="star"><a.*?">(.+?)</p>'
                         + '.*?<p class="releasetime">(.+?)</p>'
                         + '.*?<p class="score"><i class="integer">(.+?)</i>'
                         + '.*?<i class="fraction">(.*?)</i>.*?</dd>', re.S)
    data = driver.page_source
    print(data)
    items = re.findall(pattern, data)
    print(items)
    for item in items:
        board_index = item[0]
        image_url = item[1]
        name = item[2]
        star = item[3].strip()[3:]
        time = item[4].strip()[5:]
        score = item[5] + item[6]
        _content[board_index] = [name, star, time, score, image_url]
        print(_content[board_index])