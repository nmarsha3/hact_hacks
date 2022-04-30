import json
import random
import CardStealer

class Freecell:

   def __init__(self, card_file="cards.json"):

      # Get card data and init cards
      with open(card_file) as f:
         data = json.load(f)

      card_data = data["cards"]
      self.cards = [tuple(c) for c in card_data]

      # init columns
      self.columns = [[] for x in range(8)]

      # init final piles
      self.final_hearts = list()
      self.final_diamonds = list()
      self.final_spades = list()
      self.final_clubs = list()

      # init free cells
      self.freecells = list()

   def build_random_board(self):
      ''' This method will be used before we know how to get gamestate from exe '''

      # Shuffle the cards
      random.shuffle(self.cards)

      # fill in each column

      for column in self.columns:
         for i in range(0,7):
            column.append(self.cards[i])

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

   def move(self, source, destination):
      ''' move the specified card to the specified destnaiton'''      
      
      # print("source: ", source)
      # print("destination: ", destination)
      
      print("Recommended Move: ")
      print("move the ", source[-1])
      if len(destination) > 0:
         print("onto the ", destination[-1])
      else:
         print("onto the foundation pile")
      ans = input("did you complete the recommended move? (Y): ")
      destination.append(source.pop())
      
   def move_to_cell(self, source, destination):
      print("Recommended Move: ")
      print("move the ", source[-1])
      print("onto the freecells")
      # else:
      #    print("onto the foundation pile")
      ans = input("did you complete the recommended move? (Y): ")
      destination.append(source.pop())
      

   def move_from_cell(self, card, destination):
      if card in self.freecells:
         self.freecells.remove(card)
         destination.append(card)
      

   def get_gamestate_from_exe(self):
      self.columns = CardStealer.steal_cards()
