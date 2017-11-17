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
actionDictionary ["save"] = "save"
actionDictionary ["load"] = "load"

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
itemDictionary ["matches"] = "matches"
itemDictionary ["matchbox"] = "matches"


roomStatus      = {}
roomDescription = {}
roomNorth       = {}
roomEast        = {}
roomSouth       = {}
roomWest        = {}
roomUp          = {}
roomDown        = {}
roomItems       = {}

## Basement

## Ground Floor

roomStatus      ["FrontDoor"] = 0
roomDescription ["FrontDoor"] = ["This a a description of the FrontDoor."]
roomNorth       ["FrontDoor"] = "EntryHall"
roomEast        ["FrontDoor"] = "null"
roomSouth       ["FrontDoor"] = "null"
roomWest        ["FrontDoor"] = "null"
roomUp          ["FrontDoor"] = "null"
roomDown        ["FrontDoor"] = "null"
roomItems       ["FrontDoor"] = []

roomStatus      ["EntryHall"] = 0
roomDescription ["EntryHall"] = ["This a a description of the Entry Hall."]
roomNorth       ["EntryHall"] = "MainHall"
roomEast        ["EntryHall"] = "null"
roomSouth       ["EntryHall"] = "null"
roomWest        ["EntryHall"] = "null"
roomUp          ["EntryHall"] = "null"
roomDown        ["EntryHall"] = "null"
roomItems       ["EntryHall"] = ["key", "candle", "candle"]

roomStatus      ["MainHall"] = 0
roomDescription ["MainHall"] = ["This a a description of the Main Hall."]
roomNorth       ["MainHall"] = "DiningHall"
roomEast        ["MainHall"] = "null"
roomSouth       ["MainHall"] = "EntryHall"
roomWest        ["MainHall"] = "Library"
roomUp          ["MainHall"] = "CentralLanding"
roomDown        ["MainHall"] = "null"
roomItems       ["MainHall"] = []

roomStatus      ["DiningHall"] = 0
roomDescription ["DiningHall"] = ["This a a description of the Dining Hall."]
roomNorth       ["DiningHall"] = "Solarium"
roomEast        ["DiningHall"] = "ServiceArea"
roomSouth       ["DiningHall"] = "MainHall"
roomWest        ["DiningHall"] = "null"
roomUp          ["DiningHall"] = "null"
roomDown        ["DiningHall"] = "null"
roomItems       ["DiningHall"] = []

roomStatus      ["ServiceArea"] = 0
roomDescription ["ServiceArea"] = ["This a a description of the Service Area."]
roomNorth       ["ServiceArea"] = "null"
roomEast        ["ServiceArea"] = "ServantsHall"
roomSouth       ["ServiceArea"] = "null"
roomWest        ["ServiceArea"] = "DiningHall"
roomUp          ["ServiceArea"] = "null"
roomDown        ["ServiceArea"] = "ServantsStairs"
roomItems       ["ServiceArea"] = []

roomStatus      ["Library"] = 0
roomDescription ["Library"] = ["This a a description of the Library."]
roomNorth       ["Library"] = "HiddenRoom"
roomEast        ["Library"] = "MainHall"
roomSouth       ["Library"] = "Study"
roomWest        ["Library"] = "null"
roomUp          ["Library"] = "null"
roomDown        ["Library"] = "null"
roomItems       ["Library"] = []

roomStatus      ["Study"] = 0
roomDescription ["Study"] = ["This a a description of the Study."]
roomNorth       ["Study"] = "Library"
roomEast        ["Study"] = "null"
roomSouth       ["Study"] = "EntryHall"
roomWest        ["Study"] = "Library"
roomUp          ["Study"] = "null"
roomDown        ["Study"] = "null"
roomItems       ["Study"] = []

roomStatus      ["HiddenRoom"] = 0
roomDescription ["HiddenRoom"] = ["This a a description of the Hidden Room."]
roomNorth       ["HiddenRoom"] = "null"
roomEast        ["HiddenRoom"] = "null"
roomSouth       ["HiddenRoom"] = "null"
roomWest        ["HiddenRoom"] = "null"
roomUp          ["HiddenRoom"] = "null"
roomDown        ["HiddenRoom"] = "null"
roomItems       ["HiddenRoom"] = []

## First Floor

roomStatus      ["CentralLanding"] = 0
roomDescription ["CentralLanding"] = ["This a a description of the Central Landing."]
roomNorth       ["CentralLanding"] = "null"
roomEast        ["CentralLanding"] = "null"
roomSouth       ["CentralLanding"] = "null"
roomWest        ["CentralLanding"] = "null"
roomUp          ["CentralLanding"] = "null"
roomDown        ["CentralLanding"] = "MainHall"
roomItems       ["CentralLanding"] = []

itemList = []
currentRoom = "FrontDoor"




def addToList(item):
        
    try:
        if playerTarget == "all":
            itemList.extend(roomItems[currentRoom])
            roomItems[currentRoom].clear()
        else:
            itemList.  append(roomItems[currentRoom].  pop(  roomItems.get(currentRoom).  index(playerTarget)))
    except:
        print (playerTarget + " cannot be taken.")

def removeFromList(item):
    try:
        if playerTarget == "all":
            roomItems[currentRoom].extend (itemList)
            itemList.clear()
        else:
            roomItems[currentRoom].  append(itemList.  pop(  itemList.  index(playerTarget  )))
    except:
        print ("You do not have a " + playerTarget + ".")
        
def printInventory():
    itemList.sort()
    for i, item in enumerate(itemList):
        if itemList[i] != itemList[i-1]:
            print (str(itemList.count(item)) + "x " + item)
        elif i==0:
            print (str(itemList.count(item)) + "x " + item)

def look():
    print (roomDescription[currentRoom][roomStatus[currentRoom]])
    roomItems[currentRoom].sort()
    for i, item in enumerate(roomItems[currentRoom]):
        if roomItems[currentRoom][i] != roomItems[currentRoom][i-1]:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)
        elif i==0:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)



def go(direction):
    targetRoom = currentRoom
    if direction == "north":
        if roomNorth[currentRoom] != "null":
            targetRoom = roomNorth[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    elif direction == "east":
        if roomEast[currentRoom] != "null":
            targetRoom = roomEast[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    elif direction == "south":
        if roomSouth[currentRoom] != "null":
            targetRoom = roomSouth[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    elif direction == "west":
        if roomWest[currentRoom] != "null":
            targetRoom = roomWest[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    elif direction == "up":
        if roomUp[currentRoom] != "null":
            targetRoom = roomUp[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    elif direction == "down":
        if roomDown[currentRoom] != "null":
            targetRoom = roomDown[currentRoom]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
        else:
            print ("You cannot go that way.")
    else:
            print ("That is not a proper direction.")
    return targetRoom
            



        




while True:
    try:
        playerInput = input()+" "
        playerInput.lower ()
        playerInputSplit = playerInput.split(" ")
     
        playerAction = "null"
        playerTarget = "null"
        
        if playerInputSplit[0] in actionDictionary:
            playerAction = actionDictionary[playerInputSplit[0]]
        elif playerInputSplit[0] in directionDictionary:
            playerAction = directionDictionary[playerInputSplit[0]]
    
        if playerInputSplit[1] in itemDictionary:
            playerTarget = itemDictionary[playerInputSplit[1]]
        elif playerInputSplit[1] in directionDictionary:
            playerTarget = directionDictionary[playerInputSplit[1]]


            

        
        if playerAction == "take":
            addToList(playerAction)
            
        if playerAction == "drop":
            removeFromList(playerAction)

        if playerAction == "use":
            ## room specific item usage checks

        if playerAction == "inventory":
            printInventory()

        if playerAction == "go" and playerTarget in directionDictionary:
            currentRoom = go(playerTarget)
        if playerAction in directionDictionary:
            currentRoom = go(playerAction)

        if playerAction[0] == "look":
            look()
            
        if playerAction[0] == "save":
            ## save roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)

        if playerAction[0] == "load":            
            ## load roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)
            
        if playerAction[0] == "quit":            
            ## end the game

    except:
        print ("That was not a recognised action.")
