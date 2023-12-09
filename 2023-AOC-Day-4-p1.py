# Advent of Code
# Day 4 - Part 1
# Source: https://adventofcode.com/2023/day/4

## SETUP
import pathlib
import re

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-4-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def cardEngine(input, i):
    cardKey = re.search(r'\d+(?=:)', input[i]).group()
    processedInput = re.sub('  ', ' ', input[i])
    winPattern = r'(?<=: )\d+(?: \d+)*(?= \|)'
    cardWinValues = re.split(' ', re.search(winPattern, processedInput).group())
    actualPattern = r'(?<= \| )\d+(?: \d+)*'
    cardActualValues = re.split(' ', re.search(actualPattern, processedInput).group())

    runCardData(cardWinValues, cardActualValues)

def runCardData(cardWinValues, cardActualValues):
    global points
    winningNumbers = list()
    for i in range(len(cardActualValues)):
        for j in range(len(cardWinValues)):
            if cardWinValues[j] == cardActualValues[i]:
                winningNumbers.append(cardWinValues[j])
    if len(winningNumbers) > 0: # Without this, an empty list was adding 1/2 point each
        points += (2**(len(winningNumbers) - 1))

## ENGINE
points = 0
for i in range(len(input)):
    cardEngine(input, i)

print("Total card points: {}".format(points))