def test_product_init(first_product):
    assert first_product.name == "first product"
    assert first_product.description == "first product is a first product"
    assert first_product.price == 3.0
    assert first_product.quantity == 10
