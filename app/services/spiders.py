import scrapy

class FetchContentSpider(scrapy.Spider):
    name = "fetch-content"
    start_urls = []

    def parse(self, response):
        self.output.append(response.text)

class DiscoverLinksSpider(scrapy.Spider):
    name = "discover-links"
    start_urls = []

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            self.output.append(link)
