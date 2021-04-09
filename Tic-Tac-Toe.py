#Tic-Tac-Toe

"""
 │ │ 
-----
 │ │ 
-----
 │ │ 
"""
"""
Instead of printing spaces as we see above, we had to integrate the currentField
into the drawField function and assign values to where spaces were.
"""

def drawField(field):
    for row in range(5):                    #0,1,2,3,4(the values of the range)
        if row%2 == 0:                                  #even numbers ONLY
            practicalRow = int(row/2)                   #0,1,2 (even numbers)
            for column in range(5):                     #0,1,2,3,4 (range values)
                if column%2 ==0:                        #even numbers ONLY
                    practicalColumn = int(column/2)      #0,1,2 (even numbers)
                    if column != 4:                     #when column is NOT 4
                        print(field[practicalColumn][practicalRow],end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("│",end="")
        else:
            print("-"*5)
Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentField)

while(True):
    print("Players turn: ",Player)
    moveRow= int(input("Enter the row: "))
    moveColumn= int(input("\nEnter the column: "))
    if Player == 1:
        #make move for player 1
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            Player = 2
    else:
        #make move for player 2
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            Player = 1
            
    drawField(currentField)
