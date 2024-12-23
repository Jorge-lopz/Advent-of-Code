# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 04/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/4

with open('input.txt', 'r') as f:
    memory: [[str]] = [list(line.strip()) for line in f.readlines()]

rows = len(memory)
cols = len(memory[0])

# FIRST PART: Get the number of times 'XMAS' appears in any direction on the input text
target = 'XMAS'
result = 0
directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
    (1, 1),  # Down-right
    (-1, -1),  # Up-left
    (1, -1),  # Down-left
    (-1, 1)  # Up-right
]

def check_direction(x: int, y: int, dx: int, dy: int):
    for i in range(len(target)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or memory[nx][ny] != target[i]:
            return False
    return True

for row in range(rows):
    for col in range(cols):
        for dx, dy in directions:
            if check_direction(row, col, dx, dy):
                result += 1

print("\n\033[37mThe number of 'XMAS' is:\033[0m\033[1m", result)

# SECOND PART: Get the number of times 'MAS' appears in an X-format
mas_result = 0

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if memory[i][j] != 'A':
            continue
        if not (memory[i - 1][j - 1], memory[i + 1][j + 1]) in (('M', 'S'), ('S', 'M')):
            continue
        if not (memory[i + 1][j - 1], memory[i - 1][j + 1]) in (('M', 'S'), ('S', 'M')):
            continue
        mas_result += 1

print("\n\033[0m\033[37mThe number of 'X-MAS' is:\033[0m\033[1m", mas_result)
