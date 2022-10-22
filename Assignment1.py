#Assignment 1:
#Create a program that will print your nickname using only asterisk character (*)

Name = "KENT"
printK = [[" " for i in range(5)] for j in range(5)]
printE = [[" " for i in range(5)] for j in range(5)]
printN = [[" " for i in range(5)] for j in range(5)]
printT = [[" " for i in range(5)] for j in range(5)]
#Letter K
for row in range(5):
    for colum in range(5):
        if colum==0 or (row+colum==3 and row<3) or (colum==row-1 and row>2):
            printK[row][colum] = "*"

#Letter E
for row in range(5):
    for colum in range(5):
        if (colum==0 or (row==0 or row==2 or row==4) and (colum>0)):
            printE[row][colum] = "*"

#Letter N
for row in range(5):
    for colum in range(5):
        if colum==0 or colum==4 or row==colum:
            printN[row][colum] = "*"

#Letter T
for row in range(5):
    for colum in range(5):
        if colum==2 or (row==0 and colum!=2):
            printT[row][colum] = "*"

for i in range(5):
    for j in range(5):
        print(printK[i] [j],end="")
    print(end=" ")
    for j in range(5):
        print(printE[i] [j],end="")
    print(end="  ")
    for j in range(5):
        print(printN[i] [j],end="")
    print(end=" ")
    for j in range(5):
        print(printT[i] [j],end="")
    print()

