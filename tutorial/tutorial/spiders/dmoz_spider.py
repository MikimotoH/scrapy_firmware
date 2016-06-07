# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="cat-item"]/a/@href'):# "div.title-and-desc" "ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.css('div.site-item'):
            item = DmozItem()
            item['title'] = sel.css('div.site-title').xpath('text()').extract()[0].strip()
            item['link'] = sel.xpath('.//a/@href').extract()
            item['desc'] = sel.css('div.site-descr').xpath('text()').extract()[0].strip()
            yield item
