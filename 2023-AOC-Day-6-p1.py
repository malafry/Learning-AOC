# Advent of Code
# Day 6 - Part 1
# Source: https://adventofcode.com/2023/day/6

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-6-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

time_str = input[0].split(':')[1].strip().split()
time_int = [int(x) for x in time_str]
record_distance_str = input[1].split(':')[1].strip().split()
record_distance_int = [int(x) for x in record_distance_str]

raceData = {'time': time_int, 'record_distance': record_distance_int}

def distance(i, time, record_distance):
    wins = list()
    for time_i in range(time):
        time_held = time_i # aka speed
        for time_in_motion in range(time - time_held + 1):
            distance = time_held * time_in_motion
            if distance > record_distance:
                if time_held not in wins:
                    wins.append(time_held)
    if wins:
        scores.append(len(wins))    

## ENGINE
scores = list()
winningTotal = 1

for i in range(len(raceData['time'])):
    distance(i, raceData['time'][i], raceData['record_distance'][i])

print("Score: {}. Winning total: {}.".format(scores, scores[0] * scores[1] * scores[2] * scores[3]))