def square(num):
    return num ** 2

from math_operations import MathOperations

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number for addition: "))
        num2 = float(input("Enter the second number for addition: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()

    calculator = MathOperations()
    result_addition = calculator.add(num1, num2)
    result_square = square(result_addition)

    print(f"The result of adding {num1} and {num2} is: {result_addition}")
    print(f"The square of the result is: {result_square}")
