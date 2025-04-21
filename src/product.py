from itertools import product
from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        sum_product = self.__price * self.quantity + other.price * other.quantity
        return sum_product


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


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")








