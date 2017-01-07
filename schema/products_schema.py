from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    price = fields.Str()


def schema_dump(product):
    return ProductSchema().dump(product).data
