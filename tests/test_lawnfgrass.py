import pytest

def test_lawngrass_init(test_lawngrass_1):
    assert test_lawngrass_1.name == 'Газонная трава'
    assert test_lawngrass_1.description == 'Элитная трава для газона'
    assert test_lawngrass_1.price == 500
    assert test_lawngrass_1.quantity == 20
    assert test_lawngrass_1.country == 'Россия'
    assert test_lawngrass_1.germination_period == '7 дней'
    assert test_lawngrass_1.color == 'Зеленый'


def test_deadline_task_add(test_lawngrass_1, test_lawngrass_2):
    assert test_lawngrass_1 + test_lawngrass_2 == 16750


def test_deadline_task_add_error(test_lawngrass_1):
    with pytest.raises(TypeError):
        result = test_lawngrass_1+ 1