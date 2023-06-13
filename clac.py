def add(x, y):
    """"Add Function"""
    return x + y


def subtract(x, y):
    """"Subtract Function"""
    return x - y


def multiply(x, y):
    """"Multiply Function"""
    return x * y


def divide(x, y):
    """"Divide Function"""
    if y == 0:
        raise ValueError('Cant divide by zero !')
    if type(y) != int:
        raise TypeError('Only get integer!')
    if type(x) != int:
        raise TypeError('Only get integer!')
    return x // y
