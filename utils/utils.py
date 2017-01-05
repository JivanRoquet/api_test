import json
from typing import TypeVar, List, Dict

from flask import make_response

Data = TypeVar('Data', Dict, List[Dict])


def api_response(data: Data, code: int, headers: dict=None):
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
