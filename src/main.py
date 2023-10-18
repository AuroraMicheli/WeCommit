'''
Combining operations
'''
from operations import summation, subtraction, multiplication, division

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = summation(num1, num2)
    elif operation == "subtract":
        result = subtraction(num1, num2)
    elif operation == "multiply":  # Check for 'multiply' operation
        result = multiplication(num1, num2)
    elif operation == "divide":  # Check for 'divide' operation
        if num2 == 0:  # Handle division by zero
            raise ValueError("Division by zero is not allowed.")
        result = division(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.")

    return result
