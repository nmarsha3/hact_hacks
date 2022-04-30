from operator import truediv
from shutil import move
from Freecell import Freecell
import sys

def main():

   # Create game object
   f = Freecell()

   # loads cards from memory, assumes process is already running!!!!
   # f.get_gamestate_from_exe()

   # test move 8
   f.build_random_board()
   f.columns[0].pop()
   f.columns[0].pop()
   f.columns[0].pop()
   f.columns[0].append([1, "hearts"])
   f.columns[0].append([3, "clubs"])
   f.columns[0].append([6, "diamonds"])


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
   
   if try_move_8(f):
      find_best_move(f)
   else:
      print("Oh no! I'm stuck!")
      f.print_board()
      return

   # if try_move_1(f):
   #    find_best_move(f)
   # elif try_move_2(f):
   #    find_best_move(f)
   # elif try_move_3(f):
   #    find_best_move(f)
   # elif try_move_6(f):
   #    find_best_move(f)
   # elif try_move_8(f):
   #    find_best_move(f)
   # elif try_move_9(f):
   #    find_best_move(f)
   # elif move_to_cell(f):
   #    find_best_move(f)
   # else:
   #    print("Oh no! I'm stuck!")
   
   # f.print_board()

def can_stack(source_card, dest_card):
   print(source_card)
   print(dest_card)
   if source_card[0] == int(dest_card[0]) - 1:
      if (source_card[1] == "diamonds" or source_card[1] == "hearts") and (dest_card[1] == "clubs" or dest_card[1] == "spades"):
         return True
      if (source_card[1] == "clubs" or source_card[1] == "spades") and (dest_card[1] == "diamonds" or dest_card[1] == "hearts"):
          return True
   return False

# when there is nothing else to try, check if you can move an arbitrary card into the freecells
def move_to_cell(f):
   if len(f.freecells) == 4:
      return False
   for column in f.columns:
      if len(column) == 0:
         continue
      else:
         f.move_to_cell(column, f.freecells)
         return True
   return False

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

# move a sequence of cards from the top of a column to a parent card on a different column
def try_move_4(f):
   # iterate over cols
   for c in f.columns:
      # get to first card
      first = 0
      seq = first

      # set first cards 
      pre_card = int(c[first][0])
      pre_suit = c[first][1]

      # iterate over cards in col to see if they are a seq
      for i in range(1, len(c), 1):
         cur_card = int(c[i][0])
         cur_suit = c[i][1]

         # check if the cards break the color pattern 
         if (cur_suit == "spades" or cur_suit == "clubs") and (pre_suit == "spades" or pre_suit == "clubs"):
            break
         if (cur_suit == "hearts" or cur_suit == "diamonds") and (pre_suit == "hearts" or pre_suit == "diamonds"):
            break

         # check to see if cur_card is not one greater than pre_card
         if cur_card != (pre_card - 1):
            break
         
         # reset pre_card and pre_suit
         pre_card = cur_card
         pre_suit = cur_suit

         # decrement seq
         seq += 1

      # check to see if seq is the length of the full col 
      if seq == (len(c) - 1):
         # find a parent card for seq
         top = c[seq]
         for dest in f.columns:
            bot = dest[-1]
            stack = can_stack(top, bot)
            # if we can stack then move the seq
            if stack:
               # TODO: move the sequence to parent card of new col
               move_seq(c, 0, dest)
               return True
   
   return False

# move a sequence of cards from the top of a column to an empty stack
def try_move_5(f):
   # iterate over cols
   for c in f.columns:
      # get to first card
      first = 0
      seq = first

      # set first cards 
      pre_card = int(c[first][0])
      pre_suit = c[first][1]

      # iterate over cards in col to see if they are a seq
      for i in range(1, len(c), 1):
         cur_card = int(c[i][0])
         cur_suit = c[i][1]

         # check if the cards break the color pattern 
         if (cur_suit == "spades" or cur_suit == "clubs") and (pre_suit == "spades" or pre_suit == "clubs"):
            break
         if (cur_suit == "hearts" or cur_suit == "diamonds") and (pre_suit == "hearts" or pre_suit == "diamonds"):
            break

         # check to see if cur_card is not one greater than pre_card
         if cur_card != (pre_card - 1):
            break
         
         # reset pre_card and pre_suit
         pre_card = cur_card
         pre_suit = cur_suit

         # decrement seq
         seq += 1

      # check to see if seq is the length of the full col 
      if seq == (len(c) - 1):
         # find an empty column to move card to
         for dest in f.columns:
            if len(dest) == 0:
               # TODO: move the sequence to parent card of new col
               move_seq(c, 0, dest)
               return True
   
   return False
      

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

# move a sequence of cards that is already on top of a valid parent to a different parent
def try_move_7(f):
   # iterate over cols
   for c in f.columns:
      # get to first card
      first = len(c) - 1
      pre_card = int(c[first][0])
      pre_suit = c[first][1]

      # set sequence
      seq = first

      # iterate over cards in col to find seq
      for i in range((first - 1), -1, -1):
         cur_card = int(c[i][0])
         cur_suit = c[i][1]

         # check if the cards break the color pattern 
         if (cur_suit == "spades" or cur_suit == "clubs") and (pre_suit == "spades" or pre_suit == "clubs"):
            break
         if (cur_suit == "hearts" or cur_suit == "diamonds") and (pre_suit == "hearts" or pre_suit == "diamonds"):
            break

         # check to see if cur_card is not one greater than pre_card
         if cur_card != (pre_card + 1):
            break
         
         # reset pre_card and pre_suit
         pre_card = cur_card
         pre_suit = cur_suit

         # decrement seq
         seq -= 1

      # check to see if seq != first, if != then a seq has been found 
      if seq != first:
         # find a parent to parent column
         seq_final = seq
         while (first - seq_final) >= 2:
            top = c[seq_final]
            for dest in f.columns:
               bot = dest[-1]
               stack = can_stack(top, bot)
               # if we can stack then move the seq
               if stack:
                  # TODO: move the sequence to parent card of new col
                  move_seq(c, seq_final, dest)
                  return True
            seq_final += 1
   
   return False

# move 8: move a cards that is hidden under some cards, into the foundations, by moving cards above it to vacant freecells and columns. 
def try_move_8(f):
   if len(f.final_hearts) == 0:
      next = [1, "hearts"]
   else:
      next = [f.final_hearts[-1] + 1, "hearts"]
   
   for col in f.columns:
      if next not in col:
         continue
      # try to uncover
      # iterate over all the cards in between the top of the col and next
      flag = False
      col_move = False
      cell_move = False
      while next != col[-1]:
         # check if a parent is free on another column
         for col2 in f.columns:
            if len(col2) == 0:
               col_move = False
               continue
            if can_stack(col[-1], col2[-1]):
               f.move(col, col2)
               print("MOVING PARENT TO NEW COLUMN")
               col_move = True
               continue
            else:
               col_move = False
         # check if a freecell is open
         if len(f.freecells) is not 4:
            f.move_to_cell(col, f.freecells)
            print("MOVING INTO FREECELLS")
            cell_move = True
         else:
            cell_move = False
         
         # if the card could not be moved to either column 
         if not cell_move and not col_move:
            return False

      if next == col[-1]:
         f.move(col, f.final_hearts)
         

   if len(f.final_diamonds) == 0:
      next_diamonds = [1, "diamonds"]
   else:
      next_diamonds = [(f.final_diamonds[-1] + 1), "diamonds"]

   for col in f.columns:
      if next not in col:
         continue
      # try to uncover
      # iterate over all the cards in between the top of the col and next
      flag = False
      col_move = False
      cell_move = False
      while next != col[-1]:
         # check if a parent is free on another column
         for col2 in f.columns:
            if len(col2) == 0:
               col_move = False
               continue
            if can_stack(col[-1], col2[-1]):
               f.move(col, col2)
               print("MOVING PARENT TO NEW COLUMN")
               col_move = True
               continue
            else:
               col_move = False
         # check if a freecell is open
         if len(f.freecells) is not 4:
            f.move_to_cell(col, f.freecells)
            print("MOVING INTO FREECELLS")
            cell_move = True
         else:
            cell_move = False
         
         # if the card could not be moved to either column 
         if not cell_move and not col_move:
            return False

      if next == col[-1]:
         f.move(col, f.final_diamonds)

   if len(f.final_clubs) == 0:
      next_clubs = [1, "clubs"]
   else:
      next_clubs = [f.final_dclubs[-1] + 1, "clubs"]

   for col in f.columns:
      if next not in col:
         continue
      # try to uncover
      # iterate over all the cards in between the top of the col and next
      flag = False
      col_move = False
      cell_move = False
      while next != col[-1]:
         # check if a parent is free on another column
         for col2 in f.columns:
            if len(col2) == 0:
               col_move = False
               continue
            if can_stack(col[-1], col2[-1]):
               f.move(col, col2)
               print("MOVING PARENT TO NEW COLUMN")
               col_move = True
               continue
            else:
               col_move = False
         # check if a freecell is open
         if len(f.freecells) is not 4:
            f.move_to_cell(col, f.freecells)
            print("MOVING INTO FREECELLS")
            cell_move = True
         else:
            cell_move = False
         
         # if the card could not be moved to either column 
         if not cell_move and not col_move:
            return False

      if next == col[-1]:
         f.move(col, f.final_clubs)
         
   if len(f.final_spades) == 0:
      next_spades = [1, "spades"]
   else:
      next_spades = [f.final_spades[-1] + 1, "spades"]
   
   for col in f.columns:
      if next not in col:
         continue
      # try to uncover
      # iterate over all the cards in between the top of the col and next
      flag = False
      col_move = False
      cell_move = False
      while next != col[-1]:
         # check if a parent is free on another column
         for col2 in f.columns:
            if len(col2) == 0:
               col_move = False
               continue
            if can_stack(col[-1], col2[-1]):
               f.move(col, col2)
               print("MOVING PARENT TO NEW COLUMN")
               col_move = True
               continue
            else:
               col_move = False
         # check if a freecell is open
         if len(f.freecells) is not 4:
            f.move_to_cell(col, f.freecells)
            print("MOVING INTO FREECELLS")
            cell_move = True
         else:
            cell_move = False
         
         # if the card could not be moved to either column 
         if not cell_move and not col_move:
            return False

      if next == col[-1]:
         f.move(col, f.final_spades)
   
   

# i think this needs to iterate over all the cards in the column, currently it only moves one card to the freecells
def try_move_9(f):
   # iterate through 
   for column in f.columns:
      if len(column) <= len(f.freecells) and len(column) != 0:
         f.move_to_cell(column, f.freecells)
         return True

   return False

if __name__ == "__main__":
   main()