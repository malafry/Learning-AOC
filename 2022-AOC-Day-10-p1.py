# Advent of Code
# Day 10 - Part 1
# Source: https://adventofcode.com/2022/day/10

## IMPORTS AND SETUP ##

moves = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-10-Puzzle-input.txt') as file:
    for line in file.readlines():
        moves.append(line.replace('\n',''))

## TOOLS: CLASSES AND FUNCTIONS ##
class MyRegister:

    def __init__(self, registerValue, signalStrength, instructions):
        
        self.registerValue = registerValue
        self.signalStrength = signalStrength
        self.instructions = instructions

        self.workOutput = {}

    def processInstructions(self):

        cycle = 0

        for i in range(len(self.instructions)):

            if self.instructions[i] == 'noop':
                cycle += 1
                self.workOutput[cycle] = self.registerValue
                self.registerValue += 0                

            else:
                cycle += 1
                self.workOutput[cycle] = self.registerValue
                self.registerValue += 0                

                cycle += 1 
                self.workOutput[cycle] = self.registerValue            
                self.registerValue += (int(self.instructions[i][5:]))

    def calculateSignalStrength(self, intSig):

        for i in range(len(intSig)):
            self.signalStrength += (self.workOutput[intSig[i]] * intSig[i])
            print(self.signalStrength)

## ENGINE: CALLS ##
register = MyRegister(1, 0, moves)
interestingSignals = [20, 60, 100, 140, 180, 220]

register.processInstructions()
register.calculateSignalStrength(interestingSignals)
