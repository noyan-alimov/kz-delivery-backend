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


class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    orders = db.relationship('Order', backref='clients', lazy=True)


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    item = Column(String(180), nullable=False)
    from_address = Column(String, nullable=False)
    to_address = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    courier_id = Column(Integer, ForeignKey('couriers.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
