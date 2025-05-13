from abc import ABC, abstractmethod
from app.domain.product.entities.product import Product
from typing import List

class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass
