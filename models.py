from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Product(db.Model,SerializerMixin):
    __tablename__='products'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer)
    category = db.Column(db.String(50),nullable = False)

    def __repr__(self):
        return f"<Product name: {self.name} price: {self.price} category: {self.category}>"