try:
    print("calculating...")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} divided by {num2} is {num1 / num2}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(e)
except Exception as err:
    print("An unexpected error occurred.")
    print(err)
