itemList = []

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

        


