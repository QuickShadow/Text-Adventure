list = []
def addToList(item):
    list.append(item)
    
def removeFromList(item):
    list.remove(item)

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4
directions = {}
directions_name = {}

def define_direction(number, name):
    if name in directions:
        print(name, " is already defined as, ", directions[name])
    directions[name] = number
    if not number in directions_name or (len(directions_name[number]) < len(name)):
        directions_name[number] = name


##while(True):
##    
##    action = input()
##    actionSteps = action.split(" ")
##    if actionSteps[0] == "take":
##        addToList(actionSteps[1])
##
##    if actionSteps[0] == "drop":
##        if list.count(actionSteps[1]) >0:
##            removeFromList(actionSteps[1])
##        else:
##            print("You do not have that.")
##        
##
##    if actionSteps[0] == "i":
##        list.sort()
##        print(list)

    
