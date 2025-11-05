# Binary Search

def binarySearch(arr,target):
  left=0
  right=len(arr)-1
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]<target:
      left=mid+1
    else:
      right=mid-1
  return -1


arr=[7,19,23,27,46,49,53,59]
target=27
r=binarySearch(arr,target)
if r!=-1:
  print("Element is found at position: ",r)
else:
  print("Element is not found")