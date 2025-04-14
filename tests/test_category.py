import pytest


def test_category_init(first_category):
    assert first_category.name == "first category"
    assert first_category.description == "first category is a first category"
    assert first_category.products == ["First product, 3.0 руб. Остаток: 10 шт.", "Second product, 5.0 руб. Остаток: 20 шт."]
    assert first_category.category_count == 1
    assert first_category.product_count == 2

def test_list_product_property(first_category):
    assert first_category.products == ["First product, 3.0 руб. Остаток: 10 шт.", "Second product, 5.0 руб. Остаток: 20 шт."]

def test_list_product_setter(first_category, second_product):
    assert first_category.product_count == 2
    first_category.products = second_product
    assert first_category.product_count == 3

def test_product_iterator(test_productiter):
    iter(test_productiter)
    assert test_productiter.index == 0
    assert next(test_productiter) == 'First product, 3.0 руб. Остаток: 10 шт.'
    assert next(test_productiter) == 'Second product, 5.0 руб. Остаток: 20 шт.'

    with pytest.raises(StopIteration):
        next(test_productiter)


def test_category_str(first_category):
    assert str(first_category) == 'first category, количество продуктов: 30 шт.'

def test_category_setter_smartfone(first_category, test_smartfone_1):
    first_category.products = test_smartfone_1
    assert first_category.products[-1] == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'



