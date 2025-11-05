# Find the alternating sum of digits of a number.
# Example: 1234 → 1-2+3-4 = -2.

# num=int(input("Enter a number "))
# sign=1
# sum=0
# while num>0:
#     f=num%10
#     sum=sum+f*sign
#     sign=sign*(-1)
#     num=num//10
# print(sum)

sum = 0
num = int(input("Enter a number "))
rev = 0
temp = num

while temp > 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10

sign = 1
while rev > 0:
    f = rev % 10
    sum = sum + f * sign
    sign = sign * -1
    rev = rev // 10

print(sum)