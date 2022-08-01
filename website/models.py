from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class FavStocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    current_stock = db.Column(db.String(10))
    last_login = db.Column(db.DateTime(timezone=True), default=func.now())
    tickers = db.relationship('FavStocks')
    user_salt = db.Column(db.String(250))
