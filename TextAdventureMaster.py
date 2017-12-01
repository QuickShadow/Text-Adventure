import TextAdventureRooms

roomStatus      = TextAdventureRooms.roomStatus
roomDescription = TextAdventureRooms.roomDescription
roomNorth       = TextAdventureRooms.roomNorth
roomEast        = TextAdventureRooms.roomEast
roomSouth       = TextAdventureRooms.roomSouth
roomWest        = TextAdventureRooms.roomWest
roomUp          = TextAdventureRooms.roomUp
roomDown        = TextAdventureRooms.roomDown
roomItems       = TextAdventureRooms.roomItems
roomInteractive = TextAdventureRooms.roomInteractive

##This Dictionary is used to change the player input into key words
actionDictionary = {}
actionDictionary ["take"] = "take"
actionDictionary ["get"] = "take"
actionDictionary ["drop"] = "drop"
actionDictionary ["read"] = "use"
actionDictionary ["use"] = "use"
actionDictionary ["light"] = "use"
actionDictionary ["place"] = "use"
actionDictionary ["search"] = "use"
actionDictionary ["unlock"] = "use"
actionDictionary ["go"] = "go"
actionDictionary ["move"] = "go"
actionDictionary ["quit"] = "quit"
actionDictionary ["q"] = "quit"
actionDictionary ["end"] = "quit"
actionDictionary ["search"] = "look"
actionDictionary ["look"] = "look"
actionDictionary ["l"] = "look"
actionDictionary ["save"] = "save"
actionDictionary ["load"] = "load"
actionDictionary ["i"] = "inventory"
actionDictionary ["inventory"] = "inventory"

##This Dictionary is used to change the player input into cardinal directions
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

##This Dictionary os used to change the player input into item names
itemDictionary = {}
itemDictionary ["all"]= "all"
itemDictionary ["candle"]= "candle"
itemDictionary ["journal"] = "journal"
itemDictionary ["book"] = "journal"
itemDictionary ["desk"] = "desk"
itemDictionary ["diary"] = "diary"
itemDictionary ["ladder"]= "ladder"
itemDictionary ["lamp"] = "lamp"
itemDictionary ["letter"] = "letter"
itemDictionary ["key"] = "key"
itemDictionary ["telescope"] = "telescope"
itemDictionary ["match"] = "match"
itemDictionary ["matches"] = "match"
itemDictionary ["matchbox"] = "match"

itemList = ["letter"]
currentRoom = "FrontDoor"



## These definitions link actions to key word subroutines

def addToList(item):
## Looks for the target item in the current room and adds it to the player inventory, removing it from the room inventory.
    try:
        if playerTarget == "all":
            itemList.extend(roomItems[currentRoom])
            roomItems[currentRoom].clear()
        else:
            itemList.  append(roomItems[currentRoom].  pop(  roomItems.get(currentRoom).  index(playerTarget)))
    except:
        print (playerTarget + " cannot be taken.")


def removeFromList(item):
## Looks for the target item in the player inventory and adds it to the room inventory, removing it from the player inventory.
    try:
        if playerTarget == "all":
            roomItems[currentRoom].extend (itemList)
            itemList.clear()
        else:
            roomItems[currentRoom].  append(itemList.  pop(  itemList.  index(playerTarget  )))
    except:
        print ("You do not have a " + playerTarget + ".")

        
def printInventory():
## Puts the player inventory into alphabetical order and then prints the contents, showing multiples of an object as a stack.
    itemList.sort()
    for i, item in enumerate(itemList):
        if itemList[i] != itemList[i-1]:
            print (str(itemList.count(item)) + "x " + item)
        elif i==0:
            print (str(itemList.count(item)) + "x " + item)


def look():
## Prints the description of the current room, alphabetises the room inventory and prints the contents, showing multiples of an object as a stack.
    print (roomDescription[currentRoom][roomStatus[currentRoom]])
    roomItems[currentRoom].sort()
    for i, item in enumerate(roomItems[currentRoom]):
        if roomItems[currentRoom][i] != roomItems[currentRoom][i-1]:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)
        elif i==0:
            print (str(roomItems[currentRoom].count(item)) + "x " + item)



def go(direction):
## Returns the next room to move to after checking there is a room in the chosen direction of travel and prints the description for that room.
## Checks destination rooms accounting for the current status of the room as this can alter the available options.
    targetRoom = currentRoom
    if direction == "north":
        if roomNorth[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomNorth[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "east":
        if roomEast[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomEast[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "south":
        if roomSouth[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomSouth[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "west":
        if roomWest[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomWest[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "up":
        if roomUp[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomUp[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "down":
        if roomDown[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomDown[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    else:
            print ("You cannot go that way.")
    return targetRoom
            


def useItem(item):
    if item == "letter":
        print ("You take the letter from your pocket and read it.")
        
    elif item == "ladder" and currentRoom == "ServantsHall2":
        print ("You place the ladder across the gap in the floor, forming a bridge.")
        [roomStatus["ServantsHall2"]] = 2


##itemDictionary ["candle"]= "candle"
##itemDictionary ["journal"] = "journal"
##itemDictionary ["book"] = "journal"
##itemDictionary ["diary"] = "diary"
##itemDictionary ["ladder"]= 
##itemDictionary ["lamp"] = "lamp"
##itemDictionary ["letter"] = 
##itemDictionary ["key"] = "key"
##itemDictionary ["telescope"] = "telescope"
##itemDictionary ["match"] = "match"
##itemDictionary ["matches"] = "match"
##itemDictionary ["matchbox"] = "match"

while True:
## Main code loop
    ##try:
    ## Takes player input and changes it to lower case before splitting into seperate pieces at a SPACE character
    playerInput = input()+" "
    playerInput.lower ()
    playerInputSplit = playerInput.split(" ")
 
    playerAction = "null"
    playerTarget = "null"

    ## Passes the seperate pieces of the player input through the Dictionaries to match with key words
    if playerInputSplit[0] in actionDictionary:
        playerAction = actionDictionary[playerInputSplit[0]]
    elif playerInputSplit[0] in directionDictionary:
        playerAction = directionDictionary[playerInputSplit[0]]

    if playerInputSplit[1] in itemDictionary:
        playerTarget = itemDictionary[playerInputSplit[1]]
    elif playerInputSplit[1] in directionDictionary:
        playerTarget = directionDictionary[playerInputSplit[1]]
        

    ## Calls defined actions depending on the player input.
    if playerAction == "take":
        addToList(playerTarget)
        
    if playerAction == "drop":
        removeFromList(playerTarget)

    ##if playerAction == "use":
    ##    if playerTarget in itemList[] || playerTarget in roomItems[currentRoom] || playerTarget in roomInteractive[currentRoom]:
    ##        useItem(playerTarget)
    
    if playerAction == "inventory":
        printInventory()

    if playerAction == "go" and playerTarget in directionDictionary:
        currentRoom = go(playerTarget)
    if playerAction in directionDictionary:
        currentRoom = go(playerAction)

    if playerAction == "look":
        look()
        
    if playerAction == "save":
        ## TO DO: save roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)
        pass
    
    if playerAction == "load":            
        ## TO DO: load roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)
        pass
    
    if playerAction == "quit":            
        ## TO DO: end the game
        pass
    ##except:
    ##    print ("That was not a recognised action.")



##Passive room status updates
    if currentRoom == "Pantry" and roomStatus["Pantry"] == 0:
        roomStatus["Pantry"]=1
        roomStatus["ServantsHall2"]=1
