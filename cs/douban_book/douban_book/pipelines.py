# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs

class DoubanBookPipeline(object):
    def __init__(self):
        self.filename = 'douban_book_top250.csv'
        # 先给文件写一个Windows系统用来识别编码的头
        with open(self.filename, 'wb') as f:
            f.write(codecs.BOM_UTF8)  # 避免乱码
        # 使用append模式打开文件，写入标题
        with open(self.filename, 'a', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f, dialect='excel')
            f_csv.writerow(['书名','作者','评分','评价','评价人数',
                            '出版日期','单价','URL'])
    def process_item(self, item, spider):
        # 使用append模式打开文件，继续写入
        with open(self.filename, 'a', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f, dialect='excel')
            f_csv.writerow([item['bookname'],item['author'],item['rating_nums'],
                            item['quote'],item['comment_nums'],item['pubdate'],
                            item['price'],item['url']])
        return item
