class Account:
    def __init__(self):
        self.amount=int(input("enter amount:"))
    def deposit(self):
        x=1000
        print("your new account balance",x)
        self.amount=x+self.amount
        print("After deposit your total balance is",self.amount)
    def withdraw(self):
        print(self.amount)
        y=int(input("enter amount to withdraw"))
        self.amount=self.amount-y
        print("your balance remains after withdrawn",self.amount)
class SavingsAccount(Account):
    def withdraw(self):
        super().deposit()
        a=int(input("enter amount to withdraw:"))
        if(a<25000):
            self.amount=self.amount-a
            print("now your savings account balance is:",self.amount)
        else:
            print("you are trying to with draw more than 25k but your limit is to draw less than 25k per day")
class CurrentAccount(Account):
     def withdraw(self):
        super().deposit()
        a=int(input("enter amount to withdraw:"))
        if(a>self.amount):
            self.amount=self.amount-a
            print("now your Current account balance is:",self.amount)
            if(self.amount<0):
                print("your bank balance is less than 0 after deposition we can subtract the amount from your deposition")
        else:
            self.amount=self.amount-a
            print("after withdrawn your current account balance is:",self.amount)
obj1=SavingsAccount()
obj1.withdraw()
ob2=CurrentAccount()
ob2.withdraw()
