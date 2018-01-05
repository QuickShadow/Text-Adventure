##These Dictionaries are used to define the attributes of the locations in the game
roomStatus      = {}
roomDescription = {}
roomNorth       = {}
roomEast        = {}
roomSouth       = {}
roomWest        = {}
roomUp          = {}
roomDown        = {}
roomItems       = {}
roomInteractive = {}
interactiveStatus = []


## Basement

roomStatus      ["HoHo1"] = 0
roomDescription ["HoHo1"] = ["This is a description of the Ho-Ho (West)."]
roomNorth       ["HoHo1"] = ["null"]
roomEast        ["HoHo1"] = ["HoHo2"]
roomSouth       ["HoHo1"] = ["GroundsKeepersOffice"]
roomWest        ["HoHo1"] = ["null"]
roomUp          ["HoHo1"] = ["null"]
roomDown        ["HoHo1"] = ["null"]
roomItems       ["HoHo1"] = []
roomInteractive ["HoHo1"] = {}

roomStatus      ["HoHo2"] = 0
roomDescription ["HoHo2"] = ["This is a description of the Ho-Ho (East)."]
roomNorth       ["HoHo2"] = ["HoHo1"]
roomEast        ["HoHo2"] = ["null"]
roomSouth       ["HoHo2"] = ["null"]
roomWest        ["HoHo2"] = ["DarkHallway"]
roomUp          ["HoHo2"] = ["null"]
roomDown        ["HoHo2"] = ["null"]
roomItems       ["HoHo2"] = []
roomInteractive ["HoHo2"] = {}

roomStatus      ["GroundsKeepersOffice"] = 0
roomDescription ["GroundsKeepersOffice"] = ["This is a description of the Grounds Keepers Office."]
roomNorth       ["GroundsKeepersOffice"] = ["HoHo1"]
roomEast        ["GroundsKeepersOffice"] = ["null"]
roomSouth       ["GroundsKeepersOffice"] = ["null"]
roomWest        ["GroundsKeepersOffice"] = ["null"]
roomUp          ["GroundsKeepersOffice"] = ["null"]
roomDown        ["GroundsKeepersOffice"] = ["null"]
roomItems       ["GroundsKeepersOffice"] = ["ladder"]
roomInteractive ["GroundsKeepersOffice"] = {}

roomStatus      ["WineCellar"] = 0
roomDescription ["WineCellar"] = ["This is a description of the Wine Cellar.", "This is a description of the Wine Cellar after the candles have been lit"]
roomNorth       ["WineCellar"] = ["EntryHall",  "EntryHall"]
roomEast        ["WineCellar"] = ["null",       "null"]
roomSouth       ["WineCellar"] = ["null",       "null"]
roomWest        ["WineCellar"] = ["null",       "null"]
roomUp          ["WineCellar"] = ["null",       "null"]
roomDown        ["WineCellar"] = ["null",       "null"]
roomItems       ["WineCellar"] = []
roomInteractive ["WineCellar"] = {"circle":"broken", "candle":0}

roomStatus      ["Kitchen"] = 0
roomDescription ["Kitchen"] = ["The large galley kitchen looks like it was abandoned halfway through a large meal being prepared.\nMarble sideboards are covered in food that has been left out for a few days, half chopped and half mouldy.\nA door in the north wall has stairs leading up just past it,\nand a door to the south leads back to the Pantry.\nA door in the east side leads out into a dark corridor."]
roomNorth       ["Kitchen"] = ["ServantsStairs"]
roomEast        ["Kitchen"] = ["DarkHallway"]
roomSouth       ["Kitchen"] = ["Pantry"]
roomWest        ["Kitchen"] = ["null"]
roomUp          ["Kitchen"] = ["null"]
roomDown        ["Kitchen"] = ["null"]
roomItems       ["Kitchen"] = ["match"]
roomInteractive ["Kitchen"] = {"drawer":"closed"}

roomStatus      ["Pantry"] = 0
roomDescription ["Pantry"] = ["The creaking floor finally gives way as you walk across it, taking the ground from beneath your feet.\nYou fall into the darkness below and it takes a moment for your head to stop spinning.\nLooking around you seem to have landed in the storage pantry for the main kitchen.\nFeeling slightly disorientated you hope you can find your way back upstairs.\nA door to the north seems to be the only way out.", "The large hole in the celing of the pantry serves as a reminder of your fall from the corridor above.\nThere seems to be a lot of food goods stored here, and the only door out on the north side leads out into the kitchen.\nThe door is open despite having a rather solid looking lock on it."]
roomNorth       ["Pantry"] = ["null", "Kitchen"]
roomEast        ["Pantry"] = ["null", "null"]
roomSouth       ["Pantry"] = ["null", "null"]
roomWest        ["Pantry"] = ["null", "null"]
roomUp          ["Pantry"] = ["null", "null"]
roomDown        ["Pantry"] = ["null", "null"]
roomItems       ["Pantry"] = ["key"]
roomInteractive ["Pantry"] = {}

roomStatus      ["DarkHallway"] = 0
roomDescription ["DarkHallway"] = ["The hallway is too dark to see where you are going.\nAfter a moment of trying to let your eyes adjust,you realise the only thing you can see is the kitchen doorway at the north end of the hall.", "By the lamplight you can see several doors leading from the hall.\nThe kitchen is at the left to the north,\na door to the east seems to lead outside,\nanother dim room to the west of the hall,\nand some stairs leading up at the south."]
roomNorth       ["DarkHallway"] = ["Kitchen", "Kitchen"]
roomEast        ["DarkHallway"] = ["null",    "HoHo2"]
roomSouth       ["DarkHallway"] = ["null",    "ShadowStairs"]
roomWest        ["DarkHallway"] = ["null",    "LaundryRoom"]
roomUp          ["DarkHallway"] = ["null",    "null"]
roomDown        ["DarkHallway"] = ["null",    "null"]
roomItems       ["DarkHallway"] = []
roomInteractive ["DarkHallway"] = {}

roomStatus      ["LaundryRoom"] = 0
roomDescription ["LaundryRoom"] = ["This is a description of the Laundry Room."]
roomNorth       ["LaundryRoom"] = ["null"]
roomEast        ["LaundryRoom"] = ["DarkHallway"]
roomSouth       ["LaundryRoom"] = ["null"]
roomWest        ["LaundryRoom"] = ["null"]
roomUp          ["LaundryRoom"] = ["null"]
roomDown        ["LaundryRoom"] = ["null"]
roomItems       ["LaundryRoom"] = ["starch"]
roomInteractive ["LaundryRoom"] = {}

##Stairs (Ground Floor to First Floor)

roomStatus      ["SecretStairs"] = 0
roomDescription ["SecretStairs"] = ["This is a description of the Secret Stairs."]
roomNorth       ["SecretStairs"] = ["null"]
roomEast        ["SecretStairs"] = ["null"]
roomSouth       ["SecretStairs"] = ["null"]
roomWest        ["SecretStairs"] = ["null"]
roomUp          ["SecretStairs"] = ["HiddenRoom"]
roomDown        ["SecretStairs"] = ["WineCellar"]
roomItems       ["SecretStairs"] = []
roomInteractive ["SecretStairs"] = {}

roomStatus      ["ServantsStairs"] = 0
roomDescription ["ServantsStairs"] = ["The servants stairs wind upwards through the back of the house coming to a small landing.\nA heavy door stands at the top, firmly dividing the staff area and the family area with a solid lock.\nThe only other way is back down to the kitchen.","The servants stairs wind through the back wall of the building with the service area up at the top\nand the main galley kitchen down at the bottom."]
roomNorth       ["ServantsStairs"] = ["null",       "null"]
roomEast        ["ServantsStairs"] = ["null",       "null"]
roomSouth       ["ServantsStairs"] = ["null",       "null"]
roomWest        ["ServantsStairs"] = ["null",       "null"]
roomUp          ["ServantsStairs"] = ["null",       "ServiceArea"]
roomDown        ["ServantsStairs"] = ["Kitchen",    "Kitchen"]
roomItems       ["ServantsStairs"] = []
roomInteractive ["ServantsStairs"] = {}

roomStatus      ["ShadowStairs"] = 0
roomDescription ["ShadowStairs"] = ["These stairs lead upwards, but come to an abrupt end at a door.\nIt seems to have been barricaded from the other side.\nThere is nowhere to go but back down to the hall."]
roomNorth       ["ShadowStairs"] = ["null"]
roomEast        ["ShadowStairs"] = ["null"]
roomSouth       ["ShadowStairs"] = ["null"]
roomWest        ["ShadowStairs"] = ["null"]
roomUp          ["ShadowStairs"] = ["null"]
roomDown        ["ShadowStairs"] = ["DarkHallway"]
roomItems       ["ShadowStairs"] = []
roomInteractive ["ShadowStairs"] = {}

## Ground Floor

roomStatus      ["Solarium"] = 0
roomDescription ["Solarium"] = ["This is a description of the Solarium.", "This is a description of the Solarium after the portal has been activated." ]
roomNorth       ["Solarium"] = ["null", "???"]
roomEast        ["Solarium"] = ["null", "null"]
roomSouth       ["Solarium"] = ["DiningHall", "DiningHall"]
roomWest        ["Solarium"] = ["null", "null"]
roomUp          ["Solarium"] = ["null", "null"]
roomDown        ["Solarium"] = ["null", "null"]
roomItems       ["Solarium"] = []
roomInteractive ["Solarium"] = {}

roomStatus      ["HeadOfHouseQuarters"] = 0
roomDescription ["HeadOfHouseQuarters"] = ["This is a description of the Head of House Quarters."]
roomNorth       ["HeadOfHouseQuarters"] = ["null"]
roomEast        ["HeadOfHouseQuarters"] = ["null"]
roomSouth       ["HeadOfHouseQuarters"] = ["null"]
roomWest        ["HeadOfHouseQuarters"] = ["ServantsHall1"]
roomUp          ["HeadOfHouseQuarters"] = ["null"]
roomDown        ["HeadOfHouseQuarters"] = ["null"]
roomItems       ["HeadOfHouseQuarters"] = ["candle"]
roomInteractive ["HeadOfHouseQuarters"] = {"drawer":"closed"}

roomStatus      ["ServantQuarters1"] = 0
roomDescription ["ServantQuarters1"] = ["This is a description of the Servants Quarters 1."]
roomNorth       ["ServantQuarters1"] = ["null"]
roomEast        ["ServantQuarters1"] = ["null"]
roomSouth       ["ServantQuarters1"] = ["null"]
roomWest        ["ServantQuarters1"] = ["ServantsHall2"]
roomUp          ["ServantQuarters1"] = ["null"]
roomDown        ["ServantQuarters1"] = ["null"]
roomItems       ["ServantQuarters1"] = []
roomInteractive ["ServantQuarters1"] = {"drawer":"closed"}

roomStatus      ["ServantQuarters2"] = 0
roomDescription ["ServantQuarters2"] = ["This is a description of the Servants Quarters 2."]
roomNorth       ["ServantQuarters2"] = ["null"]
roomEast        ["ServantQuarters2"] = ["null"]
roomSouth       ["ServantQuarters2"] = ["null"]
roomWest        ["ServantQuarters2"] = ["ServantsHall3"]
roomUp          ["ServantQuarters2"] = ["null"]
roomDown        ["ServantQuarters2"] = ["null"]
roomItems       ["ServantQuarters2"] = []
roomInteractive ["ServantQuarters2"] = {"drawer":"default"}

roomStatus      ["FrontDoor"] = 0
roomDescription ["FrontDoor"] = ["This is a description of the Front Door."]
roomNorth       ["FrontDoor"] = ["EntryHall"]
roomEast        ["FrontDoor"] = ["null"]
roomSouth       ["FrontDoor"] = ["null"]
roomWest        ["FrontDoor"] = ["null"]
roomUp          ["FrontDoor"] = ["null"]
roomDown        ["FrontDoor"] = ["null"]
roomItems       ["FrontDoor"] = []
roomInteractive ["FrontDoor"] = {}

roomStatus      ["EntryHall"] = 0
roomDescription ["EntryHall"] = ["This is a description of the Entry Hall."]
roomNorth       ["EntryHall"] = ["MainHall"]
roomEast        ["EntryHall"] = ["null"]
roomSouth       ["EntryHall"] = ["null"]
roomWest        ["EntryHall"] = ["null"]
roomUp          ["EntryHall"] = ["null"]
roomDown        ["EntryHall"] = ["null"]
roomItems       ["EntryHall"] = []
roomInteractive ["EntryHall"] = {}

roomStatus      ["MainHall"] = 0
roomDescription ["MainHall"] = ["This is a description of the Main Hall."]
roomNorth       ["MainHall"] = ["DiningHall"]
roomEast        ["MainHall"] = ["null"]
roomSouth       ["MainHall"] = ["EntryHall"]
roomWest        ["MainHall"] = ["Library"]
roomUp          ["MainHall"] = ["CentralLanding"]
roomDown        ["MainHall"] = ["null"]
roomItems       ["MainHall"] = []
roomInteractive ["MainHall"] = {}

roomStatus      ["DiningHall"] = 0
roomDescription ["DiningHall"] = ["This is a description of the Dining Hall."]
roomNorth       ["DiningHall"] = ["Solarium"]
roomEast        ["DiningHall"] = ["ServiceArea"]
roomSouth       ["DiningHall"] = ["MainHall"]
roomWest        ["DiningHall"] = ["null"]
roomUp          ["DiningHall"] = ["null"]
roomDown        ["DiningHall"] = ["null"]
roomItems       ["DiningHall"] = ["candle"]
roomInteractive ["DiningHall"] = {}

roomStatus      ["ServiceArea"] = 0
roomDescription ["ServiceArea"] = ["This is a description of the Service Area.", "This is a description of the Service Area with the door unlocked."]
roomNorth       ["ServiceArea"] = ["null",          "null"]
roomEast        ["ServiceArea"] = ["ServantsHall",  "ServantsHall1"]
roomSouth       ["ServiceArea"] = ["null",          "null"]
roomWest        ["ServiceArea"] = ["DiningHall",    "DiningHall"]
roomUp          ["ServiceArea"] = ["null",          "null"]
roomDown        ["ServiceArea"] = ["null",          "ServantsStairs"]
roomItems       ["ServiceArea"] = []
roomInteractive ["ServiceArea"] = {}

roomStatus      ["ServantsHall1"] = 0
roomDescription ["ServantsHall1"] = ["This is a description of the Servants Hall 1."]
roomNorth       ["ServantsHall1"] = ["null"]
roomEast        ["ServantsHall1"] = ["HeadOfHouseQuarters"]
roomSouth       ["ServantsHall1"] = ["ServantsHall2"]
roomWest        ["ServantsHall1"] = ["ServiceArea"]
roomUp          ["ServantsHall1"] = ["null"]
roomDown        ["ServantsHall1"] = ["null"]
roomItems       ["ServantsHall1"] = []
roomInteractive ["ServantsHall1"] = {}

roomStatus      ["ServantsHall2"] = 0
roomDescription ["ServantsHall2"] = ["This is a description of the Servants Hall 2.", "This is a description of the Servants Hall 2 after the floor collapses.", "This is a description of the Servants hall 2 after the LADDER is used."]
roomNorth       ["ServantsHall2"] = ["ServantsHall1",    "ServantsHall1",    "ServantsHall1"]
roomEast        ["ServantsHall2"] = ["ServantQuarters1", "ServantQuarters1", "ServantQuarters1"]
roomSouth       ["ServantsHall2"] = ["Pantry",           "null",             "ServantsHall3"]
roomWest        ["ServantsHall2"] = ["null",             "null",             "null"]
roomUp          ["ServantsHall2"] = ["null",             "null",             "null"]
roomDown        ["ServantsHall2"] = ["null",             "Pantry",           "Pantry"]
roomItems       ["ServantsHall2"] = []
roomInteractive ["ServantsHall2"] = {}

roomStatus      ["ServantsHall3"] = 0
roomDescription ["ServantsHall3"] = ["This is a description of the Servants Hall 3."]
roomNorth       ["ServantsHall3"] = ["ServantsHall2"]
roomEast        ["ServantsHall3"] = ["ServantQuarters2"]
roomSouth       ["ServantsHall3"] = ["null"]
roomWest        ["ServantsHall3"] = ["null"]
roomUp          ["ServantsHall3"] = ["null"]
roomDown        ["ServantsHall3"] = ["ShadowStairs"]
roomItems       ["ServantsHall3"] = []
roomInteractive ["ServantsHall3"] = {}

roomStatus      ["Library"] = 0
roomDescription ["Library"] = ["This is a description of the Library.", "This a a description of the Library after the DIARY has been found."]
roomNorth       ["Library"] = ["null",     "HiddenRoom"]
roomEast        ["Library"] = ["MainHall", "MainHall"]
roomSouth       ["Library"] = ["Study",    "Study"]
roomWest        ["Library"] = ["null",     "null"]
roomUp          ["Library"] = ["null",     "null"]
roomDown        ["Library"] = ["null",     "null"]
roomItems       ["Library"] = []
roomInteractive ["Library"] = {}

roomStatus      ["Study"] = 0
roomDescription ["Study"] = ["This is a description of the Study."]
roomNorth       ["Study"] = ["Library"]
roomEast        ["Study"] = ["null"]
roomSouth       ["Study"] = ["null"]
roomWest        ["Study"] = ["null"]
roomUp          ["Study"] = ["null"]
roomDown        ["Study"] = ["null"]
roomItems       ["Study"] = []
roomInteractive ["Study"] = {"desk":"", "drawer":"default"}


roomStatus      ["HiddenRoom"] = 0
roomDescription ["HiddenRoom"] = ["This is a description of the Hidden Room."]
roomNorth       ["HiddenRoom"] = ["null"]
roomEast        ["HiddenRoom"] = ["null"]
roomSouth       ["HiddenRoom"] = ["Library"]
roomWest        ["HiddenRoom"] = ["null"]
roomUp          ["HiddenRoom"] = ["null"]
roomDown        ["HiddenRoom"] = ["SecretStairs"]
roomItems       ["HiddenRoom"] = []
roomInteractive ["HiddenRoom"] = {}

## First Floor

roomStatus      ["CentralLanding"] = 0
roomDescription ["CentralLanding"] = ["This is a description of the Central Landing."]
roomNorth       ["CentralLanding"] = ["Observatory"]
roomEast        ["CentralLanding"] = ["EastLanding"]
roomSouth       ["CentralLanding"] = ["null"]
roomWest        ["CentralLanding"] = ["null"]
roomUp          ["CentralLanding"] = ["null"]
roomDown        ["CentralLanding"] = ["MainHall"]
roomItems       ["CentralLanding"] = []
roomInteractive ["CentralLanding"] = {}

roomStatus      ["EastLanding"] = 0
roomDescription ["EastLanding"] = ["This is a description of the East Landing."]
roomNorth       ["EastLanding"] = ["null"]
roomEast        ["EastLanding"] = ["Nursery"]
roomSouth       ["EastLanding"] = ["GovernessQuarters"]
roomWest        ["EastLanding"] = ["CentralLanding"]
roomUp          ["EastLanding"] = ["null"]
roomDown        ["EastLanding"] = ["null"]
roomItems       ["EastLanding"] = []
roomInteractive ["EastLanding"] = {}

roomStatus      ["WestLanding"] = 0
roomDescription ["WestLanding"] = ["This is a description of the West Landing."]
roomNorth       ["WestLanding"] = ["Bedroom1"]
roomEast        ["WestLanding"] = ["CentralLanding"]
roomSouth       ["WestLanding"] = ["MasterBedroom"]
roomWest        ["WestLanding"] = ["Bedroom2"]
roomUp          ["WestLanding"] = ["null"]
roomDown        ["WestLanding"] = ["null"]
roomItems       ["WestLanding"] = []
roomInteractive ["WestLanding"] = {}

roomStatus      ["Observatory"] = 0
roomDescription ["Observatory"] = ["This is a description of the Observatory."]
roomNorth       ["Observatory"] = ["null"]
roomEast        ["Observatory"] = ["null"]
roomSouth       ["Observatory"] = ["CentralLanding"]
roomWest        ["Observatory"] = ["null"]
roomUp          ["Observatory"] = ["null"]
roomDown        ["Observatory"] = ["null"]
roomItems       ["Observatory"] = []
roomInteractive ["Observatory"] = {"telescope":"looking"}

roomStatus      ["Bedroom1"] = 0
roomDescription ["Bedroom1"] = ["This is a description of Bedroom 1."]
roomNorth       ["Bedroom1"] = ["null"]
roomEast        ["Bedroom1"] = ["null"]
roomSouth       ["Bedroom1"] = ["WestLanding"]
roomWest        ["Bedroom1"] = ["null"]
roomUp          ["Bedroom1"] = ["null"]
roomDown        ["Bedroom1"] = ["null"]
roomItems       ["Bedroom1"] = ["candle"]
roomInteractive ["Bedroom1"] = {"drawer":"closed"}

roomStatus      ["Bedroom2"] = 0
roomDescription ["Bedroom2"] = ["This is a description of Bedroom 2."]
roomNorth       ["Bedroom2"] = ["null"]
roomEast        ["Bedroom2"] = ["WestLanding"]
roomSouth       ["Bedroom2"] = ["null"]
roomWest        ["Bedroom2"] = ["null"]
roomUp          ["Bedroom2"] = ["null"]
roomDown        ["Bedroom2"] = ["null"]
roomItems       ["Bedroom2"] = ["candle"]
roomInteractive ["Bedroom2"] = {"drawer":"closed"}

roomStatus      ["MasterBedroom"] = 0
roomDescription ["MasterBedroom"] = ["This is a description of the Master Bedroom."]
roomNorth       ["MasterBedroom"] = ["WestLanding"]
roomEast        ["MasterBedroom"] = ["null"]
roomSouth       ["MasterBedroom"] = ["null"]
roomWest        ["MasterBedroom"] = ["null"]
roomUp          ["MasterBedroom"] = ["null"]
roomDown        ["MasterBedroom"] = ["null"]
roomItems       ["MasterBedroom"] = ["lamp"]
roomInteractive ["MasterBedroom"] = {"drawer":"closed"}

roomStatus      ["Nursery"] = 0
roomDescription ["Nursery"] = ["This is a description of the Nursery."]
roomNorth       ["Nursery"] = ["null"]
roomEast        ["Nursery"] = ["null"]
roomSouth       ["Nursery"] = ["GovernessQuarters"]
roomWest        ["Nursery"] = ["EastLanding"]
roomUp          ["Nursery"] = ["null"]
roomDown        ["Nursery"] = ["null"]
roomItems       ["Nursery"] = []
roomInteractive ["Nursery"] = {}
roomStatus      ["Nursery"] = 0

roomDescription ["GovernessQuarters"] = ["This is a description of the Governess Quarters."]
roomNorth       ["GovernessQuarters"] = ["Nursery"]
roomEast        ["GovernessQuarters"] = ["null"]
roomSouth       ["GovernessQuarters"] = ["null"]
roomWest        ["GovernessQuarters"] = ["EastLanding"]
roomUp          ["GovernessQuarters"] = ["null"]
roomDown        ["GovernessQuarters"] = ["null"]
roomItems       ["GovernessQuarters"] = ["candle"]
roomInteractive ["GovernessQuarters"] = {"drawer":"closed"}

## Special Room

roomStatus      ["???"] = 0
roomDescription ["???"] = ["This is a description of ???."]
roomNorth       ["???"] = ["null"]
roomEast        ["???"] = ["null"]
roomSouth       ["???"] = ["null"]
roomWest        ["???"] = ["null"]
roomUp          ["???"] = ["null"]
roomDown        ["???"] = ["null"]
roomItems       ["???"] = []
roomInteractive ["???"] = {}
