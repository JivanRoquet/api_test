from application import db
from models.product import Product

db.drop_all()
db.create_all()

products = [
    {
        'name': 'Lavender heart',
        'price': '9.25',
    },
    {
        'name': 'Personalised cufflinks',
        'price': '45.00',
    },
    {
        'name': 'Kids T-shirt',
        'price': '19.95',
    },
]

for product in products:
    db.session.add(Product(**product))

db.session.commit()
