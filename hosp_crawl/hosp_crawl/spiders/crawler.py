# -*- coding: utf-8 -*-
import pandas as pd
import scrapy
import requests
from xml import etree
import time,random
from scrapy import Request,Item
from hosp_crawl.items import *
class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['db.yaozh.com']
    max_errors=5
    num-errors=0
    def start_requests(self):
        for i in range(83221,84880):
            start_urls = 'https://db.yaozh.com/hmap/{}.html'.format(str(i))
            print(start_urls)
            yield Request(start_urls,callback=self.parse,dont_filter=True)
            time.sleep(random.random() * 4)

    def parse(self, response):
        
        item = HospCrawlItem()
        if response.text is None:
            num_errors+=1
            if num_errors==max_errors:
                break
        else:
            table = response.xpath('//table[@class="table"]/tbody')[0]
            head = table.xpath('./tr/th/text()').extract()
            content = table.xpath('./tr/td')
            content = [''.join(i.xpath('.//text()').extract()).strip() for i in content]
            a = dict(zip(head, content))
            d = {
                'hosp_name':'医院名称',
                'hosp_alias': '医院别名',
                'hospital_level': '医院等级',
                'hosp_type':'医院类型',
                'founded_date':'建院年份',
                'operation_way':'经营方式',
                'website':'医院网址',
                'phone':'电话',
                'pr':'省',
                'city':'市',
                'addr_detail':'医院地址'
            }
            for en, zh in d.items():
                if zh in a:
                    item[en] = a[zh]
            num_errors=0
        return item



