# InsertionSort algorithm

def insertionSort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
      arr[j+1]=arr[j]
      j=j-1
      arr[j+1]=key

arr=[54,18,30,24,36,60,48,12,42]
insertionSort(arr)
print(arr)