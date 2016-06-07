# -*- coding: utf-8 -*-
import scrapy


class ExamplecomSpider(scrapy.Spider):
    name = "examplecom"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
        'http://www.example.org/',
        'http://www.example.net/',
    )

    def parse(self, response):
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)
