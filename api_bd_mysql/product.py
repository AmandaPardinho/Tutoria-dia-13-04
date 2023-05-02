import mysql.connector

class Product:
    # Sets the product object
    def __init__(self, name: str, description: str, brand: str, price: float, id: None):
        self.id = id
        self.nome = name
        self.descricso = description
        self.marca = brand
        self.preco = price

    # Returns the values of the mentor object in dictionary format
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "brand": self.brand,
            "price": self.price
        }
    
    # Method creating a new product
    """def create_product(self, ):"""

