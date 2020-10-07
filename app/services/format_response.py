"""Response formatter."""

from flask import jsonify

def formatSuccess(payload = {}):
    return jsonify({
        "code": 200,
        "message": "SUCCESS",
        "data": payload
    })

def formatError(error = {}, message = ""):
    return jsonify({
        "code": 500,
        "message": message if len(message) > 0 else "ERROR",
        "error": error
    })