# Write a program to check whether a given number is an Armstrong number.

armstrong=0
num=int(input("Write a number "))
m=num
for i in range(1, num+1):
    x=num%10
    armstrong=armstrong+x*x*x
    num=num//10
if armstrong==m:
 print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")