import crochet
from scrapy.crawler import CrawlerRunner

from server.src.services.spiders import FetchContentSpider, DiscoverLinksSpider

crochet.setup()

output_data = []
crawl_runner = CrawlerRunner()

# get html content of page
def crawl_content(url):
    init_crawler(url, FetchContentSpider)
    return output_data

# get links in page
def crawl_links(url):
    init_crawler(url, DiscoverLinksSpider)
    return output_data


## BOILERPLATE FOR RUNNING
@crochet.wait_for(timeout=60.0)
def init_crawler(url, spider):
    eventual = crawl_runner.crawl(spider, start_urls=[url], output=output_data)
    return eventual  # returns a twisted.internet.defer.Deferred
