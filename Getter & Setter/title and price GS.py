# Create a class Book with attributes title and price.

# Implement getter and setter methods.

# Ensure the price cannot be set below 0.

# Demonstrate usage with an object.

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    
    def get_title(self):
        return self.title
    
    def set_title(self,x):
        self.title=x
        
    def get_price(self):
        return self.price
    
    def set_price(self,y):
        self.price=y
        
        if y < 0:
            print("Price cannot be set to less than 0. We need profits...")
            
x=Book("Hamlet",5)

print(x.get_title())
print(x.get_price())

x.set_price(6)
print(x.get_price())