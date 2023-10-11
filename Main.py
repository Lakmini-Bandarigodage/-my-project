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

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation_type = input("Enter the operation type (add, subtract, multiply, divide): ").lower()
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()

    operation_result = custom_operation(num1, num2, operation_type)
    print(f"The result of the custom operation is: {operation_result}")
