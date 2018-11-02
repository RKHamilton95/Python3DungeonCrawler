class Player(object):
    def __init__(self):
        self.playerName = ""
        self.playerHealth = int()  
        self.playerDamage = int()
        self.playerWeaponDamage = int()
        self.playerWeaponName = ""
    
    def getPlayerHealth(self):
        return self.playerHealth
    
    def setPlayerHealth(self,damage):
        self.playerHealth = self.playerHealth - damage
    
class Elf(Player):
    def __init__(self):
        self.playerName = ""
        self.playerHealth = 80
        self.playerDamage = 5
        self.playerWeaponDamage = 0
        self.playerWeaponName = ""

Player1 = Player()
Player1.playerName = "DONNIE"
#print(Player1.playerName)
ElfPlayer = Elf()
ElfPlayer.playerName = "DILLY"
print(ElfPlayer.getPlayerHealth())
ElfPlayer.setPlayerHealth(10)
print(ElfPlayer.getPlayerHealth())
print(ElfPlayer.playerName)