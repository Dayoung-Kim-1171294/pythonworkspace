def open_account():
    print("New account has been created.")

open_account()

def deposit(balance, money):
    print(f"Deposit completed. Balance is {balance + money} ")
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f"Withdrawal completed. Balance is {balance - money}")
        return balance - money
    else:
        print("Insufficient balance")
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balane = 0
balance = deposit(balane, 500)
balane = withdraw(balance, 100)
commission, balance = withdraw_night(balance, 200)

print(commission, balance)

