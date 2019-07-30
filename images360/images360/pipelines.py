# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        #开启数据库的连接，参数spider就是被开启的Spider对象
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]

    def process_item(self, item, spider):
        #返回item对象，此item会被低优先级的Item pipeline的方法调用，直道所有item全被调用完
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()



class Images360Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        url=request.url
        file_name=url.split('/')[-1]
        return file_name