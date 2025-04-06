import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(name="first product", description="first product is a first product", price=3.0, quantity=10)

@pytest.fixture
def second_product():
    return Product("second product", "second product is second product", 5, 20)



@pytest.fixture
def first_category():
    return Category(
        name="first category",
        description="first category is a first category",
        products=[Product('First product', 'first product is a first product', 3.0, 10),
                  Product('Second product', 'second product is a second product', 5.0, 20)
    ]
    )


@pytest.fixture
def dict_product():
    dict_product = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}
    return dict_product

