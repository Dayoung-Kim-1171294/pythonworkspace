# user defined error
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

# similar to Java's toString() method
    def __str__(self):
        return self.msg
    

try:
    print("dividing...")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input values: {0}, {1}".format(num1, num2))
    print(f"{num1} divided by {num2} is {num1 / num2}")
except ValueError as ve:
    print("Invalid input:", ve)

    # err: instance of BigNumberError
except BigNumberError as err:
    print("Error: Numbers must be less than 10.")

    # print(str(err))
    # print(err.__str__())
    # print(err.msg)
    print(err)

# executed always
finally:
    print("End of program.")
