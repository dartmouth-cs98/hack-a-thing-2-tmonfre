from flask import jsonify, request
from src import app
from src.services import crawler
from src.services.format_response import formatSuccess, formatError

@app.route('/crawler/content/', methods=['GET'])
def content_crawler():
    url = request.args.get('url')
    data = crawler.crawl_content(url)
    return formatSuccess(data)

@app.route('/crawler/links/', methods=['GET'])
def link_crawler():
    url = request.args.get('url')
    data = crawler.crawl_links(url)
    return formatSuccess(data)

@app.route('/crawler/keyword/', methods=['GET'])
def keyword_crawler():
    url = request.args.get('url')
    keyword = request.args.get('keyword')
    data = crawler.crawl_keywords(url, keyword)
    return formatSuccess(data)

@app.route('/crawler/google/', methods=['GET'])
def google_crawler():
    keyword = request.args.get('keyword')
    data = crawler.crawl_google(keyword)
    return formatSuccess(data)
