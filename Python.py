def greet(age):
    return f"Hello, you are {age} years old!"

if __name__ == "__main__":
    user_age = input("Enter your age: ")
    greeting = greet(user_age)
    print(greeting)

