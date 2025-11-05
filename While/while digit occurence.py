# Input a number and a digit, then use a while loop to count how many times that digit appears.
# Example: Number = 122333, Digit = 3 → Occurs 3 times.

occurrence=0
num=int(input("Enter a number "))
digit=int(input("Enter a digit for checking "))
while num>0:
    y=num%10
    if y==digit:
     occurrence=occurrence+1
    num=num//10
print("The digit occurs", occurrence, "times")