try:
    print("dividing...")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError("Numbers must be less than 10.")
    print(f"{num1} divided by {num2} is {num1 / num2}")
except ValueError as ve:
    print("Invalid input:", ve)
except ZeroDivisionError as zde:
    print("Error: Cannot divide by zero.", zde)
except Exception as err:
    print("An unexpected error occurred.", err)