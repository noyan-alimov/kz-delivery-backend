from sqlalchemy import Column, String, Integer, create_engine
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


class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
