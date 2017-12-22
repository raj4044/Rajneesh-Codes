#We are going to add all primes between two number

def chk(llim, ulim):
    #introduce iteration variable
    x = llim
    summation = 0
    #start conditional loop
    while x <= ulim:
        if x > 2:
            for i in range(2,x):
                if x % i == 0:
                    count = 'FALSE'
                    break
                else:
                    count = 'TRUE'
                    continue
            if count =='TRUE':
                summation = summation + x
        x = x + 1
    return summation

#For continuous use                    
true = 1
while True:
    #Demand Boundary Values
    llim = int(input("Enter lower limiting value : "))
    ulim = int(input("Enter upper limiting value : "))

    if llim >= 3:
        print("The summation of all prime numbers between ",llim," and ",ulim," is ",chk(llim, ulim))
    elif llim == 1:
        print("The summation of all prime numbers between ",llim," and ",ulim," is ",chk(llim, ulim)+3)
    elif llim == 2:
        print("The summation of all prime numbers between ",llim," and ",ulim," is ",chk(llim, ulim)+2)

