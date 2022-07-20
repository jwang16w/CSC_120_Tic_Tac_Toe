board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']] 
# this list contains 3 lists, each of 3 elements, each element being a single character

isValid = True

currentPlayer = 0
currentMark = 'X'

def print_board():
   print("Printing board")
   for myList in board:
      print(myList)
   pass

def check_mark(r, c, m):
   if (r<0 or r>2) or (c<0 or c>2):
      print("**** Invalid row or column. Please select row / column between 0 and 2 ****")
      print("**** Invalid choice. Please mark again! ****")
      return False
   if board[r][c] != '-':
      print("**** Board[",r,"][",c,"] has already been selected. Please select somewhere else. ****")
      print("**** Invalid choice. Please mark again! ****")
      return False
   return True

def place_mark(currentPlayer, currentMark):
   print("Player ", currentPlayer+1, " make your move")
   row = int(input("Enter row number (0-2):"))
   col = int(input("Enter column number (0-2):"))
   if check_mark(row, col, currentMark) == False:
     return
   board[row][col] = currentMark
   print("\n")
   print("Player ", currentPlayer+1, " added mark at the location ", row, ",", col)
   pass

def check_win():
   pass

def main():
   done = False
   cPlayer = 0
   cMark = 'X'
   print_board()

   while done == False:

    place_mark(cPlayer, cMark)
    print_board()
    if cPlayer == 0:
        cPlayer = 1
        cMark = 'O'
    else:
        cPlayer = 0
        cMark = 'X'

main()