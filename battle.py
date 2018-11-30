from Character import *
from enemies import *
from userInput import *
from main import *
import random

def battle(Player):
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
    print("Wuh oh! You encountered a heckin' " + enemy.enemyName + "!")



