import math

def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

if __name__ == "__main__":
    try:
        user_number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    square_result, cube_result = calculate_square_and_cube(user_number)
    print(f"The square of {user_number} is: {square_result}")
    print(f"The cube of {user_number} is: {cube_result}")
