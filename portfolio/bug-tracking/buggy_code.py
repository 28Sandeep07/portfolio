# buggy_code.py

def divide(a, b):
    return a / b  # Bug: No handling for division by zero

def test_divide():
    assert divide(10, 2) == 5
    # This will cause an error
    assert divide(10, 0) == "undefined"
