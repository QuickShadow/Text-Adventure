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


roomEntryHall = {}
roomEntryHall ["description"] = "This a a description of the Entry Hall."
roomEntryHall ["north"] = "MainHall"
roomEntryHall ["east"] = "null"
roomEntryHall ["south"] = "null"
roomEntryHall ["west"] = "null"
roomEntryHall ["up"] = "null"
roomEntryHall ["down"] = "null"
itemEntryHall = ["key"]

roomMainHall = {}
roomMainHall ["description"] = "This a a description of the Main Hall."
roomMainHall ["north"] = "null"
roomMainHall ["east"] = "null"
roomMainHall ["south"] = "EntryHall"
roomMainHall ["west"] = "null"
roomMainHall ["up"] = "null"
roomMainHall ["down"] = "null"
itemMainHall = []

itemList = []


def addToList(item):
    itemList.append (itemEntryHall.pop(itemEntryHall.index(playerAction[1])))    

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
    playerInput.lower ()
                      
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



