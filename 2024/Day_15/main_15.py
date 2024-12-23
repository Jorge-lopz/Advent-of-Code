# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 14/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/15

# IMPORTS
from copy import deepcopy  # -> Deep copy

memory: [list[str]] = []
instructions: [str] = []

robot: (int, int) = ()  # (y, x)
boxes: int = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        if line == '\n':
            temp = ""
            for instruction_line in lines[y + 1:]:
                temp += instruction_line.strip()
            instructions = [char for char in temp]
            break
        temp = ""
        for x, char in enumerate(line.strip()):
            if char == '@':
                robot = (y, x)
                temp += '.'
                continue
            elif char == 'O':
                boxes += 1
            temp += char
        memory.append(list(temp))

# Original memory and robot for part 2
memory_2: [list[str]] = deepcopy(memory)
robot_2: (int, int) = deepcopy(robot)

def is_movable(box_position: (int, int)) -> bool:
    # A box is unmovable if any 2 adjacent cells (2 consecutive sides) are blocked
    row, col = box_position

    top: bool = (memory[row - 1][col] if row > 0 else '.') in "#0"
    left: bool = (memory[row][col - 1] if col > 0 else '.') in "#0"
    bottom: bool = (memory[row + 1][col] if row < len(memory) - 1 else '.') in "#0"
    right: bool = (memory[row][col + 1] if col < len(memory[0]) - 1 else '.') in "#0"

    return not ((top and left) or (top and right) or (left and bottom) or (bottom and right))

def lock_boxes():  # Check all boxes and lock them if they are unmovable
    global memory, boxes
    for y, row in enumerate(memory):  # Iterate once to unblock now movable boxes
        for x, char in enumerate(row):
            if char == '0':  # Box (unmovable)
                if is_movable((y, x)):
                    memory[y][x] = 'O'  # (movable)
                    boxes += 1
    for y, row in enumerate(memory):  # Iterate again to block any new unmovable boxes
        for x, char in enumerate(row):
            if char == 'O':  # Box (movable)
                if not is_movable((y, x)):
                    memory[y][x] = '0'  # (unmovable)
                    boxes -= 1

def move_robot(direction: (int, int)):
    global robot
    new_pos: (int, int) = (robot[0] + direction[0], robot[1] + direction[1])
    match memory[new_pos[0]][new_pos[1]]:
        case ('#' | '0'):  # Wall cell or box (unmovable)
            return
        case '.':  # Free cell
            robot = new_pos
        case 'O':  # Box cell (movable?)
            temp_pos: (int, int) = new_pos
            while True:  # Advance in the movement direction until a free cell or unmmovable block is found
                temp_pos = (temp_pos[0] + direction[0], temp_pos[1] + direction[1])
                if temp_pos[0] < 0 or temp_pos[0] >= len(memory) or temp_pos[1] < 0 or temp_pos[1] >= len(memory[0]):
                    return
                match memory[temp_pos[0]][temp_pos[1]]:
                    case ('#' | '0'):  # Wall cell or box (unmovable)
                        return
                    case '.':  # Free cell, so the box(es) are movable
                        break
            # Move the boxes and the robot
            while temp_pos != robot:
                previous_pos = (temp_pos[0] - direction[0], temp_pos[1] - direction[1])
                memory[temp_pos[0]][temp_pos[1]] = memory[previous_pos[0]][previous_pos[1]]  # Move the box
                lock_boxes()
                temp_pos = previous_pos
            # noinspection PyTypeChecker
            memory[temp_pos[0]][temp_pos[1]] = '.'
            lock_boxes()
            robot = new_pos

def print_map(memory: [list[str]], robot: (int, int)):
    print()
    print("\n".join([
        "".join(["".join(row[:robot[1]]), '@', "".join(row[robot[1] + 1:])])
        if i == robot[0] else "".join(row)
        for i, row in enumerate(memory)
    ]))

# FIRST PART: Find the sum of all the boxes GPS coordinates after the robot movements
for instruction in instructions:
    if instruction == '^':
        move_robot((-1, 0))
    elif instruction == 'v':
        move_robot((1, 0))
    elif instruction == '<':
        move_robot((0, -1))
    elif instruction == '>':
        move_robot((0, 1))
    if boxes == 0:  # No movable boxes left
        break

print("\n\033[37mThe sum of all the boxes GPS coordinates after the robot movements is:\033[0m\033[1m",
      sum(100 * y + x for y, row in enumerate(memory) for x, col in enumerate(row) if col in 'O0'))

# TODO - SECOND PART: Same as part one, but boxes and walls are now 2 wide (affects box pushing)
boxes_2: int = 0

print(
    "\n\033[0m\033[37mThe sum of all the boxes GPS coordinates after the robot movements in Part Two is:\033[0m\033[1m",
    sum(100 * (y if row[x] == '[]' else y + 1) + (x if row[x] == '[]' else x + 1)
        for y, row in enumerate(memory_2) for x, col in enumerate(row) if col == '[]'))
