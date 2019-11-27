# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class MongoPipeline(object):
    def __init__(self,host,db,port,user,passwd):
        self.host=host
        self.db=db
        self.port=port
        self.user=user
        self.passwd=passwd


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DB'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWD')
        )
    def open_spider(self,spider):
        #开启数据库的连接，参数spider就是被开启的Spider对象
            try:
                self.conn=pymysql.connect(
                    host=self.host,db=self.db,port=self.port,user=self.user,passwd=self.passwd,charset='utf8'
                )
                self.db_cor=self.conn.cursor()
                print("数据库连接成功")
            except:
                print("数据库连接失败")

    def process_item(self, item, spider):
        #返回item对象，此item会被低优先级的Item pipeline的方法调用，直道所有item全被调用完
        values=(
            item['title'],
            item['rate'],
            item['type']
        )
        sql="""insert into article(title,rate,type) values (%s,%s,%s)"""
        try:
            self.db_cor.execute(sql,values)
            self.conn.commit()
            self.conn.close()
            print("insert into finished")
        except:
            self.conn.rollback()
            self.conn.close()
            print("insert into failed")
        return item

    def close_spider(self,spider):
        self.client.close()
