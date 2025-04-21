import pytest

from src.category import Category
from src.product import Product
from src.iter_category import IterCategory
from src.lawngrass import LawnGrass
from src.smartfone import Smartphone
from src.order import Order


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

@pytest.fixture
def test_productiter(first_category):
    return IterCategory(first_category)

@pytest.fixture
def test_smartfone_1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def test_smartfone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def test_lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def test_lawngrass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

@pytest.fixture
def category_without_product():
    return Category(
        name="first category",
        description="first category is a first category",
        products=[]
    )

@pytest.fixture
def first_order():
    return Order(Product(name="first product", description="first product is a first product", price=3.0, quantity=10), 10)
