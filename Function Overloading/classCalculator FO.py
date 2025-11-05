# Write a class Calculator in Python that demonstrates function overloading using a method add().

# If one argument is passed → return the number itself.

# If two arguments are passed → return their sum.

# If more than two arguments are passed → return the sum of all arguments.

class Calculator:
    def add(self, a= None, b= None):
        if a is not None and b is not None:
            print (a+b)
        elif a is not None:
            print (a)
        else:
            print (0)
            
obj=Calculator()
obj.add()
obj.add(15)
obj.add(16,14)