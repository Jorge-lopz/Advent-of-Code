# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                  ::::             ::::::::      #
#                                            ++: :+:          :+:    :+:      #
#     PROJECT: Advent of Code              #:+   +:+         +:+              #
#                                        +#++:++#++:        +#+               #
#                                       +#+     +#+  ++::  +#+                #
#     AUTHOR: Jorge Lopez Puebla       ##+     #+#  #   # #+#    #+#          #
#     LAST UPDATE: 21/12/2024         ###     ###   ####  ########            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/21

"""
· NUMERIC          · DIRECTIONAL

| 7 | 8 | 9 |          | ^ | A |
| 4 | 5 | 6 |      | < | v | > |
| 1 | 2 | 3 |
    | 0 | A |
"""

# IMPORTS
from collections import deque  # -> Double ended queue

NUMERIC = {
    c: (row, col)
    for row, line in enumerate('789\n456\n123\n 0A'.split("\n"))
    for col, c in enumerate(line)
    if c != ' '
}

DIRECTIONAL = {
    c: (row, col)
    for row, line in enumerate(' ^A\n<v>'.split("\n"))
    for col, c in enumerate(line)
    if c != ' '
}

with open('input.txt', 'r') as f:
    codes = [line.strip() for line in f.readlines()]

def generate_sequences(key_pad, start, end):
    to_check = deque([(start, '')])  # current_position, path_to_reach_it

    while to_check:
        current_position, path = to_check.popleft()  # Pop the first position and path from the queue (FIFO).

        # Determine the target position on the keypad for the desired end key.
        target = key_pad[end]

        # If the current position matches the target, yield the path and continue.
        if current_position == target:
            yield path
            continue

        # Calculate horizontal (column)
        column_move = target[1] - current_position[1]
        if column_move != 0:
            new_point = current_position[0], current_position[1] + (column_move // abs(column_move))

            if new_point in key_pad.values():
                # Add the new position and updated path to the queue.
                if column_move > 0:
                    to_check.append((new_point, path + '>'))
                elif column_move < 0:
                    to_check.append((new_point, path + '<'))

        # Calculate vertical (row) movement
        row_move = target[0] - current_position[0]
        if row_move != 0:
            new_point = current_position[0] + (row_move // abs(row_move)), current_position[1]

            if new_point in key_pad.values():
                # Add the new position and updated path to the queue.
                if row_move > 0:
                    to_check.append((new_point, path + 'v'))
                elif row_move < 0:
                    to_check.append((new_point, path + '^'))

cache = {}  # KEYPAD, deep, code

def get_min_length(KEYPAD, code, robots) -> int:
    if (len(KEYPAD), code, robots) in cache:  # If the result is already cached.
        return cache[len(KEYPAD), code, robots]

    # Base case: If no robots are left, the minimal sequence length is simply the length of the code.
    if robots == 0:
        cache[len(KEYPAD), code, robots] = len(code)
        return len(code)

    current_position = KEYPAD['A']  # Starting position
    minimal_length = 0
    new_robots = robots - 1

    for letter in code:
        # Find the min length needed by exploring all possible paths from the current position to the target.
        minimal_length += min(
            get_min_length(DIRECTIONAL, sequence + 'A', new_robots)
            for sequence in generate_sequences(KEYPAD, current_position, letter))
        current_position = KEYPAD[letter]

    # Cache the computed minimal sequence length for this combination of keypad, code, and robots.
    cache[len(KEYPAD), code, robots] = minimal_length

    return minimal_length

def solve(robots):
    result = 0
    for code in codes:
        min_value = get_min_length(NUMERIC, code, robots)
        result += min_value * int(''.join(c for c in code if c in '1234567890'))
    return result

# FIRST PART: Get the total complexity of the codes needed to control the robot that controls the robot (x2)

print("\n\033[37mThe total complexity of the codes needed to control the final robot is:\033[0m\033[1m", solve(3))

# SECOND PART: Get the total complexity of the codes needed to control the robot that controls the robot (x25)

print("\n\033[0m\033[37mThe total complexity of the codes needed to control the final robot is:\033[0m\033[1m",
      solve(26))
