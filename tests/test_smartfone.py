import pytest

def test_smartfone_init(test_smartfone_1):
    assert test_smartfone_1.name == 'Samsung Galaxy S23 Ultra'
    assert test_smartfone_1.description == '256GB, Серый цвет, 200MP камера'
    assert test_smartfone_1.price == 180000
    assert test_smartfone_1.quantity == 5
    assert test_smartfone_1.efficiency == 95.5
    assert test_smartfone_1.model == 'S23 Ultra'
    assert test_smartfone_1.memory == 256
    assert test_smartfone_1.color == 'Серый'


def test_deadline_task_add(test_smartfone_1, test_smartfone_2):
    assert test_smartfone_1 + test_smartfone_2 == 2580000


def test_deadline_task_add_error(test_smartfone_1):
    with pytest.raises(TypeError):
        result = test_smartfone_1+ 1