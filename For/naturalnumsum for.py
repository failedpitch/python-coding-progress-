# Write a program to find the sum of squares of the first 
# 10 natural numbers.

sum=0
n=int(input("Enter your numbers "))
for i in range(1, n+1):
    sum=sum+i*i
print("The sum is", sum)