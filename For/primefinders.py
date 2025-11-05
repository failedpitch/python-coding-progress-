for num in range(2,11):
    is_prime=True
    for i in range(2, 11):
        if num % i == 0:
            is_prime=False
            break
    if is_prime:
        print(num)