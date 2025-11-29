balance = 50000
pin = 1234

while True:
    user_pin = int(input("Enter your pin: "))

    if user_pin == pin:
        print(f"Your balance is {balance}")
        amount = int(input("Enter the amount you want to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print(f"Updated Balance: {balance}")
        else:
            print("Insufficient balance!")
        break
    else:
        print("Pin is incorrect")
        break
