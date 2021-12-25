import scrapy


class Sp2Spider(scrapy.Spider):
    name = 'sp2'
    allowed_domains = ['spbeen.com']
    start_urls = ['http://spbeen.com/']

    def parse(self, response):
        pass
