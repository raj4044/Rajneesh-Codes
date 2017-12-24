import random
x=random.randint(1,100)
count=0
print("Correct Guess : ",x)
choice=int(input("Enter a number between 1 and 100 : "))
while choice!=x:
    if choice>x:
        print("Please Lowerise")
        choice=int(input("Enter : "))
        count=count+1
    elif choice<x:
        print("Please! a higher number!!")
        choice=int(input("Enter : "))
        count=count+1

print("Correct Guess : ",x)
print("Number of guess = ",count+1)
    
