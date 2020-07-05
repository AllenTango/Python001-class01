# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from config import localhost, user, pwd, db
from scrapy.exporters import CsvItemExporter


class MagicSpidersPipeline:
    def process_item(self, item, spider):
        fields_to_export = ['title',
                            'types',
                            'show_time',
                            'content']
        with open("./maoyan_movies.csv", "a+b") as f:
            exporter = CsvItemExporter(
                f, include_headers_line=False, fields_to_export=fields_to_export)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()

        return item

class MagicSpidersMySQLPipeline(object):
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
            self.cursor.execute("INSERT INTO movie(title, types, show_time) VALUES (%s, %s, %s)", (item['title'], item['types'], item['show_time']))
            self.connect.commit()
        except Exception as e:
            print(e)
        
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()