# Advent of Code
# Day 4 - Part 2
# Source: https://adventofcode.com/2023/day/4#part2

## SETUP
import pathlib
import re
from collections import Counter

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-4-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def cardSetup(input, set_i):
    cardKey = int(re.search(r'\d+(?=:)', input[set_i]).group())
    processedInput = re.sub('  ', ' ', input[set_i])
    winPattern = r'(?<=: )\d+(?: \d+)*(?= \|)'
    cardWinValues = re.split(' ', re.search(winPattern, processedInput).group())
    actualPattern = r'(?<= \| )\d+(?: \d+)*'
    cardActualValues = re.split(' ', re.search(actualPattern, processedInput).group())
    cardData.append([cardKey, cardWinValues, cardActualValues])

def runCardData(cardData, run_i):
    global totalCards
    winningNumbers = list()
    totalCards += 1

    for winNum in range(len(cardData[run_i][1])): # cardWinValues
        for actualNum in range(len(cardData[run_i][2])): # cardActualValues
            if cardData[run_i][1][winNum] == cardData[run_i][2][actualNum]:
                winningNumbers.append(cardData[run_i][1][winNum])
    
    if winningNumbers:
        for wins in range(len(winningNumbers)):
            if (wins + 1 + run_i) == len(cardData):
                break
            else:
                runCardData(cardData, (wins + 1 + run_i))

## ENGINE
totalCards = int()
cardData = list()

for set_i in range(len(input)):
    cardSetup(input, set_i)

for run_i in range(len(cardData)):
    runCardData(cardData, run_i)

print("\nTotal cards: {}".format(totalCards))