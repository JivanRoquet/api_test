import json
from typing import Dict

from flask import make_response

def api_response(data: str, code: int, headers: dict=None):
    """
    Marshalls a view method response to JSON format and Content-Type
    """
    content_type = 'application/vnd.api+json'
    payload = json.dumps(data)
    if headers:
        headers.update({'Content-Type': content_type})
    else:
        headers = {'Content-Type': content_type}
    return make_response(payload, code, headers)
