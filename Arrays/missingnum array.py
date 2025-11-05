# You are given an array of size n-1, which contains numbers from 1 to n.
# One number is missing. You need to find that missing number.

# Example

# Input: arr = [1, 2, 4, 5]
# Here n = 5 (since numbers should be 1 to 5)

# Missing number = 3

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

n = int(input("Enter value of n (range from 1 to n): "))
arr = list(map(int, input("Enter numbers separated by space: ").split()))
missing = find_missing_number(arr, n)
print(" Missing number is:", missing)