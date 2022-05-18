import urllib
import time
from selenium import webdriver


class Crawler:

    def __init__(self):
        self.url = 'http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%9C%BA&oq=shouji&rsp=1'  # url to crawl
        # self.img_xpath = '//ul/li/div/a/img'  # xpath of img element
        # self.download_xpath = '//divul/li/div/div/span/a[@class="downloadicon"]'  # xpath of download link element
        self.img_xpath = '//div[@class="imgpage"]/ul/li[@class="imgitem"]'
        self.img_dic = {}

        # kernel function

    def get_img_urls(self):
        """抓取图像的URL和title，存储到字典self.img_dic"""
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.url)

        # 模拟滚动窗口以浏览下载更多图片
        pos = 0
        for i in range(2):
            pos += i * 500  # 每次下滚500
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            images = driver.find_elements_by_xpath(self.img_xpath)
            for img in images:
                img_title = self.replace_mark_with_underscore(img.get_attribute('data-title'))
                img_url = img.get_attribute('data-objurl')
                self.img_dic[img_url] = img_title
                print(self.img_dic[img_url])
        driver.close()

    def replace_mark_with_underscore(self, s):
        invalid_set = ('<strong>','</strong>','\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ')
        for i in invalid_set:
            s = s.replace(i, '_')
        return s

    def download_images(self):
        if img_url != None and not img_url_dic.has_key(img_url):
            img_url_dic[img_url] = ''
            ext = img_url.split('.')[-1]
            filename = img_desc + '.' + ext
            print(img_desc, img_url)
            urllib.request.urlretrieve(img_url, 'c:/temp/'.format(filename))
            time.sleep(1)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.get_img_urls()