"""Election data routes."""

from flask import Blueprint, jsonify, request
from app.services import google
from app.services.format_response import formatSuccess, formatError

blueprint = Blueprint('/', __name__, url_prefix='/elections')

@blueprint.route('/', methods=['GET'])
def get_election_info():
    data = google.getElectionInfo()
    return formatSuccess(data)

@blueprint.route('/voter-info', methods=['GET'])
def get_voter_info():
    address = request.args.get('address')
    electionId = request.args.get('electionId')

    data = google.getVoterInfo(address, electionId)
    return formatSuccess(data)

@blueprint.route('/representative-info', methods=['GET'])
def get_representative_info():
    address = request.args.get('address')

    data = google.getRepresentativeInfo(address)
    return formatSuccess(data)