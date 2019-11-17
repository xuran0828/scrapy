# -*- coding: utf-8 -*-
import pandas as pd
import scrapy
import requests
from xml import etree
from scrapy import Request,Item
from hosp_crawl.items import *
class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['db.yaozh.com']


    def start_requests(self):
        for i in range(83221,84880):
            start_urls = 'https://db.yaozh.com/hmap/{}.html'.format(str(i))
            print(start_urls)

        yield Request(start_urls,callback=self.parse,dont_filter=True)

    def parse(self, response):
        items = response.xpath('//html/body/div[5]/div[2]')

        table = items.xpath('//table[@class="table"]/tbody')[0]
        head = table.xpath('./tr/th/text()')
        content = table.xpath('./tr/td')
        content = [''.join(str(i.xpath('.//text()')).strip()) for i in content]

        return dict(zip(head, content))

        item=HospCrawlItem()
        df=pd.DataFrame(item)
        info=df[['医院名称','医院别名','医院等级']]
        print(info)

        mapper_name={
            '医院名称':'hosp_name',
            '医院别名':'hosp_alias',
            '医院类型':'hosp_type'
        }
        df.columns=[mapper_name[i] for i in df.columns]

        df.to_csv('hosp.csv')