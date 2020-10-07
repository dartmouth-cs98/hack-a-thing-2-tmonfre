from flask import jsonify, request
from server import app
from server.src.services import crawler
from server.src.services.format_response import formatSuccess, formatError

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
