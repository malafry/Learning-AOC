# Advent of Code
# Day 7 - Part 1
# Source: https://adventofcode.com/2023/day/7

## SETUP
import pathlib
from collections import Counter

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-7-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setupPlays(input):
    global plays
    for i in range(len(input)):
        cardData = {'id': i, 'rank': int(), 'hand': input[i].split()[0], 'type': str(), 'bet': int(input[i].split()[1]), 'score': int()}
        plays.append(cardData)

def runPlays(plays):
    for i in range(len(plays)):
        handType(plays[i])
        handRank(plays[i])

def handType(hand):
    global handTypeDict
    handType = Counter(hand['hand'])
    print(handType)
    if 5 in handType.values():
        hand['type'] = '5kind'
    elif 4 in handType.values():
        hand['type'] = '4kind'
    elif 3 in handType.values():
        if 2 in handType.values():
            hand['type'] = 'fullhouse'
        else:
            hand['type'] = '3kind'
    elif 2 in handType.values():
        num_pairs = sum(1 for count in handType.values() if count == 2)
        if num_pairs == 2:
            hand['type'] = '2pair'
        elif num_pairs == 1:
            hand['type'] = '1pair'
    else:
        hand['type'] = 'highcard'

def handRank(hand):
    pass

## ENGINE
plays = list()
handTypeDict = dict()
setupPlays(input)
runPlays(plays)
print(plays) ## TEST


## PSEUDO / RULES
'''
1 hand = 5 cards

> [A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2]

Every hand has 1 type:
> five of a kind (AAAAA)
> four of a kind (AA8AA)
> full house (23332)
> three of a kind (TTT98)
> two pair (23432)
> one pair (A23A4)
> high card (23456)

Rules:
> card type wins (DO NOT compare the strongest cards the type)
> if tie, compare first card in each hand
> if tie, compare second card in each hand
> if tie, [...]

Scoring:
> Rank the hands
> the lowest hand is rank 1
> the second lowest hand is rank 2
> [...]

> Each hand has a bid; the bind is multiplied by the rank (e.g. lowest hand bind is multiplied by 1)

'''