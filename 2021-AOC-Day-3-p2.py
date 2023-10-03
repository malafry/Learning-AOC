# Advent of Code
# 2021 - Day 3 - Part 2
# Source: https://adventofcode.com/2021/day/3

## IMPORTS ##
import statistics
my_file = (r"2021 AOC\2021-AOC-Day-3-Puzzle-input.txt")
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

## ENGINES ##
listSeparated = []
def separatorEngine(list):
    
    for i in range(len(list[0])):
        digitList = []
        for j in range(len(list)):
            digitList.append(int(list[j][i]))
        listSeparated.append(digitList)
    findCommonEngine(list, listSeparated)

def findCommonEngine(list, listSeparated):
    oxygenRate = []
    co2Rate = []

    for i in range(len(listSeparated)):
        meanNum = statistics.mean(listSeparated[i])
        if meanNum > 0.5:
            mostCommon = 1
            leastCommon = 0
        if meanNum == 0.5:
            mostCommon = 1
            leastCommon = 0
        if meanNum < 0.5:
            mostCommon = 0
            leastCommon = 1
        oxygenRate.append(mostCommon)
        co2Rate.append(leastCommon)

    findDecimal(reduceList(list, oxygenRate), reduceList(list, co2Rate))

def reduceList(list, array):
    bestMatch = []

    for i in range(len(list)):
        indexOfBreak = -1
        for j in range(len(array)):
            if list[i][j] != str(array[j]):
                indexOfBreak = j
                break
        bestMatch.append(indexOfBreak - 1)

    return list[bestMatch.index(max(bestMatch))]

def findDecimal(oxygenRate, co2Rate):   
    value = int(oxygenRate, 2) * int(co2Rate, 2)
    print(value)

def runEngine():
    separatorEngine(data)

## RUN ##
runEngine() # ANSWER: 3812795 is too high, 2515396 is too low
