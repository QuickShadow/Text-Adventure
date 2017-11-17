actionDictionary = {}
actionDictionary ["take"] = "take"
actionDictionary ["get"] = "take"
actionDictionary ["drop"] = "drop"
actionDictionary ["use"] = "use"
actionDictionary ["light"] = "use"
actionDictionary ["go"] = "go"
actionDictionary ["move"] = "go"
actionDictionary ["quit"] = "quit"
actionDictionary ["q"] = "quit"
actionDictionary ["end"] = "quit"
actionDictionary ["look"] = "look"
actionDictionary ["l"] = "look"

directionDictionary = {}
directionDictionary ["north"] = "north"
directionDictionary ["n"] = "north"
directionDictionary ["east"] = "east"
directionDictionary ["e"] = "east"
directionDictionary ["south"] = "south"
directionDictionary ["s"] = "south"
directionDictionary ["west"] = "west"
directionDictionary ["w"] = "west"
directionDictionary ["up"] = "up"
directionDictionary ["u"] = "up"
directionDictionary ["down"] = "down"
directionDictionary ["d"] = "down"


itemDictionary = {}
itemDictionary ["candle"]= "candle"
itemDictionary ["journal"] = "journal"
itemDictionary ["book"] = "journal"
itemDictionary ["ladder"]= "ladder"
itemDictionary ["lamp"] = "lamp"
itemDictionary ["key"] = "key"
itemDictionary ["telescope"] = "telescope"

roomItems = {}

roomEntryHall = {}
roomEntryHall ["description"] = "This a a description of the Entry Hall."
roomEntryHall ["north"] = "mainHall"
roomEntryHall ["east"] = "null"
roomEntryHall ["south"] = "null"
roomEntryHall ["west"] = "null"
roomEntryHall ["up"] = "null"
roomEntryHall ["down"] = "null"
roomItems ["entryHall"] = ["key", "candle"]

roomMainHall = {}
roomMainHall ["description"] = "This a a description of the Main Hall."
roomMainHall ["north"] = "null"
roomMainHall ["east"] = "null"
roomMainHall ["south"] = "entryHall"
roomMainHall ["west"] = "null"
roomMainHall ["up"] = "null"
roomMainHall ["down"] = "null"
roomItems ["mainHall"]= []

itemList = []
currentRoom = "entryHall"


def addToList(item):
    try:
        itemList.  append(roomItems[currentRoom].  pop(  roomItems.get(currentRoom).  index(playerAction[1]  )))
    except:
        print (playerAction[1] + " cannot be taken.")

def removeFromList(item):
    try:
        roomItems[currentRoom].  append(itemList.  pop(  itemList.  index(playerAction[1]  )))
    except:
        print ("You do not have a " + playerAction[1] + ".")
        
def printInventory():
    itemList.sort()
    for i, item in enumerate(itemList):
        if itemList[i] != itemList[i-1]:
            print (str(itemList.count(item)) + "x " + item)
        elif i==0:
            print (str(itemList.count(item)) + "x " + item)

def look():
    roomItems[currentRoom].sort()
    for i, item in enumerate(roomItems[currentRoom]):
        if roomItems[currentRoom][i] != roomItems[currentRoom][i-1]:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)
        elif i==0:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)

def checkAction():
    if playerAction[0] == "take":
            addToList(playerAction[1])
            
    elif playerAction[0] == "drop":
        removeFromList(playerAction[1])

    elif playerAction[0] == "i":
        printInventory()

    elif playerAction[0] == "go":
        go(playerAction[1])

    elif playerAction[0] == "look":
        look()

    else:
        print ("That was not a recognised action.")
        

while(True):
    try:
        playerInput = input()
        playerInput.lower ()
                      
        playerAction = playerInput.split(" ")
        checkAction()
 
    except:
        print ("ERROR")
