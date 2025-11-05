# Write a program using a for loop to reverse a list [1, 2, 3, 4, 5, 6].
# (Output → [6, 5, 4, 3, 2, 1])

list=[1,2,3,4,5,6]
rev=[]

for i in range(len(list)-1,-1,-1):
    rev.append(list[i])
    
print(rev)