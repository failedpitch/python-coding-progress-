# You are given an array of integers. Write a program to find the second most frequent 
# element in the array.

# If multiple elements qualify, print any one of them.

# If no second most frequent element exists, print a suitable message.

# Example:
# Input: [1, 2, 2, 3, 3, 3, 4]
# Output: Second most frequent element = 2

def second_most_frequent(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    first_max = second_max = -1
    for count in freq.values():
        if count > first_max:
            second_max = first_max
            first_max = count
        elif count > second_max and count != first_max:
            second_max = count

    if second_max == -1:
        print("No second most frequent element exists")
        return

    for key, value in freq.items():
        if value == second_max:
            print("Second most frequent element =", key)
            return

arr = [1, 2, 2, 2, 2, 3, 3, 3, 4]
second_most_frequent(arr)