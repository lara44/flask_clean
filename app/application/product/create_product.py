from app.domain.product.entities.product import Product

def create_product(repository, id, name, price):
    product = Product(id = id, name = name, price = price)
    repository.add(product)
    return product
