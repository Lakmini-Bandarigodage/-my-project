def custom_operation(num1, num2, operation_type):
    if operation_type == 'add':
        result = num1 + num2
    elif operation_type == 'subtract':
        result = num1 - num2
    elif operation_type == 'multiply':
        result = num1 * num2
    elif operation_type == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!!!!"
    else:
        result = "Invalid operation type!"

    return result


