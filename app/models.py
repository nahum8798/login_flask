from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

"""
Users models
"""
class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

"""
Products models
"""

class Product(db.Model):

    __tablename__ = 'product'

    id_product = db.Column(db.Integer, primary_key = True)
    name_product = db.Column(db.String(100), nullable=True)
    price_product = db.Column(db.Integer, nullable=True)
    stock_product = db.Column(db.Integer, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='product')
