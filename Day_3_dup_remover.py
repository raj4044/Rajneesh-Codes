#to remove duplicate element

#Accept input sentence from user
Sent = input("Enter Sentence for correction :")

#Split the sentence
lists = Sent.split(" ")

#define an empty list and and an empty set
Out = []
dup = set()

#Run loop
for i in lists:
    if i not in dup:
        #add element to both set and list
        Out.append(i)
        dup.add(i)

#Join and display output
print((" ").join(Out))
