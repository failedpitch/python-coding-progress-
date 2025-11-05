# Write a Python class BankAccount with:

# Attributes: account_number, balance

# Getter and Setter methods for balance

# Setter must not allow the balance to become negative.

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def get_account_number(self):
        return self.account_number
    
    def set_account_number(self,x):
        self.account_number=x
        
    def get_balance(self):
        return self.balance
    
    def set_balance(self,y):
        
        if y < 0:
            print('Error Detected.')
        else:
            self.balance = y

x=BankAccount(12344, 1000)
print(x.get_account_number())
print(x.get_balance())

x.set_balance(-12)
print(x.get_balance())