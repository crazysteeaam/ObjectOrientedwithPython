import scrapy
from scrapy import selector
from scrapy import item
import re
from douban_book.items import DoubanBookItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']
    url_pattern = 'https://book.douban.com/top250?start={0}'
    for i in range(1):
        start_urls.append(url_pattern.format(i))

    def parse(self, response):
        selector = scrapy.selector.Selector(response)
        infos = selector.xpath('//tr[@class="item"]')
        item = DoubanBookItem()
        for info in infos:
            bookname = info.xpath('td/div/a/@title').extract()[0]
            url = info.xpath('td/a[@class="nbg"]/@href').extract()[0]
            authors = info.xpath(
                'td/p[@class="pl"]/text()').extract()[0].split('/')
            author = authors[0]
            pubdate = authors[-2]
            price = authors[-1]
            rating = info.xpath(
                'td/div/span[@class="rating_nums"]/text()').extract()[0]
            comment_nums = info.xpath(
                'td/div/span[@class="pl"]/text()').extract()[0]
            comment_nums = re.sub('\D', '', comment_nums)
            quote = info.xpath('td/p/span[@class="inq"]/text()').extract()
            if len(quote) > 0:
                quote = quote[0]
            else:
                quote = ''
            item['bookname'] = bookname
            item['author'] = author
            item['rating_nums'] = rating
            item['quote'] = quote
            item['comment_nums'] = comment_nums
            item['pubdate'] = pubdate
            item['url'] = url
            item['price'] = price
            yield item
        pass
