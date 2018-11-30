def userMovementInput():
#Returns Movement Input
    movementInput = input("Enter UP,DOWN,LEFT or RIGHT: ")
    movementInput = movementInput.upper()
    print(movementInput)
    while movementInput != "UP" and movementInput != "DOWN" and movementInput != "LEFT" and movementInput != "RIGHT":
        movementInput = input("TRY AGAIN: Enter UP,DOWN,LEFT or RIGHT: ")
        movementInput = movementInput.upper()
    return movementInput

def movementToCoodinates(x,y):
#Returns a Tuple With The New User Coordinates
    movementInput = userMovementInput()
    if movementInput == "UP":
        y+=1
    elif movementInput == "DOWN":
        y-=1
    elif movementInput == "LEFT":
        x-=1
    elif movementInput == "RIGHT":
        x+=1
    return x,y

def gameStartMenu():
    val = input("1. New Game\n2. Load Game\n3. Quit\n")
    val = int(val)
    while(val != 1 and val != 2 and val != 3):
        val = input("1. New Game\n2. Load Game\n3. Quit\n")
        val = int(val)
    return val

def userInGameMenu(inventoryDict):
#Returns 1 for Attack or Key From Inventory Menu
    menuInput = input("1. Attack\n2. Inventory: \n")
    while menuInput != "1" and menuInput != "2":
        menuInput = input("1. Attack\n2. Inventory: \n")
    if menuInput == "1":
        return 1
    elif menuInput == "2":
        return inventoryMenu(inventoryDict)

def inventoryMenu(inventoryDict):
#Returns the Key of the item in inventory
    print("Inventory: ",inventoryDict)
    inventorySelection = input("Input Name Of Item You Want To Use: ")
    if inventorySelection in inventoryDict:
        return inventorySelection
    else:
        while inventorySelection not in inventoryDict:
            inventorySelection = input("Erorr Not in Dict: Input Name Of Item You Want To Use: ")
        return inventorySelection


def mazeSizePrompt():
    val = input("Please enter difficulty\n1. Easy\n2. Normal\n3. Hard\n4. Very Hard\n5. Absolute Mad Lad\n")
    val = int(val)
    while(val != 1 and val != 2 and val != 3 and val != 4 and val != 5):
        val = ("Please enter difficulty\n1. Easy\n2. Normal\n3. Hard\n4. Very Hard\n5. Absolute Mad Lad\n")
        val = int(val)
    return val

def endMenu():
    val = input("1. Continue\n2. Save and Continue\n3. Save and Quit\n")
    val = int(val)
    while(val != 1 and val != 2 and val != 3):
        val = input("1. Continue\n2. Save and Continue\n3. Save and Quit\n")
        val = int(val)
    return val
