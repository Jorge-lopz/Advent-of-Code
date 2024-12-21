# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 07/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/7

memory: [[int, [int]]] = []

# Read input file
with open('input.txt', 'r') as file:
    for line in file.readlines():
        memory.append([int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split(' ')))])

def solve(test_operations):
    global total_possible
    for operation in memory:
        if len(operation[1]) == 1:
            total_possible += operation[0]
        else:
            if sum(operation[1]) > operation[0]:  # If sum > result, so will the multiplication -> False
                continue
            elif sum(operation[1]) == operation[0]:  # If the sum is equal to the result
                total_possible += operation[0]
            else:
                if test_operations(operation[0], operation[1], now=0):
                    total_possible += operation[0]

# FIRST PART: Find the possible operations adding just '+' or '✕' and sum their results

total_possible = 0

def test_operations(result: int, numbers: [int], now: int):
    if not numbers:
        return now == result

    # Consider the first number
    num = numbers[0]
    remaining = numbers[1:]

    # Try both sum and multiplication
    return (
            test_operations(result, remaining, now + num) or
            test_operations(result, remaining, now * num if now != 0 else num)
    )

solve(test_operations)

print("\n\033[37mThe total possible sum is:\033[0m\033[1m", total_possible)

# SECOND PART: Find the possible operations adding just '+', '✕' or '||' (concatenator) and sum their results

total_possible = 0

def test_operations(result: int, numbers: [int], now: int):
    if not numbers:
        return now == result

    # Consider the first number
    num = numbers[0]
    remaining = numbers[1:]

    # Try both sum and multiplication
    return (
            test_operations(result, remaining, now + num) or
            test_operations(result, remaining, now * num if now != 0 else num) or
            test_operations(result, remaining, int(f"{now}{num}") if now != 0 else num)
    )

solve(test_operations)

print("\n\033[37mThe total possible sum (with concatenation) is:\033[0m\033[1m", total_possible)
