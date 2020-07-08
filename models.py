from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_name = "kzdelivery"
database_path = "postgres://postgres:password@{}/{}".format(
    'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


class Courier(db.Model):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    orders = db.relationship('Order', backref='couriers', lazy=True)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def format(self):
        return {
        'id': self.id,
        'name': self.name
        }


class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    orders = db.relationship('Order', backref='clients', lazy=True)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def format(self):
        return {
        'id': self.id,
        'name': self.name
        }


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    item = Column(String(180), nullable=False)
    from_address = Column(String, nullable=False)
    to_address = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    courier_id = Column(Integer, ForeignKey('couriers.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    def __init__(self, item, from_address, to_address, price):
        self.item = item
        self.from_address = from_address
        self.to_address = to_address
        self.price = price

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def format(self):
        return {
        'id': self.id,
        'item': self.item,
        'from_address': self.from_address,
        'to_address': self.to_address,
        'price': self.price
        }
