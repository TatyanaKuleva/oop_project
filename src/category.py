from mypy.types import names

from src.product import Product

class Category:
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
            self.__products.append(product)
            Category.product_count += 1
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











