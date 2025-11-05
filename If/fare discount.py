#A bus fare is decided as follows:

#Adults (18–60): ₹100

#Children (< 18): ₹50

#Senior Citizens (60+): ₹70

#If it’s Sunday, give a 20% discount.
#Write a program that takes age and day as input and prints final fare.

day=input("Put in the day: ").strip().lower()
age=int(input("Put in your age: "))
fare=0
if age>=18 and age<=60:
    fare=100
elif age<18:
    fare=50
else:
    fare=70
if day=="sunday":
    fare=fare-(0.2*fare)
print("You have to pay", fare)