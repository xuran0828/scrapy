# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义两个属性collection和table，都为imgaes
    collection=table='images'
    id=Field()
    url=Field()
    title=Field()
    thumb=Field()


