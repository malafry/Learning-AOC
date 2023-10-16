# Advent of Code
# 2021 - Day 4 - Part 2
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

    global winningBoards
    winningBoards = []

def instructionEngine(instructions):
    for i in range(len(instructions)): # 27 instructions
        for b in range(len(boardDictionary)): # 3 boards
            board = 'B{}'.format(b + 1)
            if (board in winningBoards):
                continue
            else:
                for row in range(len(boardDictionary[board])): #5 rows
                    for col in range(len(boardDictionary[board][row])): #5 cols
                        if int(instructions[i]) == boardDictionary[board][row][col]: # Can't use int() with boardDictionary because of line below
                            boardDictionary[board][row][col] = ''
                            resultsLog[b].append("R{}".format(row + 1))
                            resultsLog[b].append("C{}".format(col + 1))
                            print("{} : {}".format(i, resultsLog[b]))
                            if (checkEngine(resultsLog, board, b, i) == True):
                                winningPoints = int(instructions[i])* (int(sum([num for sublist in boardDictionary[board] for num in sublist if isinstance(num, int)])))
                                return(print("Last winning board: {}. Last value: {}. Winning points: {}. i: {}".format(board, instructions[i], winningPoints, i)))                        
                                # LAST WINNING BOARD should be: i: 14 = 13

def checkEngine(resultsLog, board, b, iter):
    count = 0
    pattern = ['R1', 'R2', 'R3', 'R4', 'R5', 'C1', 'C2', 'C3', 'C4', 'C5']
    for j in range(len(pattern)):
        logTemp = ', '.join(resultsLog[b - 1])
        count = len(re.findall(pattern[j], logTemp))
        if count == 5:
            winningBoards.append(board)
            print("Winning boards: {} @ i: {} = {}".format(winningBoards, iter, instructions[iter])) # TEST
            if iter == 14: # iter 14 = 13 instruction # TEST
                print("winningBoards @ i 14: {}".format(len(winningBoards))) # TEST
                print("boardDictionary @ i 14: {}".format(len(boardDictionary))) # TEST
                # ITER 14 is not being printed, so count != 5 @ iter 14.
            if (len(winningBoards) == len(boardDictionary)):
                return True
        else:
            return False

def runEngine(boardSize):
    createBoardsEngine(dataCopy, boardSize)
    instructionEngine(instructions)

## RUN ##
runEngine(boardSize = 5)
