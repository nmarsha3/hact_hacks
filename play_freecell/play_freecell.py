from shutil import move
from Freecell import Freecell
import sys

def main():

   # Create game object
   f = Freecell()

   # loads cards from memory, assumes process is already running!!!!
   f.get_gamestate_from_exe()

   # print the start state
   f.print_board()

   # recursively finds the next best move
   find_best_move(f)


def test_cases(f):

   # here we will import the gamestate, for now we generate a random board
   f.build_random_board()
   # rig the board for testing purposes
   # testing move 1
   f.columns[1][6] = ["1", "hearts"]

   f.columns[0].pop()
   f.final_spades.append(("1", "spades"))
   f.columns[0].append(("2", "hearts"))

   # testing move 2
   f.freecells.append(("1", "diamonds"))

   # testing move 3
   f.freecells.append((4, "diamonds"))
   f.columns[3].pop()
   f.columns[3].append((5, "clubs"))
   
   # testing move 6
   f.columns.append(list())
   f.freecells.append(("8", "spades"))

   # testing move 9
   f.columns.append(list())
   f.columns[9].append(("7", "clubs"))
   
   f.print_board()

   find_best_move(f)

   f.print_board()


def find_best_move(f):
  # check if board is solved (i.e if the final decks are all of size 13)
   if(len(f.final_clubs) == 13 and len(f.final_diamonds) == 13 and len(f.final_hearts) == 13 and len(f.final_spades) == 13):
      return

   if try_move_1(f):
      find_best_move(f)
   elif try_sequence_move(f):
      find_best_move(f)
   elif try_move_2(f):
      find_best_move(f)
   elif try_move_3(f):
      find_best_move(f)
   elif try_move_6(f):
      find_best_move(f)
   elif try_move_9(f):
      find_best_move(f)
   elif move_to_cell(f):
      find_best_move(f)
   else:
      print("Oh no! I'm stuck!")
   
   f.print_board()

def can_stack(source_card, dest_card):
   if source_card[0] == dest_card[0] - 1:
      if (source_card[1] == "diamonds" or source_card[1] == "hearts") and (dest_card[1] == "clubs" or dest_card[1] == "spades"):
         return True
      if (source_card[1] == "clubs" or source_card[1] == "spades") and (dest_card[1] == "diamonds" or dest_card[1] == "hearts"):
          return True
   return False

def move_to_cell(f):
   for column in f.columns:
      if len(column) == 0:
         continue
      else:
         f.move(column, f.freecells)

def try_sequence_move(f):
   for source_col in f.columns:
      if len(source_col) == 0:
         continue
      for dest_col in f.columns:
         if len(dest_col) == 0:
            continue
         if can_stack(source_col[-1], dest_col[-1]):
            f.move(source_col, dest_col)

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
            elif len(f.final_clubs) == 0 and card[0] == 1:
               f.move(column, f.final_clubs)
               return True
         # check if card is the next spades
         if card[1] == "spades":
            if len(f.final_spades) > 0 and int(card[0]) - 1 == int(f.final_spades[-1][0]):
               f.move(column, f.final_spades)
               return True
            elif len(f.final_spades) == 0 and card[0] == 1:
               f.move(column, f.final_spades)
               return True
         # check if card is the next diamonds
         if card[1] == "diamonds":
            if len(f.final_diamonds) > 0 and int(card[0]) - 1 == int(f.final_diamonds[-1][0]):
               f.move(column, f.final_diamonds)
               return True
            elif len(f.final_diamonds) == 0 and card[0] == 1:
               f.move(column, f.final_diamonds)
               return True
      
   return False

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


# move 3: put a freecell card on top of a parent card, which is present on top of one of the columns. (this does not involve moving a card from a freecell to an empty column)
def try_move_3(f):
   # return bool
   r = False 

   # iterate over freecell cards 
   for cell in f.freecells:
      # get card and suit 
      fc_card = int(cell[0])
      fc_suit = cell[1]

      # check suit 
      if fc_suit == "spades" or fc_suit == "clubs":
         # iterate over columns 
         for column in f.columns:
            if len(column) == 0:
               continue
            current = column[len(column)-1]
            parent_card = int(current[0])
            parent_suit = current[1]

            # skip if spades or clubs 
            if parent_suit == "spades" or parent_suit == "clubs":
               continue
            
            #check if freecell card fits 
            if parent_card - 1 == fc_card:
               f.move_from_cell(cell, column)
               r = True 

      elif fc_suit == "hearts" or fc_suit == "diamonds":
         # iterate over columns 
         for column in f.columns:

            if len(column) == 0:
               continue
            current = column[len(column)-1]
            parent_card = int(current[0])
            parent_suit = current[1]

            # skip if spades or clubs 
            if parent_suit == "hearts" or parent_suit == "diamonds":
               continue
            
            #check if freecell card fits 
            if parent_card - 1 == fc_card:
               f.move_from_cell(cell, column)
               r = True
   return r

def try_move_4(f):
   pass

def try_move_5(f):
   pass

def try_move_6(f):
   # return bool
   r = False 

   # get number of occupied freecells 
   # num_fc = len(f.freecells)

   # create iterator for freecells 
   # i = 0
   
   # iterate over columns to find an empty one 
   for column in f.columns:
      if len(f.freecells) == 0:
         break

      if len(column) == 0:
         # move free cell to column and increment 
         f.move_from_cell(f.freecells[0], column)
         # i += 1
         r = True 

   return r

def try_move_7(f):
   pass

def try_move_8(f):
   pass

def try_move_9(f):
   # iterate through 
   for column in f.columns:
      if len(column) <= len(f.freecells) and len(column) != 0:
         f.move_to_cell(column, f.freecells)
         return True

   return False

if __name__ == "__main__":
   main()