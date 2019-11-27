# -*- coding: utf-8 -*-
#https://blog.csdn.net/qq_23518237/article/details/80722168
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import pandas as pd

class HospCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    collection = table = 'hosp_crawl'
    hosp_name=scrapy.Field()
    hosp_alias=scrapy.Field()
    hosp_type=scrapy.Field()
    hospital_level = scrapy.Field()
    founded_date=scrapy.Field()
    operation_way=scrapy.Field()
    website = scrapy.Field()
    phone = scrapy.Field()
    pr = scrapy.Field()
    city = scrapy.Field()
    addr_detail = scrapy.Field()
