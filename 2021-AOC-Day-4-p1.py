# Advent of Code
# 2021 - Day 4 - Part 1
# Source: https://adventofcode.com/2021/day/4

## IMPORTS ##
my_file = (r"2021 AOC\2021-AOC-Day-4-Puzzle-input.txt")
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

instructions = data[0].split(',')

dataCopy = [item for item in data[1:] if item]

# Code is functional until here
# Instructions are parsed and dataCopy is only board rows
# All boards will be 5x5, which means each index in dataCopy is a board row
# Can divide length of dataset by 5 to determine the number of boards in dataCopy
# Cannot create unique variables, so everything should be a separate nest within a board list

## ENGINES ##
def createBoardsEngine(dataCopy, boardSize):
    
    boardList = []
    for i in range(int(len(dataCopy) / boardSize)):
        if i == 0:
            count = 0
        boardList.append(dataCopy[(count):(count + boardSize)])
        count += boardSize

    print("boardList at step 1: {}".format(boardList)) # TEST

    for i in range(len(boardList)):
        for j in range(len(boardList[0])):
            boardList[i][j] = list(map(int, boardList[i][j].split()))

    print("boardList at step 2: {}".format(boardList)) # TEST

    boardKeys = []
    for i in range(len(boardList)):
        boardKeys.append("B{}".format(i + 1))
    
    boardDictionary = dict(zip(boardKeys, boardList))
    
    print("boardDictionary[B1] at step 3: {}".format(boardDictionary['B1'])) # TEST
    print("boardDictionary[B2] at step 3: {}".format(boardDictionary['B2'])) # TEST
    print("boardDictionary[B3] at step 3: {}".format(boardDictionary['B3'])) # TEST


## RUN ##
createBoardsEngine(dataCopy, boardSize = 5)

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
