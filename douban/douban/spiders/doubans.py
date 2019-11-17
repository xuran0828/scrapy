# -*- coding: utf-8 -*-
import scrapy
import time
import json
from scrapy import Request
from douban.items import *
from urllib.parse import urlencode

PAGE_COUNT=1000

class DoubanSpider(scrapy.Spider):
    name = 'doubans'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        time.sleep(1)
        start_urls = 'http://movie.douban.com/j/search_subjects?'
        data={
            'type':'movie',
            'tag':'%E7%83%AD%E9%97%A8',
            'sort':'recommend',
            'page_limit':20,
        }
        for page in range(1,PAGE_COUNT):
            data['page_start']=page*20
            params=urlencode(data)
            url=start_urls+params
            yield Request(url, callback=self.parse, dont_filter=True)
    def parse(self, response):
        data_list = json.loads(response.text)
        item=DoubanItem()
        for data in data_list[u'subjects']:
            item['title'] = data[u"title"]  # 这里获取标题
            item['rate'] = data[u"rate"]  # 这里获取评分
            # scrapy.Request(url=data[u'url'], callback=self.text_parse)
            # items['simple_text'] =
            item['type'] = self.movie_type
            yield item
