# You are given a unsorted list of student marks in ascending order:
# marks = [54, 18, 30, 24, 36, 60, 48, 12, 42]
# Tasks:
# 1. Write a Python function using binary search to find whether a given mark is present in the 
# list.
# 2. Use your function to determine if the mark 36 is in the list, and return its index if found.
# 3. If the mark is not found, your function should return -1

def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr=[54, 18, 30, 24, 36, 60, 48, 12, 42]
bubble(arr)

def binarysearch(arr, target):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right= right - 1
        else:
            left= left + 1
    return-1

print(arr)

target=36
result=binarysearch(arr, target)
if result != -1:
    print("Element is found at position ", result)
else:
    print("Element is not found.")
    