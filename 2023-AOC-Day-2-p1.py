# Advent of Code
# Day 2 - Part 1
# Source: https://adventofcode.com/2023/day/2

## SETUP
import pathlib
import re

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-2-Puzzle-input.txt'

with open(input, 'r') as file:
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
    greenSum = 0
    blueSum = 0
    for n1 in range(len(gameData[gameKey])):
        for n2 in range(len(gameData[gameKey][n1])):
            if 'red' in gameData[gameKey][n1][n2]:
                if redSum < int(re.search(r'\d+', gameData[gameKey][n1][n2]).group()):
                    redSum = int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
            if 'green' in gameData[gameKey][n1][n2]:
                if greenSum < int(re.search(r'\d+', gameData[gameKey][n1][n2]).group()):
                    greenSum = int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
            if 'blue' in gameData[gameKey][n1][n2]:
                if blueSum < int(re.search(r'\d+', gameData[gameKey][n1][n2]).group()):
                    blueSum = int(re.search(r'\d+', gameData[gameKey][n1][n2]).group())
    
    # TESTS
    print("GAME {}: Red: {}. Green: {}. Blue: {}.".format(gameKey, redSum, greenSum, blueSum))

    checkWin(gameKey, redSum, greenSum, blueSum)

def checkWin(gameKey, redSum, greenSum, blueSum):
    win = 0
    if redSum <= gameRules['red']:
       win += 1
    if greenSum <= gameRules['green']:
       win += 1
    if blueSum <= gameRules['blue']:
       win += 1
    
    # TEST
    print("Win value: {}".format(win))

    if win == 3:
        gamesWonID.append(gameKey)

        # TEST
        print("WIN!\n\n")

# ENGINE
gameRules = {'red': 12, 'green': 13, 'blue': 14}
gamesWonID = list()
winValue = 0

# TEST
#winCount = 0

for i in range(len(input)):
    setupGameData(input, i)
    runGameData(gameData, i)

for i in range(len(gamesWonID)):
    winValue += int(gamesWonID[i])

print("Value of winning games: {}".format(winValue)) # WRONG: 149 (too low)
print(gamesWonID)