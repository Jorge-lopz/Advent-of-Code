# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 06/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/6

memory: [[str]] = []

# Read input f
def get_map():
    global memory
    memory = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            memory.append([char for char in line])

def get_guard():
    for row, line in enumerate(memory):
        for col, char in enumerate(line):
            if char in GUARD_CHARS:
                return [row, col]

# FIRST PART: Get the number of unique cells the guard will visit
GUARD_CHARS = ['^', '>', 'v', '<']

get_map()
guard: [int, int] = get_guard()
orientation = memory[guard[0]][guard[1]]

while 0 <= guard[0] < len(memory) and 0 <= guard[1] < len(memory[0]):
    memory[guard[0]][guard[1]] = 'X'
    match orientation:
        case '^':
            if memory[guard[0] - 1][guard[1]] in 'X.':
                guard[0] -= 1
            else:
                orientation = '>'
        case '>':
            if memory[guard[0]][guard[1] + 1] in 'X.':
                guard[1] += 1
            else:
                orientation = 'v'
        case 'v':
            if memory[guard[0] + 1][guard[1]] in 'X.':
                guard[0] += 1
            else:
                orientation = '<'
        case '<':
            if memory[guard[0]][guard[1] - 1] in 'X.':
                guard[1] -= 1
            else:
                orientation = '^'

unique_cells = sum(line.count('X') for line in memory)

print("\n\033[0m\033[37mThe number of unique cells the guard will visit is:\033[0m\033[1m", unique_cells)

# SECOND PART: 1933 Find the number of possible single obstacle positions that make the guard loop forever
# block_count = 0
#
# guard: [int, int] = get_guard()
# step_limit = 10_000  # Optional safeguard to prevent excessive iterations
#
# for position in [[row, col] for row in range(len(memory)) for col in range(len(memory[0]) - 1)]:
#     if position == guard:  # Cannot block the guard position
#         continue
#     get_map()
#     guard: [int, int] = get_guard()
#     orientation = memory[guard[0]][guard[1]]
#     memory[position[0]][position[1]] = '#'
#
#     visited_positions = []  # Track visited states as a list to identify cycles
#     steps = 0
#     while 0 <= guard[0] < len(memory) and 0 <= guard[1] < len(memory[0]):
#         state = (tuple(guard), orientation)
#
#         # Check for a repeated state forming a cycle
#         if state in visited_positions:
#             cycle_start = visited_positions.index(state)
#             cycle_length = len(visited_positions) - cycle_start
#             # Validate the cycle by ensuring it repeats consistently
#             if visited_positions[-cycle_length:] == visited_positions[cycle_start:]:
#                 block_count += 1
#                 break
#
#         visited_positions.append(state)
#         steps += 1
#         if steps > step_limit:
#             break  # Prevent excessive iterations in large grids
#
#         match orientation:
#             case '^':
#                 if memory[guard[0] - 1][guard[1]] in 'X.':
#                     guard[0] -= 1
#                 else:
#                     orientation = '>'
#             case '>':
#                 if memory[guard[0]][guard[1] + 1] in 'X.':
#                     guard[1] += 1
#                 else:
#                     orientation = 'v'
#             case 'v':
#                 if guard[0] + 1 < len(memory) and memory[guard[0] + 1][guard[1]] in 'X.':
#                     guard[0] += 1
#                 else:
#                     orientation = '<'
#             case '<':
#                 if memory[guard[0]][guard[1] - 1] in 'X.':
#                     guard[1] -= 1
#                 else:
#                     orientation = '^'
#
# print("\n\033[0m\033[37mThe number of obstacle positions to make the guard loop forever is:\033[0m\033[1m", block_count)
