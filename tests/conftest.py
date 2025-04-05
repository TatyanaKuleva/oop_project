import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(name="first product", description="first product is a first product", price=3.0, quantity=10)


@pytest.fixture
def first_category():
    return Category(
        name="first category", description="first category is a first category", products=["First", "Second", "Third"]
    )
