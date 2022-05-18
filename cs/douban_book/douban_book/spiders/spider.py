# -*- coding: utf-8 -*-
import scrapy
from douban_book.items import DoubanBookItem
import re

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['book.douban.com']
    #构造要爬取的URL列表
    start_urls = []
    url_pattern = 'https://book.douban.com/top250?start={0}'
    for i in range(0, 250, 25):
        start_urls.append(url_pattern.format(i))

    def parse(self, response):
        selector = scrapy.selector.Selector(response)
        # 页面中所有的榜单信息
        infos = selector.xpath('//tr[@class="item"]')
        # 创建DoubanBookItem实例对象
        item = DoubanBookItem()
        # 循环抽取各榜单信息，并保存到item中
        for info in infos:
            bookname = info.xpath('td/div/a/@title').extract()[0] #书名
            url = info.xpath('td/a[@class="nbg"]/@href').extract()[0] #URL
            authors = info.xpath('td/p[@class="pl"]/text()').extract()[0].split('/')
            author = authors[0] #作者
            pubdate = authors[-2] #出版日期
            price = authors[-1] #单价
            # 评分
            rating = info.xpath('td/div/span[@class="rating_nums"]/text()').extract()[0]
            # 评价人数
            comment_nums = info.xpath('td/div/span[@class="pl"]/text()').extract()[0]
            comment_nums = re.sub("\D", "", comment_nums)
            # 评价
            quote = info.xpath('td/p/span[@class="inq"]/text()').extract()
            if len(quote) > 0:
                quote = quote[0]
            else:
                quote = ''

            # 设置item
            item['bookname'] = bookname
            item['author'] = author
            item['rating_nums'] = rating
            item['quote'] = quote
            item['comment_nums'] = comment_nums
            item['pubdate'] = pubdate
            item['price'] = price
            item['url'] = url
            yield item


