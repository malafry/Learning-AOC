# Advent of Code
# 2021 - Day 3 - Part 2 - version 2
# Source: https://adventofcode.com/2021/day/3

## IMPORTS ##
import statistics
my_file = (r"2021 AOC\2021-AOC-Day-3-Puzzle-input.txt")
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

## ENGINES ##
def separatorEngine(data, token):
    global reductionList
    for i in range(len(data[0])):
        if i == 0:
            reductionList = []
        
        columnBits = []        
        for j in range(len(data)):
            if len(reductionList) == (len(data) - 1):
                break
            if j not in reductionList:
                columnBits.append(int(data[j][i]))
        if len(columnBits) > 0:
            findCommonEngine(data, token, i, columnBits)

    return findDecimalEngine(data)

def findCommonEngine(data, token, i, columnBits):
    bitFrequency = []

    if len(columnBits) > 1:
        meanNum = statistics.mean(columnBits)
    else:
        meanNum = columnBits[0]
    
    if meanNum > 0.5:
        mostCommon = 1
        leastCommon = 0
    elif meanNum < 0.5:
        mostCommon = 0
        leastCommon = 1
    else: # meanNum == 0.5
        mostCommon = 1
        leastCommon = 0
    
    if token == "most":
        bitFrequency.append(mostCommon)

    if token == "least":
        bitFrequency.append(leastCommon)

    reduceList(data, i, bitFrequency)

def reduceList(data, i, bitFrequency):
    global reductionList
    for j in range(len(data)):
        if j not in reductionList:
            if data[j][i] != str(bitFrequency[0]):
                reductionList.append(j)

def findDecimalEngine(data):
    binary = -1
    for i in range(len(data)):
        if i not in reductionList:
            binary = data[i]
    return int(binary, 2)

def runEngine(data):
    print("Result: {}".format(separatorEngine(data, token = "most") * separatorEngine(data, token = "least")))

## RUN ##
reductionList = []
runEngine(data) # Answer: 2990784
