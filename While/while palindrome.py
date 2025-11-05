# Use a while loop to find out if a number is a palindrome.

x = (int(input("Enter a number ")))
m = x
y = 0
while x > 0:
    z=x%10
    y=y*10+z
    x=x//10
if m==y:
    print(m, "Is a palindrome.")
else:
    print(m, "Is not a palindrome.")