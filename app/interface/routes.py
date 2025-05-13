from flask import Blueprint, request, jsonify
from app.domain.product.entities.product import Product
from app.application.product.create_product import create_product
from app.application.product.lists_products import list_products
from app.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl

# Repositorio en memoria (podrías reemplazar por uno real después)
repository = ProductRepositoryImpl()

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/products', methods=['POST'])
def create():
    data = request.get_json()
    product = create_product(repository, data['id'], data['name'], data['price'])
    return jsonify(vars(product)), 201

@routes_bp.route('/products', methods=['GET'])
def get_all():
    products = list_products(repository)
    return jsonify([vars(p) for p in products]), 200

def register_routes(app):
    app.register_blueprint(routes_bp)
