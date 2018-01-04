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
roomDescription ["WineCellar"] = ["This is a description of the Wine Cellar."]
roomNorth       ["WineCellar"] = ["EntryHall"]
roomEast        ["WineCellar"] = ["null"]
roomSouth       ["WineCellar"] = ["null"]
roomWest        ["WineCellar"] = ["null"]
roomUp          ["WineCellar"] = ["null"]
roomDown        ["WineCellar"] = ["null"]
roomItems       ["WineCellar"] = []
roomInteractive ["WineCellar"] = {}

roomStatus      ["Kitchen"] = 0
roomDescription ["Kitchen"] = ["This is a description of the Kitchen."]
roomNorth       ["Kitchen"] = ["ServantsStairs"]
roomEast        ["Kitchen"] = ["DarkHallway"]
roomSouth       ["Kitchen"] = ["Pantry"]
roomWest        ["Kitchen"] = ["null"]
roomUp          ["Kitchen"] = ["null"]
roomDown        ["Kitchen"] = ["null"]
roomItems       ["Kitchen"] = []
roomInteractive ["Kitchen"] = {}

roomStatus      ["Pantry"] = 0
roomDescription ["Pantry"] = ["This is a description of the Pantry when the player falls in from above.", "This is a description of the pantry."]
roomNorth       ["Pantry"] = ["null", "Kitchen"]
roomEast        ["Pantry"] = ["null", "null"]
roomSouth       ["Pantry"] = ["null", "null"]
roomWest        ["Pantry"] = ["null", "null"]
roomUp          ["Pantry"] = ["null", "null"]
roomDown        ["Pantry"] = ["null", "null"]
roomItems       ["Pantry"] = []
roomInteractive ["Pantry"] = {}

roomStatus      ["DarkHallway"] = 0
roomDescription ["DarkHallway"] = ["This is a description of the Dark Hallway.", "This is a description of the Dark Hallway after the lamp has been used."]
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
roomDescription ["ServantsStairs"] = ["This is a description of the Servants Stairs."]
roomNorth       ["ServantsStairs"] = ["null"]
roomEast        ["ServantsStairs"] = ["null"]
roomSouth       ["ServantsStairs"] = ["null"]
roomWest        ["ServantsStairs"] = ["null"]
roomUp          ["ServantsStairs"] = ["ServiceArea"]
roomDown        ["ServantsStairs"] = ["Kitchen"]
roomItems       ["ServantsStairs"] = []
roomInteractive ["ServantsStairs"] = {}

roomStatus      ["ShadowStairs"] = 0
roomDescription ["ShadowStairs"] = ["This is a description of the Shadow Stairs."]
roomNorth       ["ShadowStairs"] = ["null"]
roomEast        ["ShadowStairs"] = ["null"]
roomSouth       ["ShadowStairs"] = ["null"]
roomWest        ["ShadowStairs"] = ["null"]
roomUp          ["ShadowStairs"] = ["ServantsHall3"]
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
roomItems       ["HeadOfHouseQuarters"] = []
roomInteractive ["HeadOfHouseQuarters"] = {}

roomStatus      ["ServantQuarters1"] = 0
roomDescription ["ServantQuarters1"] = ["This is a description of the Servants Quarters 1."]
roomNorth       ["ServantQuarters1"] = ["null"]
roomEast        ["ServantQuarters1"] = ["null"]
roomSouth       ["ServantQuarters1"] = ["null"]
roomWest        ["ServantQuarters1"] = ["ServantsHall2"]
roomUp          ["ServantQuarters1"] = ["null"]
roomDown        ["ServantQuarters1"] = ["null"]
roomItems       ["ServantQuarters1"] = []
roomInteractive ["ServantQuarters1"] = {}

roomStatus      ["ServantQuarters2"] = 0
roomDescription ["ServantQuarters2"] = ["This is a description of the Servants Quarters 2."]
roomNorth       ["ServantQuarters2"] = ["null"]
roomEast        ["ServantQuarters2"] = ["null"]
roomSouth       ["ServantQuarters2"] = ["null"]
roomWest        ["ServantQuarters2"] = ["ServantsHall3"]
roomUp          ["ServantQuarters2"] = ["null"]
roomDown        ["ServantQuarters2"] = ["null"]
roomItems       ["ServantQuarters2"] = []
roomInteractive ["ServantQuarters2"] = {}

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
roomItems       ["DiningHall"] = []
roomInteractive ["DiningHall"] = {}

roomStatus      ["ServiceArea"] = 0
roomDescription ["ServiceArea"] = ["This is a description of the Service Area."]
roomNorth       ["ServiceArea"] = ["null"]
roomEast        ["ServiceArea"] = ["ServantsHall1"]
roomSouth       ["ServiceArea"] = ["null"]
roomWest        ["ServiceArea"] = ["DiningHall"]
roomUp          ["ServiceArea"] = ["null"]
roomDown        ["ServiceArea"] = ["ServantsStairs"]
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

##The following rooms still need to added:
##Bedroom 1
##Bathroom 1
##Observatory
##Governess Quarters
##Nursery
##Cupboard 1
##Bathroom 2
##Master Bedroom
##Cupboard 2
##Bedroom 2

roomStatus      ["CentralLanding"] = 0
roomDescription ["CentralLanding"] = ["This is a description of the Central Landing."]
roomNorth       ["CentralLanding"] = ["null"]
roomEast        ["CentralLanding"] = ["null"]
roomSouth       ["CentralLanding"] = ["null"]
roomWest        ["CentralLanding"] = ["null"]
roomUp          ["CentralLanding"] = ["null"]
roomDown        ["CentralLanding"] = ["MainHall"]
roomItems       ["CentralLanding"] = []
roomInteractive ["CentralLanding"] = {}
