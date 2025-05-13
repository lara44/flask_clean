from app.domain.product.repositories.product_repository import ProductRepository
from app.domain.product.entities.product import Product

class ProductRepositoryImpl(ProductRepository):
    def __init__(self):
        self._products = []

    def add(self, product: Product):
        self._products.append(product)

    def list_all(self) -> list[Product]:
        return self._products
