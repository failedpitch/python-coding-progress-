# A file story.txt contains some text.
# Write a program to count how many times the word "the" appears (case-insensitive).

words=0

with open("story.txt", "r") as f:
    
    for i in f:
        x = i.lower().split()
        words = words + x.count("the")
    
print (words, "times.")