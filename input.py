def userMovementInput():
    movementInput = input("Enter UP,DOWN,LEFT or RIGHT")
    movementInput.upper()
    while movementInput != "UP" | movementInput != "DOWN" | movementInput != "LEFT" | movementInput != "RIGHT":
        movementInput = input("TRY AGAIN: Enter UP,DOWN,LEFT or RIGHT")
        movementInput.upper()
    return movementInput

def movementToCoodinates(x,y):
    movementInput = userMovementInput
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
    menuInput = input("1. Attack","2. Inventory")
    while menuInput != "1" | menuInput != "2":
        menuInput = input("1. Attack","2. Inventory")
    if menuInput == "1":
        
    elif menuInput == "2":
        inventoryMenu(inventoryDict)
    
def inventoryMenu(inventoryDict):
    print("Inventory: ",inventoryDict)
    inventorySelection = input()

