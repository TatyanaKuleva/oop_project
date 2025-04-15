from pyexpat.errors import messages

from src.product import Product
from src.smartfone import Smartphone
from src.lawngrass import LawnGrass

def test_print_mixin(capsys):
    Product(name="first product", description="first product is a first product", price=3.0, quantity=10)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(first product, first product is a first product, 3.0, 10)'

    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
               "S23 Ultra", 256, "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)'
