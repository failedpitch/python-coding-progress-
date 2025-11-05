with open("Student.txt","w") as f:
    f.write("Alice \n")
    f.write("Maurice \n")
    f.write("Peter \n")
    
with open("Student.txt","r") as f:
    c=f.read()
    print(c)