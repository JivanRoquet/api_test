from webargs import fields

from validators import validators

PATCH = {
    'name': fields.Str(location='form', missing=None),
    'price': fields.Str(location='form', missing=None, validate=validators.PRICE),
}

POST = {
    'name': fields.Str(required=True, location='form'),
    'price': fields.Str(required=True, location='form', validate=validators.PRICE),
}
