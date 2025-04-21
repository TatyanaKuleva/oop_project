import pytest
from pyexpat.errors import messages

from src.product import Product
from src.order import Order


def test_custom_exception_order(capsys, first_order):

    product_add = Product(name="first product", description="first product is a first product", price=3.0, quantity=10)
    first_order.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'
    assert message.out.strip().split('\n')[-2] == 'Товар добавлен'

    product_add = Product(name="first product", description="first product is a first product", price=0, quantity=10)
    first_order.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'
    assert message.out.strip().split('\n')[-2] == 'Нельзя добавить товар с ценой равной нулю'