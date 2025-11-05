chars = ['D', 'T', 'H', 'R']

for i in range(1, len(chars)):
    key = chars[i]
    j = i - 1

    while j >= 0 and chars[j] > key:
        chars[j + 1] = chars[j]
        j -= 1

    chars[j + 1] = key

print(chars)