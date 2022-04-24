import json
import random

class Freecell:

   def __init__(self, card_file="cards.json"):

      # Get card data and init cards
      with open(card_file) as f:
         data = json.load(f)

      card_data = data["cards"]
      self.cards = [tuple(c) for c in card_data]

      # init columns
      self.columns = [[] for x in range(8)]

      '''
      self.column2 = list()
      self.column3 = list()
      self.column4 = list()
      self.column5 = list()
      self.column6 = list()
      self.column7 = list()
      self.column8 = list()
      '''

      # init final piles
      self.final_hearts = list()
      self.final_diamonds = list()
      self.final_spades = list()
      self.final_clubs = list()

      # init free cells
      self.freecells = set()

   def build_random_board(self):
      ''' This method will be used before we know how to get gamestate from exe '''

      # Shuffle the cards
      random.shuffle(self.cards)

      # fill in each column

      for column in self.columns:
         for i in range(0,7):
            column.append(self.cards[i])
      '''
      for i in range(0, 7):
         self.column1.append(self.cards[i])
      for i in range(7, 14):
         self.column2.append(self.cards[i])
      for i in range(14, 21):
         self.column3.append(self.cards[i])
      for i in range(21, 28):
         self.column4.append(self.cards[i])
      for i in range(28, 34):
         self.column5.append(self.cards[i])
      for i in range(34, 40):
         self.column6.append(self.cards[i])
      for i in range(40, 46):
         self.column7.append(self.cards[i])
      for i in range(46, 52):
         self.column8.append(self.cards[i])
      '''
   def print_board(self):
      print("Freecells: ")
      print(self.freecells)
      print("Final hearts: ")
      print(self.final_hearts)
      print("Final diamonds: ")
      print(self.final_diamonds)
      print("Final spades: ")
      print(self.final_spades)
      print("Final clubs: ")
      print(self.final_clubs)
      print()

      i = 0
      for column in self.columns:
         print(i)
         print(column)
         i+=1
      '''
      print("Column 1: ")
      print(self.column1)
      print("Column 2: ")
      print(self.column2)
      print("Column 3: ")
      print(self.column3)
      print("Column 4: ")
      print(self.column4)
      print("Column 5: ")
      print(self.column5)
      print("Column 6: ")
      print(self.column6)
      print("Column 7: ")
      print(self.column7)
      print("Column 8: ")
      print(self.column8)'''

   def move(self, source, destination):
      ''' move the specified card to the specified destnaiton'''      ''' CURRENTLY DOES NO CHECKS ON IF MOVE IS VALID OR NOT '''
      ''' CURRENTLY DOES NOT REMOVE CARD FROM CURRENT LOCATION '''

      card = source.pop()
      destination.append(card)
      
      '''
      if destination == 1:
         self.column1.append(card)
      if destination == 2:
         self.column2.append(card)
      if destination == 3:
         self.column3.append(card)
      if destination == 4:
         self.column4.append(card)
      if destination == 5:
         self.column5.append(card)
      if destination == 6:
         self.column6.append(card)
      if destination == 7:
         self.column7.append(card)
      if destination == 8:
         self.column8.append(card)

      if destination == "freecell":
         self.freecell.add(card)
      if destination == "final_hearts":
         self.final_hearts.append(card)
      if destination == "final_diamonds":
         self.final_diamonds.append(card)
      if destination == "final_spades":
         self.final_spades.append(card)
      if destination == "final_clubs":
         self.final_clubs.append(card)
      '''

   def get_gamestate_from_exe(self):
      pass