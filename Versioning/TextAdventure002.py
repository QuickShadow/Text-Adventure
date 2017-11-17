itemList = []
facing = 0

def addToList(item):
    itemList.append(item)
    
def removeFromList(item):
    itemList.remove(item)

def printInventory():
    itemList.sort()
    for i, item in enumerate(itemList):
        if itemList[i] != itemList[i-1]:
            print (str(itemList.count(item)) + "x " + item)
        elif i==0:
            print (str(itemList.count(item)) + "x " + item)

def go(moving):
    print (moving)
##    if facing == 0:
##        direction={"FORWARD":"NORTH", "RIGHT":"EAST", "BACKWARD":"SOUTH", "LEFT":"WEST", "F":"NORTH", "R":"EAST", "B":"SOUTH", "L":"WEST"}
##    elif facing == 1:
##        direction={"RIGHT":"NORTH", "BACKWARD":"EAST", "LEFT":"SOUTH", "FORWARD":"WEST", "R":"NORTH", "B":"EAST", "L":"SOUTH", "F":"WEST"}
##    elif facing == 2:
##        direction={"BACKWARD":"NORTH", "LEFT":"EAST", "FORWARD":"SOUTH", "RIGHT":"WEST", "B":"NORTH", "L":"EAST", "F":"SOUTH", "R":"WEST"}
##    elif facing == 3:
##        direction={"LEFT":"NORTH", "FORWARD":"EAST", "RIGHT":"SOUTH", "BACKWARD":"WEST", "L":"NORTH", "F":"EAST", "R":"SOUTH", "B":"WEST"}
##    print (direction[moving])





while(True):
    
    playerInput = input()
    playerInput = playerInput.upper()
    playerAction = playerInput.split(" ")

    if playerAction[0] == "TAKE":
        addToList(playerAction[1])

    if playerAction[0] == "DROP":
        if itemList.count(playerAction[1]) >0:
            removeFromList(playerAction[1])
        else:
            print("You do not have a "+playerAction[1]+".")
        
    if playerAction[0] == "I":
        printInventory()

    if playerAction[0] == "GO":
        go(playerAction[1])



