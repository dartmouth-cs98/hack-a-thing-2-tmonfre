from flask import jsonify, request
from server import app
from server.src.services import google
from server.src.services.format_response import formatSuccess, formatError

@app.route('/elections/', methods=['GET'])
def get_election_info():
    data = google.get_election_info()
    return formatSuccess(data)

@app.route('/elections/voter-info', methods=['GET'])
def get_voter_info():
    address = request.args.get('address')
    electionId = request.args.get('electionId')

    data = google.get_voter_info(address, electionId)
    return formatSuccess(data)

@app.route('/elections/representative-info', methods=['GET'])
def get_representative_info():
    address = request.args.get('address')

    data = google.get_representative_info(address)
    return formatSuccess(data)