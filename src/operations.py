'''
Arithmetic operations
'''

def summation(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")

def multiplication(a, b):
    return a ** b # there is a bug here
