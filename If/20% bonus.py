yos=int(input("Enter your years of service: "))
salary=int(input("Enter your salary: "))
if yos>=10:
    bonus= salary*1.2
elif yos>5 and yos <10:
    bonus= salary*1.1
else:
    bonus=salary
    print("Insufficient years of service.")

print ("You have a ",bonus)