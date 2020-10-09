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

class SearchWordsSpider(scrapy.Spider):
    name = "search-words"
    start_urls = []

    def parse(self, response):
        # find all links with keyword in href
        for link in response.xpath('//a/@href').extract():
            if (self.keyword.upper() in link.upper()):
                self.output.append(link)

        # find all links with keyword in link text
        for link in response.xpath('//a[contains(.,"' + self.keyword + '")]/@href').extract():
            link_to_append = ""

            if (link.startswith("//")):
                link_to_append = link[2:]
            elif (link.startswith("/")):
                link_to_append = self.start_urls[0] + link
            else:
                link_to_append = link

            if (len(link_to_append) > 0 and link_to_append != link and link != "/"):
                self.output.append(link_to_append)

class GoogleSearchSpider(scrapy.Spider):
    name = "search-google"
    start_urls = []

    def parse(self, response):
        link_appendage = "/url?q="

        # find all google search link results
        for link in response.xpath('/html//a[contains(@href,"https")]/@href').extract():
            if (link.startswith(link_appendage)):
                self.output.append(link[len(link_appendage):])

        if ("&start=" not in self.start_urls[0]):
            yield scrapy.Request(
                response.urljoin(self.start_urls[0] + "&start=10"),
                callback=self.parse
            )
