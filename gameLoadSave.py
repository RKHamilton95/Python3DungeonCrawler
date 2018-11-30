import csv
from Character import *

def loadPlayer(playerName):
    arr = []
    with open(playerName + '.csv', 'r') as csvfile:
        reader = csvfile.readlines()
        for line in reader:
                line = line.rstrip()
                arr.append(line)

        p = Player()
        p.playerName = str(arr[0])
        p.playerHealth = 100
        p.playerDamage = int(arr[1])
        p.playerWeaponName = arr[2]
        return p

def savePlayer(playerObj):
    with open(playerObj.playerName + '.csv', 'w') as csvfile:
        csvfile.write(playerObj.playerName+"\n")
        #csvfile.write(str(playerObj.playerHealth))
        csvfile.write(str(playerObj.playerDamage)+"\n")
        csvfile.write(playerObj.playerWeaponName+"\n")
