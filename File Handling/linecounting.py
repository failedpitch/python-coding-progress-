with open("Student.txt","r") as f:
    lines=f.readlines()
    
line_count=len(lines)
words=sum(len(line.split()) for line in lines)
chars=sum(len(line) for line in lines)

print(line_count)
print(words)
print(chars)