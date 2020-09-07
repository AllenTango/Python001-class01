# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from datetime import datetime
from .config import localhost, user, pwd, db


class ZdmSpidersMySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = localhost,
            db = db,
            user = user,
            password = pwd,
            charset = 'utf8mb4'
        )
        self.cursor = self.connect.cursor()
    
    def process_item(self, item, spider):
        try:
            create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("INSERT INTO product(product_name, user_name, user_comment, create_time) VALUES (%s, %s, %s, %s)", (item['product_name'], item['user_name'], item['user_comment'], create_time))
            self.connect.commit()
        except Exception as e:
            print(e)
        
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()