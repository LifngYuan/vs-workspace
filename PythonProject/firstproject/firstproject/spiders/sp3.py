import scrapy


class Sp3Spider(scrapy.Spider):
    name = 'sp3'
    allowed_domains = ['spbeen.com']
    start_urls = ['http://spbeen.com/']

    def parse(self, response):
        pass
