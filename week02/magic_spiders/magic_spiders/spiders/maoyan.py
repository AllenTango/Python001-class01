# -*- coding: utf-8 -*-
import scrapy
from magic_spiders.items import MagicSpidersItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['m.maoyan.com']

    def start_requests(self):
        for i in range(0, 41, 10):
            url = f"https://m.maoyan.com/ajax/moreClassicList?sortId=1&showType=3&limit=10&offset={i}&optimus_uuid=3D5B1F90B48A11EAB726418169972B1D660DA419116B40DA8241C22175BD138A&optimus_risk_level=71&optimus_code=10"
            if i > 0:
                continue
            yield scrapy.Request(url=url, callback=self.prase)

    def prase(self, response):
        movies = Selector(response=response).xpath('//a')
        url = 'https://m.maoyan.com/asgard'
        for movie in movies:
            link = url + movie.xpath('./@href').get()
            yield scrapy.Request(url=link, callback=self.prase_detail)

    def prase_detail(self, response):
        item = MagicSpidersItem()
        item['title'] = Selector(response=response).xpath(
            '//div[@class="movie-cn-name"]/h1/text()').extract_first()
        item['types'] = Selector(response=response).xpath(
            '//span[@class="movie-cat"]/text()').extract_first()
        item['show_time'] = Selector(response=response).xpath(
            '//div[@class="movie-show-time"]/span/text()').extract_first()[:10]
        item['content'] = Selector(response=response).xpath(
            '//*[@id="brief-introduction-content"]/text()').extract_first()
        
        yield item
