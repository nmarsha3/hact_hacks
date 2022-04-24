from Freecell import Freecell
import sys

def main():

   # Create game object
   f = Freecell()

   # here we will import the gamestate, for now we generate a random board
   f.build_random_board()
   # rig the board for testing purposes
   f.columns[0][6] = ["2", "clubs"]

   f.columns[3][5] = ["3", "hearts"]
   f.final_hearts.append(["2", "hearts"])
   f.print_board()

   find_best_move(f)

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

# move 1: move a card from the top of a column to the foundation
def try_move_1(f):
 
   # hearts
   h_len = len(f.final_hearts)
   if h_len > 0:
      c = f.final_hearts[len(f.final_hearts)-1]
      c[0] = str(int(c[0]) + 1)
   else:
      c = ["2", "hearts"]
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_hearts)
         print("*****************moving card*******************")
         f.print_board()
         return True

   # diamonds
   if len(f.final_diamonds) > 0:
      c = f.final_diamonds[len(f.final_diamonds)-1]
   else:
      c = ["2", "diamonds"]
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_diamonds)
         print("*****************moving card*******************")
         f.print_board()
         return True

   # clubs
   print("TRYING TO MOVE 2 OF CLUBS")
   if len(f.final_clubs) > 0:
      c = f.final_clubs[len(f.final_clubs)-1]
   else:
      c = ["2", "clubs"]
   for column in f.columns:
      current_card = column[len(column)-1]
      print("CURRENT CARD")
      print(current_card)
      if current_card[0] == c[0] and current_card[1] == c[1]:
         f.move(column, f.final_clubs)
         print("*****************moving card*******************")
         f.print_board()
         return True
   print("failed")

   # spades
   if len(f.final_spades) > 0:
      c = f.final_spades[len(f.final_spades)-1]
   else:
      c = ["2", "spades"]
   for column in f.columns:
      if column[len(column)-1] == c:
         f.move(column, f.final_spades)
         print("*****************moving card*******************")
         f.print_board()
         return True


   return False

# move 2: move a card from a freecell to the foundations
def try_move_2(f):
   pass

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