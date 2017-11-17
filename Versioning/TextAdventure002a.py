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

##def go(direction):
##    if facing == 0:
##        direction={FORWARD=NORTH, RIGHT=EAST, BACKWARD=SOUTH, LEFT=WEST}
##        dircetion={F=NORTH, R=EAST, B=SOUTH, L=WEST}
##    elif facing == 1:
##        direction={RIGHT=NORTH, BACKWARD=EAST, LEFT=SOUTH, FORWARD=WEST}
##        dircetion={R=NORTH, B=EAST, L=SOUTH, F=WEST}
##    elif facing == 2:
##        direction={BACKWARD=NORTH, LEFT=EAST, FORWARD=SOUTH, RIGHT=WEST}
##        dircetion={B=NORTH, L=EAST, F=SOUTH, R=WEST}
##    elif facing == 3:
##        direction={LEFT=NORTH, FORWARD=EAST, RIGHT=SOUTH, BACKWARD=WEST}
##        dircetion={L=NORTH, F=EAST, R=SOUTH, B=WEST}
##    print direction





while(True):
    
    playerInput = input()
    
    playerAction = playerInput.split(" ")

    if playerAction[0] == "take":
        addToList(playerAction[1])

    if playerAction[0] == "drop":
        if itemList.count(playerAction[1]) >0:
            removeFromList(playerAction[1])
        else:
            print("You do not have a "+playerAction[1]+".")
        
    if playerAction[0] == "i":
        printInventory()

    if playerAction[0] == "go":
        go(playerAction[1])



