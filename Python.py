def greet(name, age):
    if age>0:
        if age >= 18:
            return f"Hello, {name}! Welcome to the adult club!!"
        else:
            return f"Hello, {name}! You're still a young one!!"
    else:
        print("Invalid age")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    try:
        user_age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        exit()

    greeting = greet(user_name, user_age)
    print(greeting)
