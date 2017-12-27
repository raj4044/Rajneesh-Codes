import random

#Enter a four-digit number
G_Num = input("Enter a 4-digit number(1000 to 9999) : ")

#Generate a random 4-digit number
R_Num = str(random.randint(1000, 9999))

#Run loop
while G_Num != R_Num:
    listg = list(G_Num)
    listr = list(R_Num)

    #Initiate Cows and Bulls.
    Cows = 0
    Bulls = 0
    for i in range(4):
        if listg[i] == listr[i] :
            Cows += 1
        else:
            for j in range(4) :
                if listg[i] == listr[j]:
                    Bulls += 1

    #print next result
    print("Cows = ",Cows)
    print("Bulls = ",Bulls)

    #Take next input
    G_Num = input("Enter a 4-digit number(1000 to 9999) : ")


#After success
print("""Cows = 4
Succed!!""")
print("Correct Number is ",R_Num)
