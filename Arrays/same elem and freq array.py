# You are given two arrays. Write a program to check if both arrays contain the same 
# elements with the same frequency, regardless of order.

# Example:
# Input:
# arr1 = [1, 2, 2, 3]
# arr2 = [2, 1, 3, 2]
# Output: Arrays are equal

def count(arr1,arr2):
    if len(arr1)!=len(arr2):
        print("Arrays are not equal")
        return
    u=[]
    x=[]
    for i in arr1:
       if arr1 not in u:
           u.append(i)
    for i in arr2:
        if arr2 not in x:
            x.append(i)
    if u[i]==x[i]:
        print("Arrays are equal.")
    else:
        print("Arrays are not equal.") 
        
arr1=[1,2,2,2,3]
arr2=[1,2,3]
count(arr1,arr2)