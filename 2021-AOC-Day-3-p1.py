# Advent of Code
# 2021 - Day 3 - Part 1
# Source: https://adventofcode.com/2021/day/3

## IMPORTS ##
from collections import Counter
my_file = (r"2021 AOC\2021-AOC-Day-3-Puzzle-input.txt")
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

## ENGINES ##
# Parse list (data) and separate the nth digit of each number into the same group (listSeparated)
listSeparated = []
def separatorEngine(list):
    for i in range(len(list[0])):
        digitList = []
        for j in range(len(list)):
            digitList.append(list[j][i])
        listSeparated.append(digitList)

# Find the GAMMA: most common number in each nested array
def findCommonEngine(list):
    gammaRate = []
    for i in range(len(list)):
        counter = Counter(list[i])
        mostCommonNum = counter.most_common(1)[0][0]
        gammaRate.append(mostCommonNum)
    findDecimal(gammaRate, findLeastCommonEngine(gammaRate))
           
    #print(gammaRate) ## TEST
    #print(mostCommonNum) ## TEST

# Find the EPSILON: least common number based on GAMMA input
def findLeastCommonEngine(array):
    epsilonRate = []
    for i in range(len(array)):
        if array[i] == '0':
            epsilonRate.append('1')
        if array[i] == '1':
            epsilonRate.append('0')
    return epsilonRate
    #print(array) ## TEST
    #print(epsilonRate) ## TEST

def findDecimal(gamma, epsilon):
    gammaBinary = ''.join(gamma)
    epsilonBinary = ''.join(epsilon)
    value = int(gammaBinary, 2) * int(epsilonBinary, 2)
    print(value)

def runEngine():
    separatorEngine(data)
    findCommonEngine(listSeparated)

## RUN ##
runEngine() # ANSWER: 3813416

## TEST ##

## PSEUDO ##
'''
create a function that takes the nth sub-index of each index in an array and pass it to a new function
new function takes input and adds an index into. splits it, averages it

'''