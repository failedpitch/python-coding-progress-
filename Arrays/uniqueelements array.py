# You are given an array of integers. Count and display the number of unique elements in the array.

# Example:
# Input: [1, 2, 2, 3, 4, 4, 4, 5]
# Output: 5 unique elements

def count(arr):
  u=[]
  for i in arr:
    if i not in u:
      u.append(i)
  print(len(u)," Unique elements")

arr=[2,2,2,2,2,3,4]
count(arr)