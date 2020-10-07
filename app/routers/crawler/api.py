"""Crawler routes."""

from flask import Blueprint, jsonify, request
from app.services import crawler
from app.services.format_response import formatSuccess, formatError

blueprint = Blueprint('/crawler', __name__, url_prefix='/crawler')

@blueprint.route('/content', methods=['GET'])
def content_crawler():
    url = request.args.get('url')
    data = crawler.crawl_content(url)
    return formatSuccess(data)

@blueprint.route('/links', methods=['GET'])
def link_crawler():
    url = request.args.get('url')
    data = crawler.crawl_links(url)
    return formatSuccess(data)
