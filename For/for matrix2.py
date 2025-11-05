# Write a Python program that:

# 1. Takes a matrix input from the user (number of rows and columns decided by user).

# 2. Displays the matrix neatly in grid format.

# 3. Calculates and prints the sum of each row separately.

# Example:

# Input (3x3 matrix):
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# Matrix:
# 1 2 3
# 4 5 6
# 7 8 9

# Row sums:
# Row 1 → 6
# Row 2 → 15
# Row 3 → 24

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix values:")
for i in range(rows):
    row = []
    for j in range (cols):
        value = int(input("Enter value for position ({i+1}, {j+1}): "))
        row.append(value)
    matrix.append(row) 
    
for i in range(rows):
    sum=0
    for j in range (cols):
        sum=sum+matrix[i][j]
    print(sum)      
    