def test_category_init(first_category):
    assert first_category.name == "first category"
    assert first_category.description == "first category is a first category"
    assert first_category.products == ["First", "Second", "Third"]
    assert first_category.category_count == 1
    assert first_category.product_count == 3
