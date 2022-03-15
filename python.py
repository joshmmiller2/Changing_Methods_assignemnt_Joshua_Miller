class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        
    def make_deposit(self, amount):
        self.amount += amount
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
        
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
        

josh = User("Josh")
kyle = User("Kyle")
jeremy = User("Jeremy")




josh.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(45).display_user_balance()

kyle.make_deposit(100).make_deposit(100).make_withdrawal(45).make_withdrawal(110).display_user_balance()

jeremy.make_deposit(100).make_withdrawal(20).make_withdrawal(50).make_withdrawal(45).display_user_balance()