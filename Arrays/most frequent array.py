# Write a program to find the most frequent element in the array.

# Example:
# Input: [7, 8, 7, 5, 7, 8, 8]
# Output: Most frequent element = 7 or 8 (both appear 3 times)

def most_frequent(arr):
    f = {}
    for i in arr:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    m = max(f.values())
    for k, v in f.items():
        if v == m:
            print("Most frequent element =", k, "appears", v, "times")

arr = [7, 8, 7, 5, 7, 8, 8]
most_frequent(arr)