from operations import add, sub, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 1) == 4

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(0, 1) == 0

def test_divide():
    assert divide(4, 2) == 2