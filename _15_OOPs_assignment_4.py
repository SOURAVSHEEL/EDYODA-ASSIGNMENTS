## CHALLENGE 4 : IMPLEMENT A BANKING ACCOUNT: 

class Account:

    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
    
    def displayAccount(self):
        print(f"TITLE : {self.title} \nBALANCE : {self.balance}")

class SavingsAccount(Account):

    def __init__(self,title,balance,interestRate):
        super().__init__(title,balance)
        self.interestRate = interestRate
      
    def displaySavingAccount(self):
        print(f"TITLE : {self.title} \nBALANCE : {self.balance} \nINTERESTE RATE : {self.interestRate}")

# account = Account("Sourav",5000)
# account.displayAccount()

savingsaccount = SavingsAccount("Sourav",5000,5)
savingsaccount.displaySavingAccount()
