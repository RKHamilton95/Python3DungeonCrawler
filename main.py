from ASCIIArt import *
from Character import *
from userInput import *
from enemies import *
from maze import *
from enemies import *
from gameLoadSave import *

#Function definitions
def battle():
    choice = random.randrange(1,4)
    if(choice == 1):
        enemy = createTypeErrorPython()
    if(choice == 2):
        enemy = createSyntaxErrorPython()
    if(choice == 3):
        enemy = createValueErrorPython()
    if(choice == 4):
        enemy = createNameErrorPython()
    print(enemy.ascii)
    print("Wuh oh! You encountered a " + enemy.enemyName + "!")
    print(player.playerName + ": " + str(player.playerHealth) + "    " + enemy.enemyName + ": " + str(enemy.enemyHealth) + "\n")
    while(enemy.enemyHealth > 0):
        val = userInGameMenu(player.inventory.inventory)
        if(val == 1):
            #Player attacks
            damage = player.playerDoesDamage()
            enemy.damageEnemy(damage)
            verb = random.choice(["unleashes a mighty swing with", "lunges forward to stab with", "bashes with the hilt of"])
            print("\n--------------------------------------------\n")
            print(player.playerName + " " + verb + " their " + player.playerWeaponName + "!")
            print(enemy.enemyName + " takes " + str(damage) + " damage!")

            #Enemy attacks
            damage = enemy.doDamage()
            player.playerTakesDamage(damage)
            bodyPart = random.choice(["arm", "ankle", "nose", player.playerWeaponName, "helmet", "ear", "chest", "hand", "finger", "foot", "toe", "eye", "chin", "hip", "stomach", "scalp", "elbow", "knee", "shoulder", "forehead", "throat"])
            verb = random.choice(["takes a bite out of " + player.playerName + "'s " + bodyPart + "!", "whips " + player.playerName + "'s " + bodyPart + " with its tail!", "trips " + player.playerName + ", making them break their " + bodyPart + "!"])
            print(enemy.enemyName + " " + verb)
            print(player.playerName + " takes " + str(damage) + " damage!\n")
            print(player.playerName + ": " + str(player.playerHealth) + "    " + enemy.enemyName + ": " + str(enemy.enemyHealth) + "\n")
            print("--------------------------------------------")
        else:
            if(val == "Sword" or val == "Mace" or val == "Claymore" or val == "Axe"):
                print(player.playerName + " equips " + val + "!")
                player.playerSwitchesToWeapon(val)
            else:
                #Player Heals
                heal = player.healthPotionDict[val]
                player.playerHeals(heal)
                player.inventory.removeFromInventory(val)
                print(player.playerName + " uses " + val + "! " + str(heal) + " HP restored!")

                #Enemy attacks
                damage = enemy.doDamage()
                player.playerTakesDamage(damage)
                bodyPart = random.choice(["arm", "ankle", "nose", player.playerWeaponName, "helmet", "ear", "chest", "hand", "finger", "foot", "toe", "eye", "chin", "hip", "stomach", "scalp", "elbow", "knee", "shoulder", "forehead", "throat"])
                verb = random.choice(["takes a bite out of " + player.playerName + "'s " + bodyPart + "!", "whips " + player.playerName + "'s " + bodyPart + " with its tail!", "trips " + player.playerName + ", making them break their " + bodyPart + "!"])
                print(enemy.enemyName + " " + verb)
                print(player.playerName + " takes " + str(damage) + " damage!\n")
                print(player.playerName + ": " + str(player.playerHealth) + "    " + enemy.enemyName + ": " + str(enemy.enemyHealth) + "\n")


def processCoord():
    val = maze.movedTo
    if(val == "$"):
        choice = random.choice(["Sword", "Axe", "Mace", "Claymore", "Potion", "Great Potion", "Superior Potion", "Ultimate Potion"])
        player.inventory.addItemToInventory(choice)
        print(choice + " added to Inventory!\n")
    if(val == "&"):
        battle()

while(True):
    #Print title
    print(titleASCII)

    #Get menu choice
    choice = gameStartMenu()

    #New Game
    if(choice == 1):
        player = Player()
        player.setPlayerName()
        print(player)

    #Load Game
    if(choice == 2):
        player = loadPlayer(input("Input Player Name: "))
        print(player)

    #Exit
    if(choice == 3):
        exit()

    #Get Maze Difficulty
    size = mazeSizePrompt()

    #Create Maze
    maze = generateMaze(sizeDict[size])
    while(findPath(maze) == False):
        maze = generateMaze(sizeDict[size])

    #Game Flow
    count = 0
    stop_maze = False
    while(stop_maze == False):
        count+=1
        printMaze(maze)
        moved = mazeMove(maze, player, userMovementInput())
        if(moved):
            processCoord()
        if(maze.movedTo == "E"):
            stop_maze = True
    endVal = endMenu()
    if(endVal == 2 or endVal == 3):
        #Save Character
        savePlayer([player.playerName, player.playerHealth, player.playerDamage, player.playerWeaponName])
    if(endVal == 3):
        exit()
