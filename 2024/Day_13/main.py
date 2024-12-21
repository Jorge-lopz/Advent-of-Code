# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 13/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/13

memory: [{}] = []

with open('input.txt', 'r') as file:
    while True:
        lines = [file.readline().strip() for _ in range(4)]  # 4 to read the blank line after every option
        if not all(lines[:2]):  # Stop if any line is missing (apart form the blank line at the end) (EOF)
            break
        option = {}
        # Get the two buttons movement values
        keys = ["A", "B"]
        for line in range(2):
            parts = lines[line].split(',')
            option[keys[line]] = (int(parts[0][parts[0].index('+') + 1:]), int(parts[1][parts[1].index('+') + 1:]))
        # Get the prize position
        parts = lines[2].split(',')
        option["Prize"] = (int(parts[0][parts[0].index('=') + 1:]), int(parts[1][parts[1].index('=') + 1:]))
        memory.append(option)

def solve(A: (int, int), B: (int, int), prize: (int, int), conversion_error=0):
    aX, aY = A
    bX, bY = B
    pX, pY = prize
    tokens = 0

    pX += conversion_error
    pY += conversion_error

    a = round((pY / bY - pX / bX) / (aY / bY - aX / bX))
    b = round((pX - a * aX) / bX)

    if a * aX + b * bX == pX and a * aY + b * bY == pY:
        tokens += 3 * a + b

    return tokens

solved_machines = []
solved_bigger_machines = []
for machine in memory:
    # FIRST PART: Find the sum of minimum costs of every solvable machine
    p1_tokens = solve(machine["A"], machine["B"], machine["Prize"])
    if p1_tokens:
        solved_machines.append(p1_tokens)

    # SECOND PART: Find the sum of minimum costs of every solvable machine (with higher max presses and positions)
    p2_tokens = solve(machine["A"], machine["B"], machine["Prize"], 10_000_000_000_000)
    if p2_tokens:
        solved_bigger_machines.append(p2_tokens)

print(f"\n\033[0m\033[37mThe total minimum cost is:\033[0m\033[1m {sum(solved_machines)}")

print(f"\n\033[0m\033[37mThe total minimum cost (bigger machines) is:\033[0m\033[1m {sum(solved_bigger_machines)}")
