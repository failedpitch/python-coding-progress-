# Write a program to calculate the sum of factorials of the first 6 numbers.
# (1! + 2! + 3! + 4! + 5! + 6!)

sum=0
n=(int(input("Enter your number")))
for i in range(1, n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    sum=sum+f
    
print(sum)
