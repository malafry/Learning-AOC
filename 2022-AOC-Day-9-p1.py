# Advent of Code
# Day 9 - Part 1
# Source: https://adventofcode.com/2022/day/9

## IMPORTS AND SETUP ##

moves = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-9-Puzzle-input.txt') as file:
    for line in file.readlines():
        moves.append(line.replace('\n',''))

## TOOLS: CLASSES AND FUNCTIONS ##
class MyHead:

    def __init__(self, xloc, yloc):
        
        self.xloc = xloc
        self.yloc = yloc
        self.xlocPrev = xloc
        self.ylocPrev = yloc

    def moveX(self, value):

        self.xlocPrev = self.xloc
        self.ylocPrev = self.yloc
        self.xloc += value

        grid[self.yloc][self.xloc] = 'H'

        if tail.trailCheck() == True:
            grid[self.ylocPrev][self.xlocPrev] = '#'
        else:
            grid[self.ylocPrev][self.xlocPrev] = '.'

        if tail.checkPullX() == True:
            tail.pull()

    def moveY(self, value):
        
        self.xlocPrev = self.xloc
        self.ylocPrev = self.yloc
        self.yloc += value

        grid[self.yloc][self.xloc] = 'H'

        if tail.trailCheck() == True:
            grid[self.ylocPrev][self.xlocPrev] = '#'
        else:
            grid[self.ylocPrev][self.xlocPrev] = '.'

        if tail.checkPullY() == True:
            tail.pull()

class MyTail:

    def __init__(self, xloc, yloc):
        
        self.xloc = xloc
        self.yloc = yloc
        self.xlocPrev = xloc 
        self.ylocPrev = yloc
        self.trailHistory = []

    def checkPullX(self):
        
        if abs(abs(head.xloc) - abs(self.xloc)) > 1:
            return True
        else:
            return False

    def checkPullY(self):
        
        if abs(abs(head.yloc) - abs(self.yloc)) > 1:
            return True
        else:
            return False

    def pull(self):
        
        self.xlocPrev, self.ylocPrev = self.xloc, self.yloc
        self.xloc, self.yloc = head.xlocPrev, head.ylocPrev

        grid[self.yloc][self.xloc] = 'T'

        tail.trail()

    def trail(self):

        grid[self.ylocPrev][self.xlocPrev] = '#'
        self.trailHistory.append([self.ylocPrev, self.xlocPrev])

    def trailCheck(self):
        
        check = [head.ylocPrev, head.xlocPrev]

        if check in self.trailHistory:
            return True
        else:
            return False

## ENGINE: CALLS ##
grid = [['.' for i in range(750)] for _ in range(750)]
startX, startY = (len(grid)//2), (len(grid)//2)

head = MyHead(startX, startY)
tail = MyTail(startX, startY)

for i in range(len(moves)):
    
    direction = moves[i][0]
    number = int(moves[i][2:])

    if 'R' in direction:
        
        for i in range(abs(number)):
            head.moveX(1)

    if 'L' in direction:
        
        for i in range(abs(number)):
            head.moveX(-1)

    if 'D' in direction:
        
        for i in range(abs(number)):
            head.moveY(1)
   
    if 'U' in direction:
        
        for i in range(abs(number)):
            head.moveY(-1)

uniqueTrailHistory = []

[uniqueTrailHistory.append(item) for item in tail.trailHistory if item not in uniqueTrailHistory]

print(len(uniqueTrailHistory) + 1)