from flask_restful import Resource
from flask import request,jsonify
from models import Product,db

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([
            product.to_dict() for product in products
        ])
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ("name","price","category")):
            return {"error": "Missing required fields"},400
        new_product = Product(
            **data
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict(),201
    
class ProductResource(Resource):
    def get(self,id):
        product = Product.query.get(id)
        if not product:
            return {"message": "Product not found"},404
        return product.to_dict(),200
    def patch(self,id):
        data = request.get_json()
        product = Product.query.get(id)

        if not product:
            return {"error": "Product you are trying to update is not found"},404
        if "name" in data:
            product.name = data['name']
        if "price" in data:
            product.price = data['price']
        if "category" in data:
            product.category = data['category']
        db.session.commit()
        return product.to_dict(),200
    def delete(self,id):
        product = Product.query.get(id)
        if not product:
            return {"error": "Product you are trying to delete does not exist"},404
        db.session.delete(product)
        db.session.commit()
        return {"message":"Product deleted successfully"},200