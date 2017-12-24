
x=0
y=0
z=0
print("New Co-ordinate is : ",x,",",y)
while z>=0:
    dirn=input("Enter Direction(R for Right/L for Left/F for Forward/B for Backward) : ")
    dist = int(input("How Much : "))
    if dirn == 'R':
        x= x- dist
        y=y
    elif dirn == 'L':
        x= x+ dist
        y=y
    elif dirn == 'F':
        x=x
        y= y+ dist
    elif dirn == 'B':
        x=x
        y= y- dist
    print("New Co-ordinate is : ",x,",",y)
    z=z+1
