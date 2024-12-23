# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 05/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/5

memory: [str]

# Read input f
with open('input.txt', 'r') as f:
    memory = f.readlines()

# Find the divider between rules and updates
divider = next((i for i in range(len(memory)) if ',' in memory[i]), len(memory))
rules_lines = memory[:divider]
updates_lines = memory[divider:]

rules = [(int(x), int(y)) for rule in rules_lines if '|' in rule for x, y in [rule.split('|')]]
updates = [[int(num) for num in update.split(',')] for update in updates_lines]

def validate_update(ordering_rules, update):
    positions = {page: idx for idx, page in enumerate(update)}
    for x, y in ordering_rules:
        if x in positions and y in positions and positions[x] > positions[y]:
            return False
    return True

def topological_sort(ordering_rules, update):
    graph = {page: [] for page in update}
    in_degree = {page: 0 for page in update}

    for x, y in ordering_rules:
        if x in graph and y in graph:
            graph[x].append(y)
            in_degree[y] += 1

    queue = [node for node in update if in_degree[node] == 0]
    sorted_order = []

    while queue:
        current = queue.pop(0)
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

valid_updates = []
incorrect_updates = []

for update in updates:
    is_valid = True
    positions = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions and positions[x] > positions[y]:
            incorrect_updates.append(update)
            is_valid = False
            break
    if is_valid:
        valid_updates.append(update[len(update) // 2])

sum_correct_middle = sum(valid_updates)
print("\n\033[37mThe sum of valid updates is:\033[0m\033[1m", sum_correct_middle)

reordered_updates = [topological_sort(rules, update) for update in incorrect_updates]
sum_reordered_middle = sum(update[len(update) // 2] for update in reordered_updates)
print("\n\033[0m\033[37mThe sum of reordered updates is:\033[0m\033[1m", sum_reordered_middle)
