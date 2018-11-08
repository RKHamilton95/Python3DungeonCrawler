from ASCIIArt import *

class Player(object):
    
    weaponDict = {"Sword":5,"Axe": 7,"Mace":8,"Claymore":10}
    healthPotionDict = {"Healing": 10,"Greater Healing":20,"Superior Healing":50,"FulL Healing":100}

    def __init__(self):
        self.playerName = ""
        self.playerHealth = 100  
        self.playerDamage = 5
        self.playerWeaponName = ""
        self.inventory = Inventory()

    #Getters
    def getPlayerHealth(self):
        return self.playerHealth

    def playerSwitchesToWeapon(self,weaponName):
        self.playerWeaponName = weaponName
        self.playerDamage = self.weaponDict[weaponName]
    
    def playerTakesDamage(self,damage):
        if self.playerHealth - damage == 0:
            print(youDiedASCII)
            exit(0)
        else:
            self.playerHealth = self.playerHealth - damage

    def playerDoesDamage(self):
        return self.playerDamage
    
    def playerHeals(self,amountHealed):
        if((self.playerHealth+amountHealed) >= 100):
            self.playerHealth = 100
        else:
            self.playerHealth = self.playerHealth+amountHealed

class Enemy(object):

    def __init__(self):
        self.enemyName = ""
        self.enemyHealth = 30
        self.enemyDamage = 5

    def damageEnemy(self,damageDone):
        self.enemyHealth -= damageDone

    def doDamage(self):
        return self.enemyDamage


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


Player1 = Player()
#Damage Test
#Player1.playerTakesDamage(100)
print(playerCharacter,pythonSnake)

#Inventory Tests
#Player1.inventory.addItemToInventory("Sword")
#Player1.inventory.addItemToInventory("Sword")
#Player1.inventory.addItemToInventory("Sword")
#Player1.inventory.addItemToInventory("Sword")
#Player1.inventory.addItemToInventory("Healing")
#Player1.inventory.printInventory()
#Player1.inventory.removeFromInventory("Sword")
#Player1.inventory.removeFromInventory("Sword")
#Player1.inventory.removeFromInventory("Cat")
#Player1.inventory.printInventory()

