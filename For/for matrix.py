# Write a program that asks the user to enter a square matrix (as a 2D list)
# and then uses for loops to calculate the sum of both diagonals.

# Example input:

# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

# Expected output:

# Primary diagonal sum = 15
# Secondary diagonal sum = 15

n=int(input("Enter size of my matrix"))
matrix=[]

for i in range(n):
  row=[]
  for j in range(n):
    value=int(input("Enter me a number for matrix: "))
    row.append(value)
  matrix.append(row)


for i in matrix:
  print(i)

left=0
right=0
for i in range(n):
  left = left+matrix[i][i]
  right=right+matrix[i][n-i-1]

print(left)
print(right)