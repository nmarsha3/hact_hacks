from shutil import move
from Freecell import Freecell
import sys

def main():

   # Create game object
   f = Freecell()

   # here we will import the gamestate, for now we generate a random board
   f.build_random_board()
   # rig the board for testing purposes
   f.columns[0][6] = ["1", "hearts"]

   f.columns[3].pop()
   f.final_spades.append(("1", "spades"))
   f.columns[3].append(("2", "hearts"))

   f.freecells.append(("1", "diamonds"))
   f.print_board()

   find_best_move(f)

   f.print_board()

   #f.print_board()


def find_best_move(f):
  # check if board is solved (i.e if the final decks are all of size 13)
   if(len(f.final_clubs) == 13 and len(f.final_diamonds) == 13 and len(f.final_hearts) == 13 and len(f.final_spades) == 13):
      return

   # try move 1
   if try_move_1(f):
      find_best_move(f)
   elif try_move_2(f):
      find_best_move(f)
   else:
      print("Oh no! I'm stuck!")
   
   f.print_board()

# move 1: move a card from the top of a column to the foundation
def try_move_1(f):

   for column in f.columns:
      if len(column) > 0:
         # current card we are on
         card = column[-1]
         # check if card is the next heart
         if card[1] == "hearts":
            if len(f.final_hearts) > 0 and int(card[0]) - 1 == int(f.final_hearts[-1][0]):
               f.move(column, f.final_hearts)
               return True
            elif len(f.final_hearts) == 0 and card[0] == "1":
               f.move(column, f.final_hearts)
               return True

         # check if card is the next clubs
         if card[1] == "clubs":
            if len(f.final_clubs) > 0 and int(card[0]) - 1 == int(f.final_clubs[-1][0]):
               f.move(column, f.final_clubs)
               return True
            elif len(f.final_clubs) == 0 and card[0] == "1":
               f.move(column, f.final_clubs)
               return True
         # check if card is the next spades
         if card[1] == "spades":
            if len(f.final_spades) > 0 and int(card[0]) - 1 == int(f.final_spades[-1][0]):
               f.move(column, f.final_spades)
               return True
            elif len(f.final_spades) == 0 and card[0] == "1":
               f.move(column, f.final_spades)
               return True
         # check if card is the next diamonds
         if card[1] == "diamonds":
            if len(f.final_diamonds) > 0 and int(card[0]) - 1 == int(f.final_diamonds[-1][0]):
               f.move(column, f.final_diamonds)
               return True
            elif len(f.final_diamonds) == 0 and card[0] == "1":
               f.move(column, f.final_diamonds)
               return Trudiamonds
      
   return False
         
            
   
'''
   # hearts
   h_len = len(f.final_hearts)
   if h_len > 0:
      c = f.final_hearts[len(f.final_hearts)-1]
      print(f.final_hearts[len(f.final_hearts)-1])
      c[0] = str(int(c[0]) + 1)
   else:
      c = ["2", "hearts"]

   print("looking for: ", c)
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_hearts)
         return True

   # diamonds
   if len(f.final_diamonds) > 0:
      c = f.final_diamonds[len(f.final_diamonds)-1]
   else:
      c = ["2", "diamonds"]
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_diamonds)
         return True

   # clubs
   if len(f.final_clubs) > 0:
      c = f.final_clubs[len(f.final_clubs)-1]
   else:
      c = ["2", "clubs"]
   print("looking for: ", c)
   for column in f.columns:
      current_card = column[len(column)-1]
      if current_card[0] == c[0] and current_card[1] == c[1]:
         f.move(column, f.final_clubs)
         return True

   # spades
   if len(f.final_spades) > 0:
      c = f.final_spades[len(f.final_spades)-1]
   else:
      c = ["2", "spades"]
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_spades)
         return True
   '''

# move 2: move a card from a freecell to the foundations
def try_move_2(f):
   for card in f.freecells:
      num = int(card[0])
      suit = card[1]
      if suit == "hearts":
         length = len(f.final_hearts)
         if length > 0 and (int(f.final_hearts[-1][0]) + 1 == num):
            f.move_from_cell(card, f.final_hearts)
         elif num == 1:
            f.move_from_cell(card, f.final_hearts)
      if suit == "diamonds":
         length = len(f.final_diamonds)
         if length > 0 and (int(f.final_diamonds[-1][0]) + 1 == num):
            f.move_from_cell(card, f.final_diamonds)
         elif num == 1:
            f.move_from_cell(card, f.final_diamonds)


def try_move_3(f):
   pass

def try_move_4(f):
   pass

def try_move_5(f):
   pass

def try_move_6(f):
   pass

def try_move_7(f):
   pass

def try_move_8(f):
   pass

def try_move_9(f):
   pass

if __name__ == "__main__":
   main()