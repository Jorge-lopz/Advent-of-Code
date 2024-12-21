# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 09/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/9

# Read input file
with open('input.txt', 'r') as file:
    memory = list(map(int, file.read().strip()))

# FIRST PART: Sort the disk visual representation to leave all the free space at the end and compress the 'files'
j = 0
disk = []

for i, num in enumerate(memory):
    if i % 2 == 0:
        disk.extend([str(j)] * num)  # Extend list with repeated numbers
        j += 1
    else:
        disk.extend(['.'] * num)  # Extend list with dots

first_dot_index = disk.index('.')
last_non_dot_index = len(disk) - 1

while first_dot_index < last_non_dot_index:
    # Swap the first '.' with the last non-dot character
    disk[first_dot_index], disk[last_non_dot_index] = disk[last_non_dot_index], '.'
    first_dot_index = disk.index('.')
    last_non_dot_index -= 1

print('\n\033[37mThe checksum after compression is:\033[0m\033[1m',
      sum(int(char) * i if char != '.' else 0 for i, char in enumerate(disk)))

# SECOND PART: Similar to the first part but only moving whole files together (using imaginary numbers like "tuples")
disk = [memory[i - 2] + (1 - i % 2) * i * .5j for i in range(2, len(memory) + 2)]

left, right = 1, len(disk) - 1
while right > 0:
    left = 1

    while disk[right].imag == 0:  # Find the next file from the right
        right -= 1

    # Find the first free space, where the entire file can fit
    while left < len(disk) and not (disk[left].imag == 0 and disk[left].real >= disk[right].real):
        left += 1

    if left < len(disk) and left < right:  # Switch the file with the free space
        disk[left] -= disk[right].real
        disk[right - 1] += disk[right].real
        disk.insert(left, disk.pop(right))
    right -= 1

pos = checksum = 0
for n in disk:
    for _ in range(int(n.real)):
        if n.imag != 0:
            checksum += pos * (n.imag - 1)
        pos += 1

print('\n\033[0m\033[37mThe checksum after compression (without fragmentation) is:\033[0m\033[1m', int(checksum))
