age = int(input("Enter age: "))
day = input("Enter day: ").strip().lower()

if age < 18:
    fare = 50
elif age >= 60:
    fare = 70
else:
    fare = 100

if day == "sunday":
    fare = fare - (fare * 0.20)

print("Final Fare: ₹", fare)