# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 10/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/10

memory: [[int]]

with open('input.txt', 'r') as file:
    memory = [[int(char) for char in line.strip()] for line in file.readlines()]

# FIRST PART: Get the sum of scores (number of trail ending 9s) of every trailhead (0)
scores = []

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right Left Down Up

def get_trail_ends(nxt: int, row: int, col: int):
    global trail_ends
    for direction in directions:
        pos = [row + direction[0], col + direction[1]]
        if pos[0] < 0 or pos[0] >= len(memory) or pos[1] < 0 or pos[1] >= len(memory[0]):
            continue
        if nxt == 9 == memory[pos[0]][pos[1]]:
            trail_ends.add((pos[0], pos[1]))
        elif memory[pos[0]][pos[1]] == nxt:
            get_trail_ends(nxt + 1, pos[0], pos[1])

for row in range(len(memory)):
    for col in range(len(memory[row])):
        if memory[row][col] == 0:
            trail_ends = set()
            get_trail_ends(1, row, col)
            scores.append(len(trail_ends))
            # print(f"\033[1mLEN: \033[0m[{len(trail_ends)}]\033[1m  TRAIL ENDS:\033[0m", *trail_ends)

print("\n\033[37mThe sum of trails scores (distinct trail ends) is:\033[0m\033[1m", sum(scores))

# SECOND PART: Get the product of the three largest scores
scores = []

def get_trails(nxt: int, row: int, col: int):
    global trails
    for direction in directions:
        pos = [row + direction[0], col + direction[1]]
        if pos[0] < 0 or pos[0] >= len(memory) or pos[1] < 0 or pos[1] >= len(memory[0]):
            continue
        if nxt == 9 == memory[pos[0]][pos[1]]:
            trails.append((pos[0], pos[1]))
        elif memory[pos[0]][pos[1]] == nxt:
            get_trails(nxt + 1, pos[0], pos[1])

for row in range(len(memory)):
    for col in range(len(memory[row])):
        if memory[row][col] == 0:
            trails = []
            get_trails(1, row, col)
            scores.append(len(trails))
            # print(f"\033[1mLEN: \033[0m[{len(trail_ends)}]\033[1m  TRAIL ENDS:\033[0m", *trail_ends)

print("\n\033[0m\033[37mThe sum of trails scores (distinct trail paths) is:\033[0m\033[1m", sum(scores))
