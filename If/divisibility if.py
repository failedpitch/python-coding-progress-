num=int(input("Enter your number: "))
if num%3==0 and num%5==0 :
    print("Divisible by both")
elif num%3==0 :
    print("Divisible by only 3")
elif num%5==0 :
    print("Divisible by only 5")
else :
    print("ineligible")    
