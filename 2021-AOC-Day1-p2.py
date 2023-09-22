# Advent of Code
# 2021 - Day 1 - Part 2
# Source: https://adventofcode.com/2021/day/1

## IMPORTS ##
my_file = (r'2021 AOC\2021-AOC-Day-1-Puzzle-input.txt')
with open(my_file, "r") as file:
    data = [int(line.strip()) for line in file]
    
## SETUP
depthInc = 0
sumData = []

## ENGINE
for num in range(len(data)):
    if num == (len(data) - 2):
        break
    else:
        sumData.append(data[num] + (data[num + 1]) + (data[num + 2]))
    
for num in range(len(sumData)):
    if num == 0:
        continue
    if sumData[num] > sumData[num - 1]:
        depthInc += 1

## RESULT
print(depthInc)
