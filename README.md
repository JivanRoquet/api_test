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

### Notes

Some liberties have been taken with the specs in order to be fully compliant to the REST standard:

- all `/product` routes have been changed to `/products` in order to have one single route for one single resource
- a trailing slash has been added to all ending roots except `GET`
- See following examples for the two rules above:
  - `POST /product` becomes `POST /products/`
  - `GET /product/3` becomes `GET /products/3`
  - `GET /products` stays the same
- `PUT` has been replaced by `PATCH` since the spec is to update one or more fields of a product,
  which is the role dedicated to `PATCH`, whereas `PUT` is used to completely replace one product
  by another one, deleting the previous one
- Successful `POST` and `PATCH` must return `201` and not `200`

All the modifications above have been ported into the `tests.postman` file provided in this repository.
