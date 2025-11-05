# You are given an array of integers. Write a program to find the maximum difference 
# between any two elements such that the larger element comes after the smaller element.

# Example:
# Input: [2, 3, 10, 6, 4, 8, 1]
# Output: Maximum difference = 8
# Explanation: 10 - 2 = 8

# Input: [7, 9, 5, 6, 3, 2]
# Output: Maximum difference = 2
# Explanation: 9 - 7 = 2

def maximum_difference(arr):
    if len(arr) < 2:
        return 0
    
    