import scrapy


class Sp1Spider(scrapy.Spider):
    name = 'sp1'
    allowed_domains = ['spbeen.com']
    start_urls = ['http://spbeen.com/']

    def parse(self, response):
        pass
