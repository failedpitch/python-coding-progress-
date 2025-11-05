# Define an  class Payment with an abstract method pay(amount).

# Implement subclasses CreditCardPayment, PayPalPayment, and BitcoinPayment.

# Each should override pay() differently (e.g., printing different confirmation messages).

# Write a function checkout(payment_obj, amount) that works polymorphically with any payment method.

class Payment:
    def Pay(self):
        return "no payment method used."

class CreditCardPayment(Payment):
    def __init__(self):
        self.CreditCardPayment_Payment = "Payment method: CreditCardPayment"

    def Pay(self):
        return self.CreditCardPayment_Payment
    
class PayPalPayment(Payment):
    def __init__(self):
        self.PayPalPayment_Payment = "Payment method: PayPalPayment"
        
    def Pay(self):
        return self.PayPalPayment_Payment
    
class BitcoinPayment(Payment):
    def __init__(self):
        self.BitcoinPayment_Payment = "Payment method: BitcoinPayment"
        
    def Pay(self):
        return self.BitcoinPayment_Payment
    
paymentmethods = [CreditCardPayment(), PayPalPayment(), BitcoinPayment()]

for i in paymentmethods:
    print(i.Pay())