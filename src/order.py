from src.product import Product
from src.abstract_class import Abstract
from src.exceptions import ZeroPriceProduct

class Order(Abstract):

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def add_product(self, product):
        if isinstance(product, Product):
            try:
                if product.price ==0:
                    raise ZeroPriceProduct('Нельзя добавить товар с ценой равной нулю')
            except ZeroPriceProduct as e:
                print(str(e))
            else:
                self.product = product
                print('Товар добавлен')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError


    def __str__(self):
        total_cost_order = self.quantity * self.product.price
        return f'в этом заказе:{self.product.name}, в кол-ве {self.quantity}, общая стоимость заказа: {total_cost_order}'



if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    ord_1 = Order(product1, 10)
    print(ord_1)

    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0, 5)

    ord_1.add_product(product2)
    print(ord_1)





