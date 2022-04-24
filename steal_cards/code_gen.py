#!/usr/bin/env python3

# Script to generate json file of conversions from freecell card codes (0-51) to our tuple codes
import json


FILE = "card_codes.json"
card_codes = {}

x = 0

for i in ["A"] + list(map(str, range(2,11))) + ["J","Q","K"]:
    for j in ["clubs","diamonds","hearts","spades"]:
        card_codes[x] = (i,j)
        x += 1

with open(FILE, 'w') as outfile:
    outfile.write(json.dumps(card_codes, indent=4))
