import crochet
from scrapy.crawler import CrawlerRunner

from src.services.spiders import (
    FetchContentSpider, 
    FetchTextSpider, 
    DiscoverLinksSpider, 
    SearchWordsSpider, 
    GoogleSearchSpider,
    GoogleArticleTextSpider
)

crochet.setup()

output_data = []
crawl_runner = CrawlerRunner()

# get html content of page
def crawl_content(url):
    global output_data
    output_data = []
    init_base_crawler(url, FetchContentSpider)
    return list(dict.fromkeys(output_data))

# get text of page
def crawl_text(url):
    global output_data
    output_data = []
    init_base_crawler(url, FetchTextSpider)
    return list(dict.fromkeys(output_data))

# get links in page
def crawl_links(url):
    global output_data
    output_data = []
    init_base_crawler(url, DiscoverLinksSpider)
    return list(dict.fromkeys(output_data))

# get links with keyword in page
def crawl_keywords(url, keyword):
    global output_data
    output_data = []
    init_declared_crawler(lambda : crawl_runner.crawl(
        SearchWordsSpider, start_urls=[url], output=output_data, keyword=keyword
    ))
    return list(dict.fromkeys(output_data))

# get google search links from keyword
def crawl_google(keyword):
    global output_data
    output_data = []
    init_base_crawler("https://www.google.com/search?q=" + "+".join(keyword.split()), GoogleSearchSpider)
    return list(dict.fromkeys(output_data))

# get article text of google search results from keyword
def crawl_google_text(keyword):
    global output_data
    output_data = []
    init_base_crawler("https://www.google.com/search?q=" + "+".join(keyword.split()), GoogleArticleTextSpider)
    return output_data

## BOILERPLATE FOR RUNNING
@crochet.wait_for(timeout=60.0)
def init_base_crawler(url, spider, **kwargs):
    # begin base crawler
    eventual = crawl_runner.crawl(spider, start_urls=[url], output=output_data, **kwargs)
    return eventual

@crochet.wait_for(timeout=60.0)
def init_declared_crawler(get_crawler):
    # begin declared user crawler
    eventual = get_crawler()
    return eventual
