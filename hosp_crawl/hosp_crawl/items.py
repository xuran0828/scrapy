# -*- coding: utf-8 -*-

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
    # name_mapper['hospital_level']=scrapy.Field()

