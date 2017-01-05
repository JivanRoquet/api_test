from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.default")
db = SQLAlchemy(app)

from resources.products import ProductsView
from errors import errors
