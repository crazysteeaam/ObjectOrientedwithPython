from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

class ImageBaiduSpider():
    ''' 爬取百度图片中的图片 '''
    def __init__(self, url, keyword, page_total, down_dir):
        self.url = url #主页网址
        self.keyword = keyword #查询关键字
        self.page_total = page_total #下载总页数
        self.down_dir = down_dir #下载保存地址
        #百度图像页面中图像的路径
        self.img_xpath = '//div[@class="imgpage"]/ul/li[@class="imgitem"]'
        self.img_dic = {} #保存图像url的字典：url:title

    def get_img_urls(self):
        """抓取图像的URL和title，存储到字典self.img_dic"""

        # 打开浏览器， 打开url的网页
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.url)
        # 模拟在百度图片搜索中输入关键字，并进行搜索
        inputElement = driver.find_element_by_name('word')
        inputElement.send_keys(self.keyword)
        inputElement.submit()
        time.sleep(2)  # 睡眠2秒钟

        page_i = 0

        while page_i < self.page_total:
            #获取页面中图像的url和title，并保存到字典self.img_dic中
            images = driver.find_elements_by_xpath(self.img_xpath)
            for img in images:
                img_title = self.replace_mark_with_underscore(img.get_attribute('data-title'))
                img_url = img.get_attribute('data-objurl')
                self.img_dic[img_url] = img_title
                # print(self.img_dic[img_url])
            #模拟按【下一页】键，处理下一页
            page_i += 1
            action = ActionChains(driver).send_keys(Keys.DOWN)
            action.perform()
        driver.close()

    def download(self):
        #使用urllib.request.urlretrieve下载图像，使用opener加header，避免被屏蔽
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        for url in self.img_dic:
            title = self.img_dic[url]
            ext = url.split('/')[-1]
            filename = title + '.' + ext
            # print(filename)
            filepath = os.path.join(self.down_dir, filename)
            if os.path.exists(filepath):
                print("已经存在：{0}".format(filepath))
            else:
                try:
                    print("正在下载：{0}".format(filepath))
                    urllib.request.urlretrieve(url, filepath)
                    time.sleep(3)
                except Exception as e:
                    print(e)
                    print("下载失败：{0}".format(filepath))

    def replace_mark_with_underscore(self, s):
        """把特殊字符替换为下划线"""
        invalid_set = ('<strong>','</strong>','\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ')
        for i in invalid_set:
            s = s.replace(i, '_')
        return s

if __name__ == "__main__":
    url = "http://image.baidu.com"
    #查询关键字
    keyword = "彩虹"
    #下载的总页数
    pages = 2
    #图片下载路径，如果不存在，则创建
    down_dir = "C:\\temp\\" + keyword
    if not os.path.exists(down_dir):
        os.makedirs(down_dir)
    spider = ImageBaiduSpider(url, keyword, pages, down_dir)
    spider.get_img_urls()
    spider.download()