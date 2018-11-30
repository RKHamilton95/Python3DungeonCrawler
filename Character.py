from ASCIIArt import *
import random

class Player(object):

    weaponDict = {"Sword": 7,"Axe": 9,"Mace":11,"Claymore": 13}
    healthPotionDict = {"Potion": 10,"Great Potion":20,"Superior Potion":50,"Ultimate Potion":100}

    def __init__(self):
        self.playerName = ""
        self.playerHealth = 100
        self.playerDamage = 5
        self.playerWeaponName = "fists"
        self.inventory = Inventory()
        self.coords = [0 , 0]

    def __str__(self):
        return "Name: "+self.playerName+"\n"+"Health: "+str(self.playerHealth)+"\n"+"Damage: "+str(self.playerDamage)+"\n"+"Player Weapon: "+self.playerWeaponName+"\n"

    #Functions
    def playerDoesDamage(self):
        return self.playerDamage + random.randrange(0 , self.playerDamage)

    #Getters
    def getPlayerHealth(self):
        return self.playerHealth

    def playerSwitchesToWeapon(self,weaponName):
        self.playerWeaponName = weaponName
        self.playerDamage = self.weaponDict[weaponName]

    #Setters
    def setPlayerName(self):
        playerName = input("Input Player Name: ")
        self.playerName = playerName

    def playerTakesDamage(self,damage):
        if self.playerHealth - damage == 0:
            print(youDiedASCII)
            exit(0) #Could Add Start Again here
        else:
            self.playerHealth = self.playerHealth - damage

    def playerHeals(self,amountHealed):
        if((self.playerHealth+amountHealed) >= 100):
            self.playerHealth = 100
        else:
            self.playerHealth = self.playerHealth+amountHealed

class Inventory(Player):

    def __init__(self):
        self.inventory = dict()

    def addItemToInventory(self,ItemName):
        if ItemName not in self.inventory:
            self.inventory.update({ItemName:1})
        else:
            self.inventory[ItemName] += 1

    def removeFromInventory(self,ItemName):
        if ItemName in self.inventory:
            if self.inventory[ItemName] == 1:
                self.inventory.pop(ItemName)
            else:
                self.inventory[ItemName] -= 1
        else:
            print(ItemName,"Is not in inventory")

    def printInventory(self):
        print(self.inventory)


