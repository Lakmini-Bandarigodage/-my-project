def square(num):
    return num ** 2

from math_operations import MathOperations

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()

    calculator = MathOperations()
    result_addition = calculator.add(num1, num2)
    result_square = square(result_addition)

    print(f"The result of addition is: {result_addition}")
    print(f"The square of the result is: {result_square}")

