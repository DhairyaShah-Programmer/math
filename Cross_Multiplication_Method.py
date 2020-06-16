from time import *
wel = str(input("What is your Name: "))
print("Hello! " + wel)

aPlaceo = int(input("A1: "))
aPlacet = int(input("A2: "))
bPlaceo = int(input("B1: "))
bPlacet = int(input("B2: "))    
cPlaceo = int(input("C1: "))
cPlacet = int(input("C2: "))

bc = bPlaceo * cPlacet
bct = bPlacet * cPlaceo
ca = cPlaceo * aPlacet
cat = cPlacet * aPlaceo
one = aPlaceo * bPlacet
oneo = aPlacet * bPlaceo

xForm = bc - bct
yForm = ca - cat
divide = one - oneo
xCart = xForm/divide
yCart = yForm/divide
xp = "X: "
yp = "Y: "
xPrint = str(xp) + str(xCart)
yPrint = str(yp) + str(yCart)
print(xPrint + " and " + yPrint )

go = str(input(wel + "!" + "," " Did you like my program(note:answer in good or bad: )") )
if go == "Good":
    print("Thank You! " + wel)
else:
    print("I will improve it")

sleep(20)


    
