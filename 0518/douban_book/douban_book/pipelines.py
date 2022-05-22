# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import codecs


class DoubanBookPipeline(object):
    def __init__(self):
        self.filename = 'douban_book_top250.csv'
        with open(self.filename, 'wb') as f:
            f.write(codecs.BOM_UTF8)
        with open(self.filename, 'a', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f, dialect='excel')
            f_csv.writerow(
                ['书名', '作者', '评分', '评价', '评价人数', '出版日期', '单价', 'URL'])

    def process_item(self, item, spider):
        with open(self.filename, 'a', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f, dialect='excel')
            f_csv.writerow([item['bookname'], item['author'], item['rating_nums'], item['quote'],
                           item['comment_nums'], item['pubdate'], item['price'], item['url']])
        return item
