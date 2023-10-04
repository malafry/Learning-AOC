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
            if j not in reductionList:
                columnBits.append(int(data[j][i]))
        print("reductionList: {}".format(reductionList)) # TEST
        print(" - i: {} ## columnBits: {}".format(i, columnBits)) # TEST
        print(" - length of columnBits: {}".format(len(columnBits)))

        findCommonEngine(data, token, i, columnBits)

        if i == len(data[0]) or (len(columnBits) == 1):
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
    
    print(" - bitFrequency: {}".format(bitFrequency)) # TEST
    reduceList(data, i, bitFrequency)

def reduceList(data, i, bitFrequency):
    global reductionList
    for j in range(len(data)):
        if j not in reductionList:
            if data[j][i] != str(bitFrequency[0]):
                reductionList.append(j)

'''def reduceList(list, array):
    bestMatch = []

    for i in range(len(list)):
        indexOfBreak = -1
        for j in range(len(array)):
            if list[i][j] != str(array[j]):
                indexOfBreak = j
                break
        bestMatch.append(indexOfBreak - 1)

    return list[bestMatch.index(max(bestMatch))]'''    

## WORKING ON THIS FUNCTION CURRENTLY, but need to debug until I can print Success as per below...
def findDecimalEngine(date):
    return(1)
'''    if len(data) == len(int(reductionList) + 1):
        print("Success") # TEST
        return(1)'''

'''
def findDecimal(oxygenRate, co2Rate):   
    value = int(oxygenRate, 2) * int(co2Rate, 2)
    print(value)
'''

def runEngine(data):
    print(separatorEngine(data, token = "most") * separatorEngine(data, token = "least"))
    ## Currently, "most" returns None (unexpected), and "least" returns 1 (expected)

## RUN ##
reductionList = []
runEngine(data)