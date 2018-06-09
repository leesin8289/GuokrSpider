# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule
from Guokr.items import GuokrItem

class GuokrSpider(CrawlSpider):

    name = 'guokr'

    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']
    rules = [
            Rule(LinkExtractor(allow=r'/ask/highlight/'), follow=True),
            Rule(LinkExtractor(allow=r'www\.guokr\.com/question/\d+'),callback='parse_page', follow=False),
            # Rule(LinkExtractor(allow=r'/ask/highlight/'), callback='parse_page',follow=False)
            ]

    def parse_page(self, response):
            item = GuokrItem()
            item['title'] = response.xpath('//*[@id="articleTitle"]/text()').extract_first()

            print "===========",response.xpath('//*[@id="articleTitle"]/text()').extract_first()
            item['detail'] = '\n'.join(response.xpath('//*[@id="questionDesc"]/p/text()').extract())
            print "-----------", '\n'.join(response.xpath('//*[@id="questionDesc"]/p/text()').extract())
            yield item
