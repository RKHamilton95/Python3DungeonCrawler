def userMovementInput():
#Returns Movement Input
    movementInput = input("Enter UP,DOWN,LEFT or RIGHT")
    movementInput.upper()
    while movementInput != "UP" | movementInput != "DOWN" | movementInput != "LEFT" | movementInput != "RIGHT":
        movementInput = input("TRY AGAIN: Enter UP,DOWN,LEFT or RIGHT")
        movementInput.upper()
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

def userMenu(inventoryDict):
#Returns 1 for Attack or Key From Inventory Menu
    menuInput = input("1. Attack","2. Inventory")
    while menuInput != "1" | menuInput != "2":
        menuInput = input("1. Attack","2. Inventory")
    if menuInput == "1":
        return "1"
    elif menuInput == "2":
        return inventoryMenu(inventoryDict)
    
def inventoryMenu(inventoryDict):
#Returns the Key of the item in inventory
    print("Inventory: ",inventoryDict)
    inventorySelection = input("Input Name Of Item You Want To Use")
    return inventorySelection

