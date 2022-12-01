class Bank:
    def __init__(self, initialAmount = 0.00):
        self.balance = 0.00
    
    def logTransaction(self, transactionString):
        print(transactionString)
        with open('transaction.txt', 'a') as file:
            file.write(f"{transactionString}\n")

    def withDrawal(self, amount):
        try:
            amount = float(amount)
        except Exception as e:
           amount = 0 
        if amount:
            self.balance = self.balance - amount
            self.logTransaction(f"Transaction with drawal is {amount}")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
            self.balance = self.balance + amount
        except Exception as e:
            amount = 0
        if amount:
             self.balance = self.balance + amount
             self.logTransaction(f"Transaction deposit is {amount}")



account = Bank(50.50)
account.deposit(50.50)
print(account.balance)
account.withDrawal(10)
print(account.balance)