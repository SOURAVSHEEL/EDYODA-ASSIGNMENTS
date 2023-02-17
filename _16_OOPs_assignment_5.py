## CHALLENGE 5 : HANDLING A BANK ACCOUNT


class Account:

    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    

    def withdrawal(self,amount):
        self.balance = self.balance - amount
        return self.balance

    def getbalance(self):
        return self.balance


class SavingsAccount(Account):

    def __init__(self,title = None,balance = 0, interestRate = 0):
        super().__init__(title,balance)
        self.interestRate = interestRate

    def interestAmount(self):
        print("INTERSET AMOUNT : ",(self.balance* self.interestRate)/100)

    def displaySavingAccount(self):
        print(f"TITLE : {self.title} \nBALANCE : {self.balance} \nINTEREST RATE : {self.interestRate}")


savingsaccount = SavingsAccount("Sourav",5000,5)
savingsaccount.displaySavingAccount()
savingsaccount.interestAmount()

# print(savingsaccount.getbalance())