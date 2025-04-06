from src.category import Category


def test_category_init(first_category):
    assert first_category.name == "first category"
    assert first_category.description == "first category is a first category"
    assert first_category.products == ("First product, 3.0руб. Остаток: 10 шт.\n" "Second product, 5.0руб. Остаток: 20 шт.\n")
    assert first_category.category_count == 1
    assert first_category.product_count == 2

def test_list_product_property(first_category):
    assert first_category.products == ("First product, 3.0руб. Остаток: 10 шт.\n" "Second product, 5.0руб. Остаток: 20 шт.\n")

def test_list_product_setter(first_category, second_product):
    assert first_category.product_count == 2
    first_category.products = second_product
    assert first_category.product_count == 3



