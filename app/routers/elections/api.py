"""Election data routes."""

from flask import Blueprint, jsonify, request
from app.services import google
from app.services.format_response import formatSuccess, formatError

blueprint = Blueprint('/elections', __name__, url_prefix='/elections')

@blueprint.route('/', methods=['GET'])
def get_election_info():
    data = google.get_election_info()
    return formatSuccess(data)

@blueprint.route('/voter-info', methods=['GET'])
def get_voter_info():
    address = request.args.get('address')
    electionId = request.args.get('electionId')

    data = google.get_voter_info(address, electionId)
    return formatSuccess(data)

@blueprint.route('/representative-info', methods=['GET'])
def get_representative_info():
    address = request.args.get('address')

    data = google.get_representative_info(address)
    return formatSuccess(data)