# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MagicSpidersPipeline:
    def process_item(self, item, spider):
        title = item['title']
        actors = item['actors']
        show_time = item['show_time']
        content = item['content']

        output = f'|{title}|\t|{actors}|\t|{show_time}|\t|{content}|\n\n'
        with open('./maoyan_movie.txt', 'a+', encoding='utf-8') as f:
            f.write(output)

        return item
