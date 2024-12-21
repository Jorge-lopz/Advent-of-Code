# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 02/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/2

rows: [[int]] = []

# Read the input
with open('input.txt', 'r') as file:
    for line in file.readlines():
        rows.append(list(map(int, line.split())))

# FIRST PART: Count the safe reports (5 long, either all increasing or decreasing and adjacent differ 1-3 units)
safe_reports: int = 0
for row in rows:
    if (
            (row == sorted(row) or row == sorted(row, reverse=True)) and
            all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))
    ):
        safe_reports += 1

print("\n\033[37mThe number of safe reports is:\033[0m\033[1m", safe_reports)

# SECOND PART: Same as part one but now one single record can be removed from any report, making more reports safe
safe_reports: int = 0

for row in rows:
    # Check if the report is already safe
    if (
            (row == sorted(row) or row == sorted(row, reverse=True)) and
            all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))
    ):
        safe_reports += 1
        continue

    # Check if removing one record makes the report safe
    for i in range(len(row)):
        m_row = row[:i] + row[i + 1:]
        if (
                (m_row == sorted(m_row) or m_row == sorted(m_row, reverse=True)) and
                all(1 <= abs(m_row[j] - m_row[j + 1]) <= 3 for j in range(len(m_row) - 1))
        ):
            safe_reports += 1
            break

print("\n\033[37mThe number of safe reports (allowing one record removal) is:\033[0m\033[1m", safe_reports)
