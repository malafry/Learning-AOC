# Advent of Code
# Day 11 - Part 1
# Source: https://adventofcode.com/2022/day/11

import re
import math

rawInstructions = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-11-Puzzle-input.txt') as file:
    for line in file.readlines():
        rawInstructions.append(line.strip().replace('\n', ''))

class InstructionsEngine:
    
    def __init__(self, rawInstructions):
        self.rawInstructions = rawInstructions

    def apportionInstructions(self):
        self.allInventory = []
        self.allWorryModification = []
        self.allWorryTestValue = []
        self.allTrueMonkey = []
        self.allFalseMonkey = []

        for i in range(len(rawInstructions)):
            if 'Starting items' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allInventory.append(item)
            if 'Operation' in rawInstructions[i]:
                item = rawInstructions[i][17:]
                self.allWorryModification.append(item)
            if 'Test' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allWorryTestValue.append(item)
            if 'If true' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allTrueMonkey.append(item)
            if 'If false' in rawInstructions[i]:
                item = re.findall(r'\d+', rawInstructions[i])
                self.allFalseMonkey.append(item)

instructions = InstructionsEngine(rawInstructions)
instructions.apportionInstructions()

class MonkeyClass:

    def __init__(self, inventory, worryModification, worryTestValue, trueMonkey, falseMonkey):
        self.inventory = inventory
        self.worryModification = worryModification
        self.worryTestValue = int(worryTestValue[0])
        self.trueMonkey = int(trueMonkey[0])
        self.falseMonkey = int(falseMonkey[0])

        self.monkeyInspections = 0
        self.updatedWorry = ''

    def initiateAction(self):
        for i in range(len(self.inventory)):
            self.monkeyInspections += 1
            self.modifyWorry(self.inventory[i])
            self.moveItem()
        self.inventory.clear()

    def modifyWorry(self, inspectedItem):
        if 'old' in self.worryModification[5:]:
            self.updatedWorry = eval('{} {} {}'.format(inspectedItem, self.worryModification[4], inspectedItem))
        else:
            self.updatedWorry = eval('{} {} {}'.format(inspectedItem, self.worryModification[4], self.worryModification[6]))   

        self.updatedWorry = math.floor(self.updatedWorry / 3)

    def moveItem(self):
        if self.testWorry() == True:
            monkeys[self.trueMonkey].inventory.append(self.updatedWorry)
        if self.testWorry() == False:
            monkeys[self.falseMonkey].inventory.append(self.updatedWorry)

    def testWorry(self):
        if (self.updatedWorry % self.worryTestValue) == 0:
            return True
        else:
            return False

monkeys = []
for i in range(8):
    monkeys.append(MonkeyClass(instructions.allInventory[i],
    instructions.allWorryModification[i],
    instructions.allWorryTestValue[i],
    instructions.allTrueMonkey[i],
    instructions.allFalseMonkey[i]))

turns = 0
while turns < 20:
    turns += 1
    for i in range(len(monkeys)):
        if len(monkeys[i].inventory) == 0:
            continue
        else:
            monkeys[i].initiateAction()

monkeyBusiness = []
for i in range(len(monkeys)):
    monkeyBusiness.append(monkeys[i].monkeyInspections)

monkeyBusiness.sort(reverse=True)
monkeyBusinessValue = monkeyBusiness[0] * monkeyBusiness[1]
print(monkeyBusinessValue)
