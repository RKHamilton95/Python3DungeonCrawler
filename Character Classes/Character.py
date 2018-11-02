class Player(object):
    
    def __init__(self):
        self.playerName = ""
        self.playerHealth = int()  
        self.playerDamage = int()
        self.playerWeaponName = ""
        self.inventory = Inventory()

    #Getters
    def getPlayerHealth(self):
        return self.playerHealth

    #def playerGrabsWeapon(self,weaponName):
    #    self.playerWeaponName = weaponName
    #    self.playerDamage = self.weaponDict[weaponName]
    
    def playerTakesDamage(self,damage):
        self.playerHealth = self.playerHealth - damage
    
    def playerHeals(self,amountHealed):
        if((self.playerHealth+amountHealed) >= 100):
            self.playerHealth = 100
        else:
            self.playerHealth = self.playerHealth+amountHealed
    
class Inventory(Player):
    
    weaponDict = {"Sword":5,"Axe": 7,"Mace":8,"Claymore":10}
    healthPotionDict = {"Healing": 10,"Greater Healing":20,"Superior Healing":50,"FulL Healing":100}

    def __init__(self):
        self.inventory = dict()

    def addItemToInventory(self,ItemName):
        if ItemName not in self.inventory:
            self.inventory.update({ItemName:1})
        else:
            self.inventory[ItemName] += 1
    
    def printInventory(self):
        print(self.inventory)

#class Elf(Player):
    #def __init__(self):
    #    self.playerName = ""
    #    self.playerHealth = 80
    #    self.playerDamage = 5
    #    self.playerWeaponDamage = 0
    #    self.playerWeaponName = ""

Player1 = Player()
Player1.inventory.addItemToInventory("Sword")
Player1.inventory.addItemToInventory("Healing")
Player1.inventory.printInventory()

