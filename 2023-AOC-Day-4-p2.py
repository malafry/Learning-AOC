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
    cardKey = int(re.search(r'\d+(?=:)', input[set_i]).group()) # also == (i + 1)
    processedInput = re.sub('  ', ' ', input[set_i])
    winPattern = r'(?<=: )\d+(?: \d+)*(?= \|)'
    cardWinValues = re.split(' ', re.search(winPattern, processedInput).group())
    actualPattern = r'(?<= \| )\d+(?: \d+)*'
    cardActualValues = re.split(' ', re.search(actualPattern, processedInput).group())
    cardData.append([cardKey, cardWinValues, cardActualValues])

def runCardData(cardData, run_i):
    global totalCards, checkList
    totalCards += 1
    winningNumbers = list()
    checkList.append(run_i + 1) # TEST
    print(totalCards, checkList) # TEST

    ## MESS WITH THIS A LITTLE?
    for winNum in range(len(cardData[run_i][1])): # cardWinValues
        for actualNum in range(len(cardData[run_i][2])): # cardActualValues
            if cardData[run_i][1][winNum] == cardData[run_i][2][actualNum]:
                winningNumbers.append(cardData[run_i][1][winNum])

    for winNum in range(len(cardData[run_i][1])): # cardWinValues
        for actualNum in range(len(cardData[run_i][2])): # cardActualValues
            if cardData[run_i][1][winNum] == cardData[run_i][2][actualNum]:
                winningNumbers.append(cardData[run_i][1][winNum])
            # if cardData[run_i][1][winNum] == cardData[run_i][2][actualNum]:
            #     winningNumbers.append(cardData[run_i][1][winNum])
    
    if winningNumbers:
        for wins in range(len(winningNumbers)):
            if wins == 2:
                print("\n\nWINWINWIN")
            if (wins + 1 + run_i) == len(cardData):
                break
            else:
                runCardData(cardData, (run_i + 1))

## ENGINE
totalCards = int()
cardData = list()
checkList = list()

for set_i in range(len(input)):
    cardSetup(input, set_i)

for run_i in range(len(cardData)):
    runCardData(cardData, run_i)

print("\nTotal cards: {}".format(totalCards))
count = Counter(checkList)
print("Card 1: {} (1) -- Card 2: {} (2) -- Card 3: {} (4) -- Card 4: {} (8) -- Card 5: {} (15) -- Card 6: {} (1)".format(count[1], count[2], count[3], count[4], count[5], count[6]))