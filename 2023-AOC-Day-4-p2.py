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
    cardKey = re.search(r'\d+(?=:)', input[i]).group() # also == (i + 1)
    processedInput = re.sub('  ', ' ', input[i])
    winPattern = r'(?<=: )\d+(?: \d+)*(?= \|)'
    cardWinValues = re.split(' ', re.search(winPattern, processedInput).group())
    actualPattern = r'(?<= \| )\d+(?: \d+)*'
    cardActualValues = re.split(' ', re.search(actualPattern, processedInput).group())
    cardData.append([cardKey, cardWinValues, cardActualValues])

    #runCardData(cardKey, cardWinValues, cardActualValues)

def runCardData(cardData, originCard):
    print(type(cardData)) # TEST
    print(type(originCard)) # TEST
    global points
    winningNumbers = list()

    for originCard in cardData:
        for i in range(len(cardData[originCard][2])): # cardActualValues
            for j in range(len(cardData[originCard][1])): # cardWinValues
                if cardData[originCard][j] == cardData[originCard][i]:
                    winningNumbers.append(cardData[originCard][j])
    
    print(originCard, winningNumbers) # TEST

    if len(winningNumbers) > 0:
        points =+ 1
        for i in range(len(winningNumbers)):
            if (originCard + i) > len(cardData):
                continue
            else:
                runCardData(cardData, originCard + i)

## ENGINE
points = 0
cardData = list()
for i in range(len(input)):
    cardSetup(input, i)

for i in range(len(input)):
    runCardData(cardData, i)

print(cardData)

print("Total card points: {}".format(points))