##This file will need work just needed to build a basic idea of the functions

def loadGame():
    try:
       saveFile = open("saveFile.txt","r")
       readItems = saveFile.read
       saveFile.close
       return readItems
    except OSError:
        print("Save File Does Not Exist")


def saveGame(playerData):
    try:
        saveFile = open("saveFile.txt","w+")
        saveFile.write(playerData)
        saveFile.close
    except OSError:
        print("Error During Saving")