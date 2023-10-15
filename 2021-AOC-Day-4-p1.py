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
    
    global resultsLog
    resultsLog = []
    for i in range(len(boardDictionary)):
        resultsLog.append([])

def instructionEngine(instructions):
    for i in range(len(instructions)): # 27 instructions
        for b in range(len(boardDictionary)): # 3 boards
            for row in range(len(boardDictionary['B{}'.format(b + 1)])): #5 rows
                for col in range(len(boardDictionary['B{}'.format(b + 1)][row])): #5 cols
                    if int(instructions[i]) == (boardDictionary['B{}'.format(b + 1)][row][col]):
                        boardDictionary['B{}'.format(b + 1)][row][col] = ''
                        resultsLog[b].append("R{}".format(row + 1))
                        resultsLog[b].append("C{}".format(col + 1))
                        if (checkEngine(resultsLog, b) == True):
                            key = "B{}".format(b + 1)
                            winningPoints = int(instructions[i])* (int(sum([num for sublist in boardDictionary[key] for num in sublist if isinstance(num, int)])))
                            return(print("Winning board: {}. Last value: {}. Winning points: {}. i: {}".format((b + 1), instructions[i], winningPoints, i)))                        

def checkEngine(resultsLog, board):
    count = 0
    pattern = ['R1', 'R2', 'R3', 'R4', 'R5', 'C1', 'C2', 'C3', 'C4', 'C5']
    for j in range(len(pattern)):
        logTemp = ', '.join(resultsLog[board])
        count = len(re.findall(pattern[j], logTemp))
        if count == 5:
            return True
        else:
            return False

def runEngine(boardSize):
    createBoardsEngine(dataCopy, boardSize)
    instructionEngine(instructions)

## RUN ##
runEngine(boardSize = 5)

## PSEUDOCODE ##