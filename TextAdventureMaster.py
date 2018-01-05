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
actionDictionary ["open"] = "use"
actionDictionary ["place"] = "use"
actionDictionary ["search"] = "use"
actionDictionary ["unlock"] = "use"
actionDictionary ["go"] = "go"
actionDictionary ["move"] = "go"
actionDictionary ["quit"] = "quit"
actionDictionary ["q"] = "quit"
actionDictionary ["end"] = "quit"
actionDictionary ["examine"] = "look"
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

##This Dictionary is used to change the player input into item names
itemDictionary = {}
itemDictionary ["null"] = "null" ## is used to return no object defined
itemDictionary ["all"] = "all"
itemDictionary ["room"] = "room"
itemDictionary ["candle"] = "candle"
itemDictionary ["candles"] = "candle"
itemDictionary ["journal"] = "journal"
itemDictionary ["book"] = "journal"
itemDictionary ["desk"] = "desk"
itemDictionary ["drawer"] = "drawer"
itemDictionary ["diary"] = "diary"
itemDictionary ["ladder"]= "ladder"
itemDictionary ["lamp"] = "lamp"
itemDictionary ["letter"] = "letter"
itemDictionary ["key"] = "key"
itemDictionary ["telescope"] = "telescope"
itemDictionary ["match"] = "match"
itemDictionary ["matches"] = "match"
itemDictionary ["matchbox"] = "match"
itemDictionary ["starch"] = "starch"

##This Dictionary contains the descriptions of all items in the game for use with the look/examine command
itemDescription = {}
itemDescription ["candle"] =    "A large white wax and tallow candle"
itemDescription ["journal"] =   "A handwritten log of science experiments into the nature of arcane energy.\nThe name on the cover reads M.G. Callaghan."
itemDescription ["desk"] =      "This sturdy wooden desk has not been moved in some time.\nIt is covered in scraps of paper and random notes, and has a drawer built into it on one side."
itemDescription ["drawer"] =    "A plain wooden drawer."
itemDescription ["diary"] =     "A handwritten diary kept by one of the servants."
itemDescription ["ladder"]=     "An old wooden ladder."
itemDescription ["lamp"] =      "A brass bedside lamp with a wick and paraffin burner."
itemDescription ["letter"] =    "The letter from your dear friend Marcus Callaghan which brought you here."
itemDescription ["key"] =       "A heavy brass keyring with a couple of keys on it."
itemDescription ["telescope"] = "An ornate telescope that seems to have been modified with extra lenses.\nA power cable runs from it into the floor."
itemDescription ["match"] =     "A cardboard matchbox full of long matches with a striker on the outside of the box."
itemDescription ["starch"] =    "A damp box of starch flakes used for laundry."

##These variables set the starting condition of the game
itemList = ["letter"]
currentRoom = "FrontDoor"

##Import string for ASCii character strings
import string
##Import random for random number generator
import random
##Create a 6 digit random string
planet = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

print (planet)


## These definitions link actions to key word subroutines

def addToList(targetItem):
## Checks for the target item in the current room and adds it to the player inventory, removing it from the room inventory.
    try:
        if targetItem == "all":
            itemList.extend(roomItems[currentRoom])
            roomItems[currentRoom].clear()
        else:
            itemList.append(roomItems[currentRoom].pop(roomItems.get(currentRoom).index(targetItem)))
    except:
        print (targetItem + " cannot be taken.")


def removeFromList(targetItem):
## Checks for the target item in the player inventory and adds it to the room inventory, removing it from the player inventory.
    try:
        if targetItem == "all":
            roomItems[currentRoom].extend (itemList)
            itemList.clear()
        else:
            roomItems[currentRoom].append(itemList.pop(itemList.index(targetItem)))
    except:
        print ("You do not have a " + targetItem + ".")

        
def printInventory():
## Puts the player inventory into alphabetical order and then prints the contents, showing multiples of an object as a stack.
    itemList.sort()
    for i, item in enumerate(itemList):
        if itemList[i] != itemList[i-1]:
            print (str(itemList.count(item)) + "x " + item)
        elif i==0:
            print (str(itemList.count(item)) + "x " + item)


def look(targetItem):
    try:
        if playerTarget == "room" or playerTarget == "null":
## Prints the description of the current room, alphabetises the room inventory and prints the contents, showing multiples of an object as a stack.
            print (roomDescription[currentRoom][roomStatus[currentRoom]])
            roomItems[currentRoom].sort()
            for i, item in enumerate(roomItems[currentRoom]):
                if roomItems[currentRoom][i] != roomItems[currentRoom][i-1]:
                    print (str(roomItems[currentRoom].count(item)) + "x " + item)
                elif i==0:
                    print (str(roomItems[currentRoom].count(item)) + "x " + item)
## Prints the description of the target item
        else:
            print (itemDescription[playerTarget]) 
    except:
            pass


def go(direction):
## Returns the next room to move to after checking there is a room in the chosen direction of travel and prints the description for that room.
## Checks destination rooms accounting for the current status of the room as this can alter the available options.
    targetRoom = currentRoom
    ##checks if a match has been lit and removes it from the inventory if it exists.
    if "lit match" in itemList:
        itemList.remove("lit match")
        print ("The lit match burns out as you start to move around the room")
    if direction == "north" and roomNorth[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomNorth[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "east" and roomEast[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomEast[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "south" and roomSouth[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomSouth[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "west" and roomWest[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomWest[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "up" and roomUp[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomUp[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    elif direction == "down" and roomDown[currentRoom][roomStatus[currentRoom]] != "null":
            targetRoom = roomDown[currentRoom][roomStatus[currentRoom]]
            print (roomDescription[targetRoom][roomStatus[targetRoom]])
    else:
            print ("You cannot go " + direction + ".")
    return targetRoom
            


def useItem(item):
    if item == "letter":
        print ("You take the letter from your pocket and read it.\n'Dearest friend, I write to you on the eve of a great discovery.\nAs strange as the following may seem I assure you it is all true.\nBy combining knowledge from certain texts and my own scientific studies, I have managed to harness energy from a far off star.\nAfter writing this I will attempt the final phase of opening a link to that energy before sharing my discovery with the world.\nJust imagine a new era of unlimited electricity!  The inventions we could create without the constant need for giant steam engines!\nI beg you to come and visit, to see this new marvel for yourself,\n\nyours faithfully,\nMarcus")
        
    elif item == "ladder" and currentRoom == "ServantsHall2":
        print ("You place the ladder across the gap in the floor, forming a bridge.")
        [roomStatus["ServantsHall2"]] = 2
        itemList.remove("ladder")
        
    elif item == "drawer":
        ## Opens and closes drawers
        if roomInteractive[currentRoom]["drawer"]=="default":
            ## Adds the Journal to available items the first time the study drawer is opened
            if currentRoom == "Study":
                print ("You open the drawer.\nThere is a worn leather journal here.")
                roomItems[currentRoom].append("journal")
            ## Adds the Diary to available items the first time the servants quarters 2 drawer is opened
            elif currentRoom == "ServantQuarters2":
                print ("You open the drawer.\nYou find a small book inside, it looks like a diary.")
                roomItems[currentRoom].append("diary")
            else:
                print ("You open the drawer.\nThe drawer is empty.")
            roomInteractive[currentRoom]["drawer"]="open"
            
        elif roomInteractive[currentRoom]["drawer"]=="open":
            print ("You close the drawer.")
            roomInteractive[currentRoom]["drawer"]="closed"
        elif roomInteractive[currentRoom]["drawer"]=="closed":
            print ("You open the drawer.\nThe drawer is empty.")
            roomInteractive[currentRoom]["drawer"]="open"

    elif item == "match":
        if "lit match" not in itemList:
            itemList.append("lit match")
            print ("You strike a fresh match on the side of the box and a small flame springs to life.")
        elif "lit match" in itemList:
            print ("You already have a lit match.")
        ##Matches burn out on movement commands

    elif item == "candle":
        ##Determines wether to place a candle or light it, then checks for a lit match in the player inventory.
        if currentRoom == "WineCellar" and "candle" in itemList:
            roomInteractive["WineCellar"]["candle"] += 1
            itemList.remove("candle")
            if roomInteractive["WineCellar"]["candle"] == 1:
                print ("The first candle now sits in place at the edge of the strange image on the floor.")
            if roomInteractive["WineCellar"]["candle"] == 5:
                print ("All of the needed candles are set in place around the edge of the strange image on the floor.")
            elif roomInteractive["WineCellar"]["candle"] > 1:
                print ((str(roomInteractive[currentRoom]["candle"])) + " of the five candles now circle the strange image on the floor.")
        elif currentRoom == "WineCellar" and roomInteractive[currentRoom]["candle"] == 5 and roomInteractive[currentRoom]["circle"] == "fixed":
            if "lit match" in itemList:
                roomInteractive["WineCellar"]["candle"] += 1
                roomStatus["WineCellar"] = 1
                print ("As you light one of the candles, all five erupt into a pale green flame.\nThey burn more fiercely than should be possible for candles of this size.\nYou are one step closer to working out what happened here with the circle completed,\nbut a strange sense of being watched starts to creep over you.")
            else:
                print ("You have nothing to light the candles with.")
        elif "lit match" in itemList:
            print ("Touching the match to the candle wick brings forth a slow steady flame.\nAlmost immediately a strong gust of wind comes from nowhere and blows out the candle again.")
        else:
            print ("You have nothing to light the candle with.")

    elif item == "starch":
        if currentRoom == "WineCellar":
            roomInteractive[currentRoom]["circle"] = "fixed"
            itemList.remove("starch")
            print ("Using the last of the starch flakes you quickly complete the circle design laid out on the floor.\nThe symbol is now complete again.")

    elif item == "lamp" and currentRoom == "DarkHallway":
        if "lit match" in itemList:
            print ("Using the match to light the taper produces a soft yellowish glow.\nAlmost immediately a strong gust of wind comes from nowhere as if trying to blow out the light\nbut you quickly close the glass door on the lamp, protecting the flame.\nA handy nail on the wall provides a good place to hang the lamp by the handle, giving good light through the hallway.\nYou swear you could hear something hiss in the shadows and the sound of scuttering feet moving away from you.")
            itemList.remove("lamp")
            roomStatus["DarkHallway"] = 1
        else:
            print ("You have nothing to light the lamp with.")

    elif item == "key" and currentRoom == "ServantsStairs":
        print ("One of the keys fits the lock on the door, and it swings gently open revealing the service area at the back of the dining hall.")
        itemList.remove("key")
        roomStatus["ServiceArea"] = 1
        roomStatus["ServantsStairs"] = 1 

    elif item == "diary":
        print ("Flicking through the diary a couple of entries catch your eye.  The first is dated about a month ago:\n'  I was curious about the Masters experiments so I followed him on my afternoon off.\nI still have no clue what he was doing, but he's been spending a lot of time in the old observatory,\nand when I followed him into the library this evening he walked to the fire,\nand then vanished before I got around the corner.\nThere's definitely something strange going on...'\n\nThe second entry is only a few days old,\n'  I heard it again last night.  I don't care what they say that's no rat down there, it sounds huge.  I blocked the door just to be safe, but it seems to like the darkness down there...'")
        roomStatus["Library"] = 1

    elif item == "telescope":
        print ("You bend to look through the scope, but the view doesn't seem to be focused on anything.\nWhat would you like to look at?")
        viewTarget = input()
        viewTarget.upper
        if viewTarget == "MARS" or viewTarget == "JUPITER" or viewTarget == "SATURN" :
            print ("It takes a moment for you to find the planet, and slightly longer to understand what you are looking at.\nThe planets all seem to be lined up, eclipsing each other.")
        elif viewTarget == planet:
            print ("The small planet gleams brightly in the sky.  You wonder if it is getting brighter?\nA ray of light hits the telescope, lighting up the lenses before being focused into a device at the top of the cable.\nSoon after you hear the soft hum of an electric generator below you.")
            
        else:
            print (viewTarget + " is not visible from this telescope tonight.")
            roomInteractive[currentRoom]["telescope"] = "found"

    else:            
        print ("You cannot use that item here.")

##itemDictionary ["journal"] = "journal"



while True:
## Main code loop
    try:
        print()
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

        if playerAction == "use":
            if playerTarget in itemList or playerTarget in roomItems[currentRoom] or playerTarget in roomInteractive[currentRoom]:
                useItem(playerTarget)
    
        if playerAction == "inventory":
            printInventory()

        if playerAction == "go" and playerTarget in directionDictionary:
            currentRoom = go(playerTarget)
        if playerAction in directionDictionary:
            currentRoom = go(playerAction)

        if playerAction == "look":
            ## Checks the item is available
            if playerTarget in itemList or playerTarget in roomItems[currentRoom] or playerTarget in roomInteractive[currentRoom] or playerTarget == "room" or playerTarget =="null":
                look(playerTarget)
        
        if playerAction == "save":
            ## TO DO: save roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)
            pass
    
        if playerAction == "load":            
            ## TO DO: load roomStatus (dictionary), roomItems (dictionary), itemList (list), currentRoom (string)
            pass
        
        if playerAction == "quit":            
            ## TO DO: end the game
            pass

    except:
        print ("That was not a recognised action.")



##Passive room status updates
    if currentRoom == "Pantry" and roomStatus["Pantry"] == 0:
        roomStatus["Pantry"] = 1
        roomStatus["ServantsHall2"] = 1

    if  roomStatus["Solarium"] == 0 and roomInteractive["Observatory"]["telescope"] == "found" and roomStatus["WineCellar"] == 1:
        roomStatus["Solarium"] = 1
