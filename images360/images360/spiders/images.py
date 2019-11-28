# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Spider,Request
import json
from ..items import Images360Item
MAX_PAGE=50

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data={
            'ch': 'photography',
            'listtype': 'new',
            'temp': '1',
        }
        base_url='https://image.so.com/zj?'
        for page in range(1,MAX_PAGE+1):
            data['sn']=page*30
            params=urlencode(data)
            url=base_url+params
            yield Request(url,self.parse)
    def parse(self, response):
        result=json.loads(response.text)
        print(type(result))
        for image in result.get('list'):
            print(type(image))
            item=Images360Item()
            item['id']=image.get('id')
            item['url']=image.get('purl')
            item['title']=image.get('group_title')
            item['thumb']=image.get('qhimg_url')
            yield item
            
            
 优化parse():
    
    def parse(self, response):
            results = json.loads(response.text)
            # 判断list是否在results的keys中
            if 'list' in results.keys():
                images = results.get('list')

            # 每张图片动态赋值并生产ImageItem
            for image in images:
                item = ImageItem()
                for field in item.fields:
                    if field in image.keys():
                        item[field] = image.get(field)
                yield item
