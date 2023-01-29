from flask import jsonify
from .constants import JSON_CONTENT

def make_response(status_code, message, result):
    meta = {
        'code' : status_code,
        'message' : message
    }

    return jsonify({
        'meta' : meta,
        'result' : result
    }), 200, JSON_CONTENT