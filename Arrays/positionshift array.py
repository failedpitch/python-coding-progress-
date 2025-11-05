# You are given an array and a number k.
# You need to shift all elements of the array to the left by k positions.
# Elements that move past the first position wrap around to the end.

# Example

# Input:

# arr = [1, 2, 3, 4, 5, 6]
# k = 2

# Output:

# [3, 4, 5, 6, 1, 2]

def shift(arr, k):
    k=k%len(arr)
    return(arr[k:])+(arr[:k])
    
arr=[1,2,3,4,5,6]
k = 2
result=shift(arr, k)
print(result)

# Array slicing, "k:" gives 3 4 5 6 in this case, ":k" gave 1 2 3 4
