from mypy.types import names

from src.product import Product
from src.abstract_class import Abstract
from src.exceptions import ZeroPriceProduct


class Category(Abstract):
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self):
        count = 0
        for product in self.__products:
            count += product.quantity
        return f'{self.name}, количество продуктов: {count} шт.'


    def add_product(self, product):
        if isinstance(product, Product):
            try:
                if product.price == 0:
                    raise ZeroPriceProduct('Нельзя добавить товар с ценой равной нулю')
            except ZeroPriceProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Товар добавлен')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return product_list

    @products.setter
    def products(self, product:Product):
        self.__products.append(product)
        self.product_count +=1

    def middle_price(self):
        try:
            return round(sum(product.price for product in self.__products)/len(self.__products),2)
        except ZeroDivisionError:
            return 0

if __name__ == '__main__':

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])


    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 0, 7)
    category1.add_product(product4)












