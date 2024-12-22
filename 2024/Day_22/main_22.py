# --------------------------------------------------------------------------- #
#                                                                             #
#     main_22.py                               ::::             ::::::::      #
#                                            ++: :+:          :+:    :+:      #
#     PROJECT: Advent of Code              #:+   +:+         +:+              #
#                                        +#++:++#++:        +#+               #
#                                       +#+     +#+  ++::  +#+                #
#     AUTHOR: Jorge Lopez Puebla       ##+     #+#  #   # #+#    #+#          #
#     LAST UPDATE: 22/12/2024         ###     ###   ####  ########            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/22 🍌

with open('input.txt') as f:
    secrets = [int(line.strip()) for line in f.readlines()]

def transform(secret):
    secret ^= (secret * 64)
    secret %= 16777216
    secret ^= (secret // 32)
    secret %= 16777216
    secret ^= (secret * 2048)
    secret %= 16777216
    return secret

# FIRST PART: Get the sum of the 2000th secret code for every buyer after all transformation steps
result = 0
for secret in secrets:
    for _ in range(2000):
        secret = transform(secret)
    result += secret

print("\n\033[37mThe sum of the 2000th secret code for every buyer is:\033[0m\033[1m", result)

# SECOND PART: Get the maximum total number of bananas we can obtain based on the buyers' price change patterns

def price_changes(secret, steps):
    previous = secret
    prices, price_changes = [], []
    for _ in range(steps):
        actual = transform(previous)
        # Append the last digit (price) and the price change
        prices.append(actual % 10)
        price_changes.append(actual % 10 - previous % 10)

        previous = actual
    return prices, price_changes

def sequences(prices, price_changes):
    price_change_sequences = {}
    for i in range(3, len(price_changes)):
        sequence = tuple(price_changes[i - 3:i + 1])  # Extract a sequence of four consecutive price changes
        if sequence not in price_change_sequences:  # Only save sequences once
            price_change_sequences[sequence] = prices[i]
    return price_change_sequences

bananas = {}
for i, secret in enumerate(secrets):
    price, price_change = price_changes(secret, 2000)
    price_change_sequences = sequences(price, price_change)
    for seq, price in price_change_sequences.items():
        bananas[seq] = bananas.get(seq, 0) + price

print("\n\033[0m\033[37mThe max number of bananas we can buy is:\033[0m\033[1m", max(bananas.values()))
