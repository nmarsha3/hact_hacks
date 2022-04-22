import json

suits = ["hearts", "diamonds", "spades", "clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

cards = []
for suit in suits:
   for value in values:
      card = (value, suit)
      cards.append(card)

data = {"cards": cards}

with open('cards.json', 'w') as outfile:
   json.dump(data, outfile)
