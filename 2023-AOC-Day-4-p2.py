# Advent of Code
# Day 4 - Part 2
# Source: https://adventofcode.com/2023/day/4#part2

## SETUP
import pathlib
import re

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-4-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def cardSetup(input, i):
    cardKey = int(re.search(r'\d+(?=:)', input[i]).group()) # also == (i + 1)
    processedInput = re.sub('  ', ' ', input[i])
    winPattern = r'(?<=: )\d+(?: \d+)*(?= \|)'
    cardWinValues = re.split(' ', re.search(winPattern, processedInput).group())
    actualPattern = r'(?<= \| )\d+(?: \d+)*'
    cardActualValues = re.split(' ', re.search(actualPattern, processedInput).group())
    cardData.append([cardKey, cardWinValues, cardActualValues])

def runCardData(cardData, i):
    global points

    winningNumbers = list()
    
    print("\nrunCardData called on original index {}".format(i))

    for win in range(len(cardData[i][1])): # cardWinValues
        for actual in range(len(cardData[i][2])): # cardActualValues
            if cardData[i][1][win] == cardData[i][2][actual]:
                    winningNumbers.append(cardData[i][1][win])
  
    print("# winning numbers: {}, (current points: {})".format(winningNumbers, points))
    if len(winningNumbers) > 0:
        points += 1
        for wins in range(len(winningNumbers)):
            if (i + 1 + (wins + 1)) <= len(cardData):
                print("## runCardData (i {}) recursion called on wins {}".format(i, i + (wins + 1)))
                runCardData(cardData, i + (wins + 1))

## ENGINE
points = 0
cardData = list()

for i in range(len(input)):
    cardSetup(input, i)

for i in range(len(cardData)):
    runCardData(cardData, i)

print("\nTotal card points: {}".format(points))