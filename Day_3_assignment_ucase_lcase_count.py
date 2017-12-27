#Enter String
String = input("Give Input Please!_ ")

#Break it out into a list
lists = list(String)

#initialise count
countl=countu=0

#Implement codition
for i in String:
    if i.islower() == True:
        countl+=1
    else:
        countu+=1

#Print Output
print("Number of lowercase alphabets is ",countl," and number uppercase alphabets is ",countu)
