# Write a program to print all prime numbers
# between 1 and 10 using a for loop.

for i in range(2, 11):
    is_prime=True
    for j in range(2, i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
