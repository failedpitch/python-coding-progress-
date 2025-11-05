# You are given an array and a target sum. Find all pairs of elements whose sum equals the target.

# Example:

# Input: arr = [1, 2, 3, 4, 5], target = 5
# Output: (1, 4), (2, 3)

def findPairs(arr,target):
  pairs=[]
  n=len(arr)
  for i in range(n):
    for j in range(i+1,n):
      if arr[i]+arr[j]==target:
        pairs.append((arr[i],arr[j]))
  return pairs

arr=[1,2,3,4,5,6]
target=5
print(findPairs(arr,target))