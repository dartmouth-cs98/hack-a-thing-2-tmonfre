import scrapy

# returns html content of page
class FetchContentSpider(scrapy.Spider):
    name = "fetch-content"
    start_urls = []

    def parse(self, response):
        self.output.append(response.text)

# returns all text on page
class FetchTextSpider(scrapy.Spider):
    name = "fetch-text"
    start_urls = []

    def parse(self, response):
        text = ''.join(response.xpath("//*[not(self::script or self::style)]/text()").extract()).strip()
        self.output.append(text)

# returns all links on the given page
class DiscoverLinksSpider(scrapy.Spider):
    name = "discover-links"
    start_urls = []

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            self.output.append(link)

# returns links on page with keyword in them
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

# returns urls of search results from google search
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

# finds all links on provided page, then grabs text results of each page
class GoogleArticleTextSpider(scrapy.Spider):
    name = "search-google-text"
    start_urls = []

    def parse_text(self, response):
        text = ''.join(response.xpath("//*[not(self::script or self::style)]/text()").extract()).strip()
        self.output.append({
            "url": response.url,
            "text": text
        })

    def parse(self, response):
        urls_to_query = []
        link_appendage = "/url?q="

        # find all google search link results and get content
        for link in response.xpath('/html//a[contains(@href,"https")]/@href').extract():
            if (link.startswith(link_appendage)):
                urls_to_query.append(link[len(link_appendage):])

        # fetch text content of each url
        for new_link in list(dict.fromkeys(urls_to_query)):
            yield scrapy.Request(
                response.urljoin(new_link),
                callback=self.parse_text
            )
