import random
from Character import Player

sizeDict = {1 : 6, 2 : 12, 3 : 18, 4 : 24, 5 : 30}

class Maze:
    def __init__(self, maze, size):
        self.maze = maze
        self.size = size
        self.visited = generateVisited(size)
        self.visited[0][0] = 1
        self.visited[self.size-1][self.size-1] = 1
        self.movedTo = "-"
        self.recursiveVisited = generateVisited(size)

def generateMaze(size):
    #while(!endReachable():
        maze = []
        for i in range(size):
            maze.append(size * [0])
        maze = randomizeMaze(maze, size)
        return maze

def generateVisited(size):
    arr = []
    for i in range(size):
        arr.append(size * [0])
    return arr

def printMaze(Maze):
    c = 0
    for i in Maze.maze:
        r = 0
        mazeLine = ""
        for k in i:
            if(Maze.visited[c][r] == 1):
                mazeLine += str(k) + "  "
            else:
                mazeLine += "?" + "  "
            r+=1
        print(mazeLine)
        c+=1
    print("")

def randomizeMaze(maze, size):
    x = 0
    y = 0
    rand = random
    while(x < size):
        while (y < size):
            maze[x][y] = rand.choice("#$-&")
            y += 1
        x += 1
        y = 0
    #Add player
    maze[0][0] = "P"

    #Add exit
    maze[size-1][size-1] = "E"

    return Maze(maze, size)

def visited(Maze,x,y):
    if(Maze.visited[x][y] == 1):
        return True
    else:
        return False

def canVisit(Maze, x, y, recursive = False):
    if(x > Maze.size - 1 or y > Maze.size - 1 or y < 0 or x < 0):
        if(recursive == False):
            print("Can't move there! That's out of bounds!")
        return False
    if(Maze.maze[y][x] == "#"):
        if(recursive == False):
            print("Can't move there! A wall is in the way!")
            Maze.visited[y][x] = 1
        return False
    else:
        return True

def mazeMove(Maze, Player, direction):
    moved = False
    if(direction == "UP" and canVisit(Maze, Player.coords[0], Player.coords[1] - 1)):
        moved = True
        Maze.movedTo = Maze.maze[Player.coords[1] - 1][Player.coords[0]]
        Maze.maze[Player.coords[1]][Player.coords[0]] = "-"
        Maze.maze[Player.coords[1] - 1][Player.coords[0]] = "P"
        Player.coords[1] -= 1

    if(direction == "LEFT" and canVisit(Maze, Player.coords[0] - 1, Player.coords[1])):
        moved = True
        Maze.movedTo = Maze.maze[Player.coords[1]][Player.coords[0] - 1]
        Maze.maze[Player.coords[1]][Player.coords[0]] = "-"
        Maze.maze[Player.coords[1]][Player.coords[0] - 1] = "P"
        Player.coords[0] -= 1

    if(direction == "DOWN" and canVisit(Maze, Player.coords[0], Player.coords[1] + 1)):
        moved = True
        Maze.movedTo = Maze.maze[Player.coords[1] + 1][Player.coords[0]]
        Maze.maze[Player.coords[1]][Player.coords[0]] = "-"
        Maze.maze[Player.coords[1] + 1][Player.coords[0]] = "P"
        Player.coords[1] += 1

    if(direction == "RIGHT" and canVisit(Maze, Player.coords[0] + 1, Player.coords[1])):
        moved = True
        Maze.movedTo = Maze.maze[Player.coords[1]][Player.coords[0] + 1]
        Maze.maze[Player.coords[1]][Player.coords[0]] = "-"
        Maze.maze[Player.coords[1]][Player.coords[0] + 1] = "P"
        Player.coords[0] += 1

    Maze.visited [Player.coords[1]][Player.coords[0]] = 1
    return moved

def findPath(Maze, x = 0, y = 0):
    if(x == Maze.size - 1 and y == Maze.size - 1):
        return True
    if(canVisit(Maze, x, y, True) == False):
        return False
    if(Maze.recursiveVisited[y][x] == 1):
        return False
    Maze.recursiveVisited[y][x] = 1
    if(findPath(Maze, x, y - 1)):
        return True
    if(findPath(Maze, x + 1, y)):
        return True
    if(findPath(Maze, x, y + 1)):
        return True
    if(findPath(Maze, x - 1, y)):
        return True
    return False








