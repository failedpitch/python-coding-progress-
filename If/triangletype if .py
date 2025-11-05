# Write a program to check whether a triangle is Equilateral, 
# Isosceles, or Scalene, based on its side lengths.

a=int(input("Enter the angle of side A: "))
b=int(input("Enter the angle of side B: "))
c=int(input("Enter the angle of side C: "))
if a==b and c==a and b==c:
    print("Equilateral Triangle")
elif a!=b and c!=a and b!=c:
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")
    
    