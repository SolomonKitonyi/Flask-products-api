import os
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from models import db
from resources.product import ProductListResource,ProductResource
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql://postgres@localhost:5432/products_db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
migrate = Migrate(app,db)
api = Api(app)

api.add_resource(ProductListResource,'/products')
api.add_resource(ProductResource,'/products/<int:id>')
@app.route("/")
def home():
    return "<h1>Welcome to Products Page</h1>"
    
# @app.route("/products",methods=["GET"])
# def get_products():
#     products = Product.query.all()
#     return jsonify([
#         product.to_dict() for product in products
#     ])

# @app.route("/products/<int:id>",methods=["GET"])
# def get_one(id):
#     product = Product.query.get(id)
#     if not product:
#         return jsonify({"message": "Product not found"}),404
#     return jsonify(product.to_dict()),200

# @app.route("/products",methods=["POST"])
# def add_product():
#     data = request.get_json()
#     if not data or not all(key in data for key in ("name","price","category")):
#         return jsonify({"error": "Missing required fields"}),400
#     new_product = Product(
#         **data
#     )
#     db.session.add(new_product)
#     db.session.commit()
#     return jsonify(new_product.to_dict()),201

# @app.route("/products/<int:product_id>",methods=["PATCH","PUT"])
# def update_product(product_id):
#     data = request.get_json()
#     product = Product.query.get(product_id)

#     if not product:
#         return jsonify({"error": "Product you are trying to update is not found"}),404
#     if "name" in data:
#         product.name = data['name']
#     if "price" in data:
#         product.price = data['price']
#     if "category" in data:
#         product.category = data['category']
#     db.session.commit()
#     return jsonify(product.to_dict()),200
# @app.route("/products/<int:id>",methods=["DELETE"])
# def delete_product(id):
#     product = Product.query.get(id)
#     if not product:
#         return jsonify({"error": "Product you are trying to delete does not exist"}),404
#     db.session.delete(product)
#     db.session.commit()
#     return jsonify({"message":"Product deleted successfully"}),200

if __name__ == "__main__":
    app.run(debug=True)