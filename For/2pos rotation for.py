# Given a list [1, 2, 3, 4, 5], write a program using a for loop that 
# rotates the list to the right by 2 positions.
# (Output → [4, 5, 1, 2, 3])

list=[1, 2, 3, 4, 5]
n=len(list)

r=2
for i in range(r):
    last=list[-1]
    
    for j in range(n-1, 0, -1):
        list[j]=list[j-1]
    list[0]=last
    
print(list)