# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    author = scrapy.Field()
    rating_nums = scrapy.Field()
    quote = scrapy.Field()
    comment_nums = scrapy.Field()
    pubdate = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    pass
