## Submission for REST API test

### Setup

```shell
# clone the repository
git clone https://github.com/JivanRoquet/api_test api_test
cd api_test

# setup Python3 virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# seed the database
python db_seed.py

# launch the application
gunicorn application:app -b 127.0.0.1:5000
```

Any time the database needs to be restored to its initial seeded state, simply call `python db_seed.py`.
This command will erase everything and build a new seed from scratch.

### Tools used

- SQLite3 - file-based database engine - https://sqlite.org/
- SQLAlchemy - SQL ORM - http://www.sqlalchemy.org/
- Gunicorn - http server - http://gunicorn.org/
- Flask-Classful - resource-based views - http://flask-classful.teracy.org/
- Marshmallow - schema-based object serializer - https://marshmallow.readthedocs.io/
- Webargs - http request arguments parser - https://webargs.readthedocs.io/
- MyPy - static type checker - http://mypy-lang.org/

### Notes

Some liberties have been taken with the specs in order to be fully compliant to the REST standard:

- all `/product` routes have been changed to `/products` in order to have one single route for one single resource
- a trailing slash has been added to all ending roots except `GET`
- See following examples for the two rules above:
  - `POST /product` becomes `POST /products/`
  - `GET /product/3` becomes `GET /products/3`
  - `GET /products` stays the same
- `PUT` has been replaced by `PATCH` since the spec is to update one or more fields of an existing product,
  without replacing the product completely.
  This is a role dedicated to `PATCH`, whereas `PUT` is used to completely replace one product
  by another one, deleting the previous one
- Successful `POST` must return `201` (object created) and not `200`

All the modifications above have been ported into the `tests.postman` file provided in this repository.
