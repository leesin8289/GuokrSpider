# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class GuokrPipeline(object):

    def open_spider(self, spider):
        self.f = open('guokr.csv','w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item))
        self.f.write(content + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()