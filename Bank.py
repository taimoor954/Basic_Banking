class Bank:
    def __init__(self, initialAmount = 0.00):
        self.balance = 0.00
    
    def logTransaction(self, transactionString):
        print(transactionString)
        with open('transaction.txt', 'a') as file:
            file.write(f"{transactionString} \t\t current balance is {self.balance}\n\n")

    def withDrawal(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                print('sorry but the amount youre asking is too much')
                return
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


account = Bank(0.0)
while True:
    action = input("What kind of action do you want to take? ")
    if action in ['withdrawal', 'deposit']:
        if action == 'withdrawal':
            amount = input("How much do you want to with draw?")
            account.withDrawal(amount)
        elif action == 'deposit':
            amount = input("How much do you want to deposit?")
            account.deposit(amount)
    else:
        print("enter your action again")
        
