# For a given square matrix, print its upper triangular and lower triangular forms.

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
    for j in range(cols):
        if i<=j:
            print(matrix[i][j], end=" ")
            
        else:
            print(" ", end=" ")
    print()
    
for i in range(rows):
    for j in range(cols):
        if i>=j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()    