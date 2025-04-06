from src.product import Product

def test_product_init(first_product):
    assert first_product.name == "first product"
    assert first_product.description == "first product is a first product"
    assert first_product.price == 3.0
    assert first_product.quantity == 10

def test_new_product_create():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 10

def price_update(capsys, first_product):
    first_product.price = 0
    message = capsys.readouterr()
    assert  message.out.strip() == 'Цена не должна быть нулевая или отрицательная'


