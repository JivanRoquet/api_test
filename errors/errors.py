from flask import jsonify
from application import app


@app.errorhandler(422)
def handle_unprocessable_entity(err):
    return jsonify({
        'status': 'error',
        'errors': err.data
    }), 422


@app.errorhandler(400)
def handle_bad_request(err):
    return jsonify({
        'status': 'error',
        'errors': err.data
    }), 400
