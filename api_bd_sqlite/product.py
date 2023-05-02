import connector

class Products:
    def __init__(self, name: str, description: str, weight: float , brand: str, supplier: str, price: float,  id = None):
        self.id = id
        self.name = name
        self.description = description
        self.weight = weight
        self.brand = brand
        self.supplier = supplier
        self.price = price

    def to_dictionary(self):
        



