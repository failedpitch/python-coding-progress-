# You are given an array. Count how many times each element occurs in the array.

# Example:

#Input: arr = [2, 3, 2, 5, 3, 2, 4]
#Output:
#2 occurs 3 times
#3 occurs 2 times
#5 occurs 1 time
# 4 occurs 1 time

def count(arr):
  f={}
  for i in arr:
    if i in f:
      f[i]=f[i]+1
    else:
      f[i]=1

  for key,value in f.items():
    print(key," = ",value)

arr=[1,2,3,4,5,5,6,6,6]
count(arr)  
# 1:2 , 3:1 , 4:2