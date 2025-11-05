def check_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Arrays are not equal")
        return
    freq1 = {}
    freq2 = {}
    for i in arr1:
        freq1[i] = freq1.get(i, 0) + 1
    for i in arr2:
        freq2[i] = freq2.get(i, 0) + 1
    if freq1 == freq2:
        print("Arrays are equal")
    else:
        print("Arrays are not equal")

arr1 = [1, 2, 2, 3]
arr2 = [2, 1, 3, 2]
check_arrays_equal(arr1, arr2)