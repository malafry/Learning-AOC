# Advent of Code
# Day 11 - Part 1
# Source: https://adventofcode.com/2022/day/11

import re
import ast

rawInstructions = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-11-Puzzle-input.txt') as file:
    for line in file.readlines():
        rawInstructions.append(line.strip().replace('\n', ''))

class InstructionsEngine:
    
    def __init__(self, rawInstructions):

        self.rawInstructions = rawInstructions

    def apportionInstructions(self):

        self.allInventory = []
        self.allWorryOperation = []
        self.allWorryTest = []
        self.allTrueMonkey = []
        self.allFalseMonkey = []

        for i in range(len(rawInstructions)):
            if 'Starting items' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allInventory.append(item)
            if 'Operation' in rawInstructions[i]:
                item = rawInstructions[i][17:]
                self.allWorryOperation.append(item)
            if 'Test' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allWorryTest.append(item)
            if 'If true' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allTrueMonkey.append(item)
            if 'If false' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allFalseMonkey.append(item)

instructions = InstructionsEngine(rawInstructions)
instructions.apportionInstructions()

class MonkeyClass:

    def __init__(self, inventory, worryOperation, worryTest, trueMonkey, falseMonkey):
        self.inventory = inventory
        self.worryOperation = worryOperation
        self.worryTest = worryTest
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey

    def initiateAction(self):
        for i in range(len(self.inventory)):
            self.modifyWorry(self.inventory[i], self.worryOperation)
            # self.testWorry(self.inventory[i], self.worryTest)
            # self.moveItem(self.inventory[i], self.trueMonkey, self.falseMonkey)

    def modifyWorry(self, inspectedItem, modification):
        old = int(inspectedItem)
        modifiedItem = ast.parse(modification)
        new = exec(compile(modifiedItem, filename='', mode='exec'))
        print(new)
        print(ast.dump(modifiedItem))

    def testWorry(self, inspectedItem):
        pass

    def moveItem(self, inspectedItem):
        pass

monkeys = []
for i in range(8):
    monkeys.append(MonkeyClass(instructions.allInventory[i],
    instructions.allWorryOperation[i],
    instructions.allWorryTest[i],
    instructions.allTrueMonkey[i],
    instructions.allFalseMonkey[i]))

for i in range(len(monkeys)):
    monkeys[i].initiateAction()