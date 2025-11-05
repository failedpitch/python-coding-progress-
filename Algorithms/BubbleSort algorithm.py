# Bubblesort - Algorithm 1

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:   # change > to < to make it descending
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 9, 1, 5, 6, 78]
bubble(arr)
print(arr)
