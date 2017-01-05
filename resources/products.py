from flask_classful import FlaskView, route
from webargs.flaskparser import use_args, use_kwargs
from typing import Tuple, List, Dict

from application import app, db
from models.product import Product as ProductModel
from utils import utils
from args import products_args
from schema.products_schema import ProductSchema


class ProductsView(FlaskView):
    """
    Product REST Resource
    See http://flask-classful.teracy.org
    """
    representations = {'application/json': utils.api_response}

    @route('/', methods=['GET'])
    def index(self) -> Tuple[List[Dict], int]:
        """ Lists all products """
        products = ProductModel.query.all()
        data = [ProductSchema().dump(product).data for product in products]
        return data, 200


    @route('/<id>', methods=['GET'])
    def get(self, id: str) -> Tuple[Dict, int]:
        """ Gets a particular product """
        product = ProductModel.query.get(id)

        if product is not None:
            data = ProductSchema().dump(product).data
            return data, 200

        else:
            # product not found
            return {'error': 'NotFound'}, 404


    @route('/', methods=['POST'])
    @use_kwargs(products_args.POST)
    def post(self, name: str, price: str) -> Tuple[Dict, int]:
        """ Creates a new product """
        product = ProductModel(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        return {'success': 'created {}'.format(product.id)}, 201


    @route('/<id>', methods=['PATCH'])
    @use_kwargs(products_args.PATCH)
    def patch(self, id: str, **kwargs) -> Tuple[Dict, int]:
        """ Updates one or more fields of a particular product """
        product = ProductModel.query.get(id)

        if product is not None:

            # product.name
            if kwargs['name'] is not None:
                product.name = kwargs['name']

            # product.price
            if kwargs['price'] is not None:
                product.name = kwargs['price']

            db.session.commit()
            return {'success': 'updated {}'.format(product.id)}, 200

        else:
            # product not found
            return {'error': 'NotFound'}, 404


    @route('/<id>', methods=['DELETE'])
    def delete(self, id) -> Tuple[Dict, int]:
        """ Deletes a particular product """
        product = ProductModel.query.get(id)

        if product is not None:
            db.session.delete(product)
            db.session.commit()
            return {'success': 'deleted {}'.format(product.id)}, 201

        else:
            # product not found
            return {'error': 'NotFound'}, 404


ProductsView.register(app, route_base='/v1/products/')
