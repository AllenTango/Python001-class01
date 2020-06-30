# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter


class MagicSpidersPipeline:
    def process_item(self, item, spider):
        title = item['title']
        types = item['types']
        show_time = item['show_time']
        content = item['content']

        # output = f'|{title}|\t|{actors}|\t|{show_time}|\t|{content}|\n\n'
        # with open('./maoyan_movie.txt', 'a+', encoding='utf-8') as f:
        #     f.write(output)
        with open("./maoyan_movies.csv", "a+b") as f:
            exporter = CsvItemExporter(f, include_headers_line=False)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()

        return item
