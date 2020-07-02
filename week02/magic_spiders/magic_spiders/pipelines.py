# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

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
