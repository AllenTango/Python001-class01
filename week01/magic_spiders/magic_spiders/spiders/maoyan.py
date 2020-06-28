# -*- coding: utf-8 -*-
import scrapy
from magic_spiders.items import MagicSpidersItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['m.maoyan.com']
    start_urls = ['https://m.maoyan.com/?showType=3#movie/classic']

    def start_requests(self):
        for i in range(0, 41, 10):
            url = f"https://m.maoyan.com/ajax/moreClassicList?sortId=1&showType=3&limit=10&offset={i}&optimus_uuid=3D5B1F90B48A11EAB726418169972B1D660DA419116B40DA8241C22175BD138A&optimus_risk_level=71&optimus_code=10"
            if i > 0:
                continue
            yield scrapy.Request(url=url, callback=self.prase)

        # yield scrapy.Request(url='https://m.maoyan.com/asgard/movie/343355', callback=self.prase_detail)

    def prase(self, response):
        # print(response.text)
        movies = Selector(response=response).xpath('//a')
        url = 'https://m.maoyan.com/asgard'
        for movie in movies:
            link = url + movie.xpath('./@href').get()

            # title = movie.css('div.title::text').extract_first()
            # actors = movie.css('div.actors::text').extract_first()
            # show_time = movie.css('div.show-info::text').extract_first()

            yield scrapy.Request(url=link, callback=self.prase_detail)

    def prase_detail(self, response):
        # title = Selector(response=response).xpath(
        #     '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/h1/text()').extract_first()

        yield {'title': Selector(response=response).xpath('//div[@class="movie-cn-name"]/h1/text()').extract_first(),
               'types': Selector(response=response).xpath('//span[@class="movie-cat"]/text()').extract_first(),
               'show_time': Selector(response=response).xpath('//div[@class="movie-show-time"]/span/text()').extract_first()[:10],
               'content': Selector(response=response).xpath('//*[@id="brief-introduction-content"]/text()').extract_first()}
