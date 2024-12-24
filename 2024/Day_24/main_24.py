# --------------------------------------------------------------------------- #
#                                                                             #
#     main_24.py                               ::::             ::::::::      #
#                                            ++: :+:          :+:    :+:      #
#     PROJECT: Advent of Code              #:+   +:+         +:+              #
#                                        +#++:++#++:        +#+               #
#                                       +#+     +#+  ++::  +#+                #
#     AUTHOR: Jorge Lopez Puebla       ##+     #+#  #   # #+#    #+#          #
#     LAST UPDATE: 24/12/2024         ###     ###   ####  ########            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/24 🚪

# IMPORTS
from collections import deque  # -> Double ended queue

wires, gates = {}, []

with open("input.txt", "r") as f:
    for line in f.readlines():
        if ":" in line:  # Initial wire
            wire, value = line.split(": ")
            wires[wire.strip()] = int(value.strip())
        elif "->" in line:  # Gate
            inputs, output = line.split(" -> ")
            gate_parts = inputs.split(" ")
            gates.append({
                'inputs': [gate_parts[0], gate_parts[2]],
                'operation': gate_parts[1],
                'output': output.strip()
            })

wire_states = wires  # Use initial wire values
dependencies, dependents = {}, {}
queue = deque()

for gate in gates:  # Build dependency graph
    input1, input2, output, operation = gate['inputs'][0], gate['inputs'][1], gate['output'], gate['operation']
    dependencies[output] = (input1 not in wire_states) + (input2 not in wire_states)

    for input_wire in [input1, input2]:
        if input_wire not in wire_states:
            dependents.setdefault(input_wire, []).append(gate)

    if dependencies[output] == 0:  # Add to the queue if no dependencies remain
        queue.append(gate)

while queue:  # Process ready gates
    gate = queue.popleft()
    input1, input2, output, operation = gate['inputs'][0], gate['inputs'][1], gate['output'], gate['operation']
    val1, val2 = wire_states[input1], wire_states[input2]

    # Perform the gate operation (AND -> &, OR -> |, XOR -> ^)
    wire_states[output] = val1 & val2 if operation == "AND" else val1 | val2 if operation == "OR" else val1 ^ val2

    for dependent in dependents.get(output, []):
        dep_output = dependent['output']
        dependencies[dep_output] -= 1
        if dependencies[dep_output] == 0:
            queue.append(dependent)

# FIRST PART: Get the decimal encoded gate states after all logic gates evaluation (sequential because of dependencies)

z_wires = {key: value for key, value in wire_states.items() if key.startswith('z')}
result = int(''.join(str(z_wires[f"z{i:02}"]) for i in reversed(range(len(z_wires)))), 2)

print("\n\033[37mThe decimal encoded gate states is:\033[0m\033[1m", result)

# SECOND PART: Get the swapped wires
