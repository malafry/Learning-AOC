# Advent of Code
# 2021 - Day 4 - Part 1
# Source: https://adventofcode.com/2021/day/4

## IMPORTS ##
import re
my_file = (r"2021 AOC\2021-AOC-Day-4-Puzzle-input.txt")
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

instructions = data[0].split(',')

dataCopy = [item for item in data[1:] if item]

## ENGINES ##
def createBoardsEngine(dataCopy, boardSize):

    boardList = []
    for i in range(int(len(dataCopy) / boardSize)):
        if i == 0:
            count = 0
        boardList.append(dataCopy[(count):(count + boardSize)])
        count += boardSize

    for i in range(len(boardList)):
        for j in range(len(boardList[0])):
            boardList[i][j] = list(map(int, boardList[i][j].split()))

    boardKeys = []
    for i in range(len(boardList)):
        boardKeys.append("B{}".format(i + 1))
  
    global boardDictionary
    boardDictionary = dict(zip(boardKeys, boardList))
    
    rcKeys = []
    for r in range(5):
        rcKeys.append("R{}".format(r + 1))
    for c in range(5):
        rcKeys.append("C{}".format(c + 1))
    
    global resultsLog
    resultsLog = dict.fromkeys(boardKeys, [])
    for i in range(len(resultsLog)):
        resultsLog['B{}'.format(i + 1)] = dict.fromkeys(rcKeys, [])

    #global countTracker
    #for i in range(boardList):
    #    pass

    print("boardDictionary[B1] at step 3: {}".format(boardDictionary['B1'])) # TEST
    print("boardDictionary[B2] at step 3: {}".format(boardDictionary['B2'])) # TEST
    print("boardDictionary[B3] at step 3: {}".format(boardDictionary['B3'])) # TEST

def instructionEngine(instructions):
    for i in range(len(instructions)): # 27 instructions
        for b in range(len(boardDictionary)): # 3 boards
            for row in range(len(boardDictionary['B{}'.format(b + 1)])): #5 rows
                for col in range(len(boardDictionary['B{}'.format(b + 1)][row])): #5 cols
                    if int(instructions[i]) == boardDictionary['B{}'.format(b + 1)][row][col]:
                        checkEngine()
                        #boardDictionary['B{}'.format(b + 1)][row][col] = '*'
                        #resultsLog['B{}'.format(b + 1)].append("R{} C{}".format(row, col))
                        # Both lines above likely work, but I need to determine whether a Bingo is made each iteration
                        # Try to use the checkEngine() as a test
                        

def checkEngine():
    pass
#    for b in range(len(resultsLog['B{}'.format(b + 1)])): # 3 logs
    
    # Start here.
    # Consider a regex looking for five row Ns or five col Ns (if using the resultsLog)
    # Otherwise, consider a regex looking for an asterix ... might not be as easy as above.
    # The trick will be doing the calculation.

def runEngine(boardSize):
    createBoardsEngine(dataCopy, boardSize)
    instructionEngine(instructions)

    # TESTS
    print("resultsLog[B1]: {}".format(resultsLog['B1'])) # TEST
    print("resultsLog[B2]: {}".format(resultsLog['B2'])) # TEST
    print("resultsLog[B3]: {}".format(resultsLog['B3'])) # TEST 
    print("boardDictionary[B1]: {}".format(boardDictionary['B1'])) # TEST
    print("boardDictionary[B2]: {}".format(boardDictionary['B2'])) # TEST
    print("boardDictionary[B3: {}".format(boardDictionary['B3'])) # TEST

## RUN ##
runEngine(boardSize = 5)

## PSEUDOCODE ##
'''
Create a list of directions from the first row in data

Create three arrays to represent three boards (5x5) in data:
> boardOne; boardTwo; boardThree
> Each array is nested; each index is one row; each sub-index is a column
> i = row, j = column, so that boardOne[i/row][j/column] => boardOne[1][2] => row 1 column 2

Create three arrays to represent the counts; when count = 5, winner:
> boardOneResult; boardTwoResult; boardThreeResult
> row1...row5, col1...5

Create a function to parse directions

Create a function to search arrays (boards) for value
> if a value is found, the index is returned

Create a function to track counts
> the returned index is added to the results, where:
> value of i = 1 goes to row1; value of j = 2 goes to col2

Create a function to assess when a row or a column has 5 
> Iterates through rows and columns until a value of 5 is identified
'''
