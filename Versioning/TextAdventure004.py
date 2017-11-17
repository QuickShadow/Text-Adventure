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




roomDescription = {}
roomNorth       = {}
roomEast        = {}
roomSouth       = {}
roomWest        = {}
roomUp          = {}
roomDown        = {}
roomItems       = {}

roomDescription ["EntryHall"] = "This a a description of the Entry Hall."
roomNorth       ["EntryHall"] = "MainHall"
roomEast        ["EntryHall"] = "null"
roomSouth       ["EntryHall"] = "null"
roomWest        ["EntryHall"] = "null"
roomUp          ["EntryHall"] = "null"
roomDown        ["EntryHall"] = "null"
roomItems       ["EntryHall"] = ["key", "candle", "candle"]

roomDescription ["Mainhall"] = "This a a description of the Entry Hall."
roomNorth       ["MainHall"] = "null"
roomEast        ["MainHall"] = "null"
roomSouth       ["MainHall"] = "EntryHall"
roomWest        ["MainHall"] = "null"
roomUp          ["MainHall"] = "null"
roomDown        ["MainHall"] = "null"
roomItems       ["MainHall"] = []

itemList = []
currentRoom = "EntryHall"


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
    print (roomDescription[currentRoom])
    roomItems[currentRoom].sort()
    for i, item in enumerate(roomItems[currentRoom]):
        if roomItems[currentRoom][i] != roomItems[currentRoom][i-1]:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)
        elif i==0:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)



def go(direction):
    if direction == "north":
        if roomNorth[currentRoom] != "null":
            currentRoom = roomNorth[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")
    elif direction == "east":
        if roomEast[currentRoom] != "null":
            currentRoom = roomEast[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")
    elif direction == "south":
        if roomSouth[currentRoom] != "null":
            currentRoom = roomSouth[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")
    elif direction == "west":
        if roomWest[currentRoom] != "null":
            currentRoom = roomWest[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")
    elif direction == "up":
        if roomUp[currentRoom] != "null":
            currentRoom = roomUp[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")
    elif direction == "down":
        if roomDown[currentRoom] != "null":
            currentRoom = roomDown[currentRoom]
            print (roomDescription[currentRoom])
        else:
            print ("You cannot go that way.")

            



        




while(True):
    try:
        playerInput = input()
        playerInput.lower ()
                      
        playerAction = playerInput.split(" ")
        
        if playerAction[0] == "take":
            addToList(playerAction[1])
            
        if playerAction[0] == "drop":
            removeFromList(playerAction[1])

        if playerAction[0] == "i":
            printInventory()

        if playerAction[0] == "go":
            go(playerAction[1])
        if playerAction[0] == "north":
            go(playerAction[0])
        if playerAction[0] == "east":
            go(playerAction[0])
        if playerAction[0] == "south":
            go(playerAction[0])
        if playerAction[0] == "west":
            go(playerAction[0])
        if playerAction[0] == "up":
            go(playerAction[0])
        if playerAction[0] == "down":
            go(playerAction[0])
        
        if playerAction[0] == "l":
            look()

    except:
        print ("That was not a recognised action.")
