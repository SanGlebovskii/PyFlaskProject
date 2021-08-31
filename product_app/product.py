from product_app import db


class Product(db.Model):
    id = db.Column('product_id', db.Integer,
                   primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer(50))
    amount = db.Column(db.String(200))


def __init__(self, name, city, address, pin):
    self.name = name
    self.city = city
    self.address = address
    self.pin = pin
