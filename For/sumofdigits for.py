# Write a program to print the sum of the digits of a number using a for 
# loop.

# n=int(input("Enter a number: "))
# num=str(n)
# sum=0

# for i in num:
#  sum=sum+int(i)

# print(sum)

n=int(input("Enter your numbers "))
sum=0
for i in range(len(str(n))):
    d=n%10
    sum=sum+d
    n=n//10
print(sum)