# Advent of Code
# Day 2 - Part 1
# Source: https://adventofcode.com/2023/day/2

## SETUP
import pathlib
import re

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-2-Puzzle-input.txt'

with open(input, "r") as file:
    input = [line.strip() for line in file]

gameData = dict()

def setupGameData(input, i):
    gameKey = re.search(r'\d+(?=:)', input[i])
    gameValue = re.split('; ', re.search(r'(?<=: ).+', input[i]).group())
    gameValueNested = list()
    for x in range(len(gameValue)):
        gameValueNested.append(re.split(', ', gameValue[x]))
    gameData[gameKey.group()] = gameValueNested

def runGameData(gameData, i):
    gameKey = str(i + 1)
    redSum = 0
    blueSum = 0
    greenSum = 0
    for n1 in range(len(gameData[gameKey])):
        for n2 in range(len(gameData[gameKey][n1])):
            if 'red' in gameData[gameKey][n1][n2]:
                redSum += int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
            if 'blue' in gameData[gameKey][n1][n2]:
                blueSum += int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
            if 'green' in gameData[gameKey][n1][n2]:
                greenSum += int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
    
    checkWin(redSum, blueSum, greenSum, gameKey)

def checkWin(redSum, blueSum, greenSum, gameKey):
    win = 0
    if redSum <= gameRules['red']:
       win += 1
    if blueSum <= gameRules['blue']:
       win += 1
    if greenSum <= gameRules['green']:
       win += 1
    
    if win == 3:
        gamesWonID.append(gameKey)

# ENGINE
gameRules = {'red': 12, 'green': 13, 'blue': 14}
gamesWonID = list()
winValue = 0

for i in range(len(input)):
    setupGameData(input, i)
    runGameData(gameData, i)

for i in range(len(gamesWonID)):
    winValue += int(gamesWonID[i])

print("Value of winning games: {}".format(winValue)) # WRONG: 149 (too low)