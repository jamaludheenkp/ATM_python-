#  Bank app project python

class Bank :

    def __init__(self, initial_amount = 0.00) :
        self.balance = initial_amount

    # write a transaction log , details
    def transaction_log(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string}\t\tNow Available Balance is: {self.balance}\n")


    #  transaction withdrawal
    def withdrawal (self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transaction_log(f"withdrawal:{amount}")

        
    #  transaction deposited
    def deposit (self, amount):
        try:
           amount = float(amount)
        except ValueError:
           amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction_log(f"deposited:{amount}")


account = Bank(50.15)


# get the user actions withdrawal or deposit
while True:
    try:
        action = input("What kind of action do you want to take..?")
    except KeyboardInterrupt:
        print("\nleaving at the ATM, Thank you..😎 visit again...\n1")
        break
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal" :
            amount = input("How much do you want to take out..?")
            account.withdrawal(amount)
        else:
            amount = input("How  much do you want to put in..?")
            account.deposit(amount)

        print("Your Current Balance is :", account.balance)

    else:
        print("\nThat is a valid action.., try again...!\n")
