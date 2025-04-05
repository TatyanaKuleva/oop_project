from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product, excisting_list=None):
        name = dict_product['name']
        description = dict_product['description']
        quantity = dict_product['quantity']
        price = dict_product['price']
        if excisting_list is not None:
            for item in excisting_list:
                if name == item.name:
                    quantity += item.quantity
                    if price < item.price:
                        price = item.price
        return Product(name, description, price, quantity)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}, [product1])
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

