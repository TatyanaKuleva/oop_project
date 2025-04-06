from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_answer = input('Подтвердите понижение цены: "y" или "n" ')
            if user_answer == 'y':
                self.__price = new_price






