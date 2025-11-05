# Write a program to find the largest number from 
# 10 numbers entered by the user using a for loop.

largest=0
for j in range(0, 10):
 num=int(input("Enter your numbers "))     
 if num>largest:
     largest=num
print("Your largest number is: ",largest)