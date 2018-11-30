import random
from ASCIIArt import *
class Enemy(object):

    def __init__(self):
        self.enemyName = ""
        self.enemyHealth = 0
        self.enemyDamage = 0
        self.ascii = ""

    def damageEnemy(self,damageDone):
        self.enemyHealth -= damageDone

    def doDamage(self):
        return self.enemyDamage + random.randrange(0, self.enemyDamage)

def createTypeErrorPython():
    TypeErrorPython = Enemy()
    TypeErrorPython.enemyName = "TypeErrorPython"
    TypeErrorPython.enemyHealth = 25
    TypeErrorPython.enemyDamage = 5
    TypeErrorPython.ascii = TypeErrorpythonSnake
    return TypeErrorPython

def createNameErrorPython():
    NameErrorPython = Enemy()
    NameErrorPython.enemyName = "^&#NameErrorPython#&^"
    NameErrorPython.enemyHealth = 20
    NameErrorPython.enemyDamage = 2
    NameErrorPython.ascii = NameErrorpythonSnake
    return NameErrorPython

def createValueErrorPython():
    ValueErrorPython = Enemy()
    ValueErrorPython.enemyName = "ValueErrorPython"
    ValueErrorPython.enemyHealth = 15
    ValueErrorPython.enemyDamage = 5
    ValueErrorPython.ascii = ValueErrorpythonSnake
    return ValueErrorPython

def createSyntaxErrorPython():
    SyntaxErrorPython = Enemy()
    SyntaxErrorPython.enemyName = "SyntaxErrorPython"
    SyntaxErrorPython.enemyHealth = 35
    SyntaxErrorPython.enemyDamage = 3
    SyntaxErrorPython.ascii = SyntaxErrorpythonSnake
    return SyntaxErrorPython