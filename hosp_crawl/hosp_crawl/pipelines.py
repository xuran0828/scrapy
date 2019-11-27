# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from sqlalchemy import create_engine
class MySQLPipeline(object):
    def __init__(self,host,port,db,user,passwd):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            db=crawler.settings.get('MYSQL_DB_NAME'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWORD')
        )
    def open_spider(self,spider):
        self.db_conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user,
                                       passwd=self.passwd,
                                       charset='utf8')
        self.db_conn.ping(reconnect=True)
        self.db_cur = self.db_conn.cursor()
        print("数据库连接成功")
    def process_item(self, item, spider):
        values=(
            item['hosp_name'],
            item.get('hosp_alias'),
            item['hosp_type'],
            item['hospital_level'],
            item.get('founded_date'),
            item['operation_way'],
            item.get('website'),
            item['phone'],
            item['pr'],
            item['city'],
            item['addr_detail']
        )
        try:
            self.db_cur.execute("""select * from hosp_rawinfos where hosp_name=%s""",item['hosp_name'])
            sql="""insert into hosp_rawinfos(hosp_name,hosp_alias,hosp_type,hospital_level,founded_date,operation_way,website,phone ,pr,city ,addr_detail)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            print(values)
            self.db_cur.execute(sql,values)
            self.db_conn.commit()
            print("insert finished")
        except:
            print("insert to db failed")
            self.db_conn.rollback()
            self.db_conn.close()
        return item
    def close_spider(self,spider):
        self.db_conn.close()
