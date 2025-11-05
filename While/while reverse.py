# Write a program to reverse a number using a while loop.
# (Example: 1234 → 4321)

n=int(input("Enter a number "))
x = 0
while n > 0:
    y = n % 10
    x = x * 10 + y
    n = n // 10
print(x)