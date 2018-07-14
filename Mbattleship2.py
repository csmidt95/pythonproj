from time import sleep

board1 = [] #what player 2 would see
board2 = [] #what player 1 would see

for x in range(5):
  board1.append(["O"] * 5) #creating the board
  
for x in range(5):
  board2.append(["O"] * 5)

def print_board(board): #stylizing the board
  for row in board:
    print (" ".join(row))
 
def player_row_choice(player): #placing piece
    row = int(input("Player %s, choose a row from 0 to 4: " % player))
    return row

def player_col_choice(): #placing piece
    col = int(input("Now, choose a column from 0 to 4: "))
    return col 
    
def guessing_row(player):
    guess_row = int(input("Player %s, guess the row! " % player))
    return guess_row
    
def guessing_col():
    guess_col = int(input("Now, guess the column! "))
    return guess_col
  
def play_game():
    game = 3
    player_1_row = player_row_choice(1) #choosing placement
    player_1_column = player_col_choice()
    player_2_row = player_row_choice(2)
    player_2_column = player_col_choice()
    while game == 3:
      check = turn(board2, player_2_row, player_2_column, 1)   
      if check == 4:
          break
      check = turn(board1, player_1_row, player_1_column, 2)
      if check == 4:
          break
      
def turn(board, player_row, player_col, player):
     print("")
     print_board(board)     
     player_guess_row = guessing_row(player)    
     player_guess_col = guessing_col()        
     if player_guess_row == player_row and player_guess_col == player_col:
         print ()
         print ("CONGRATS")
         sleep(1)
         print ("Player %s, you win!" % player)
         game = 4
         return game
     elif player_guess_row > 4 or player_guess_col > 4:
         print()
         print("You're not even in the ocean!")
         turn(board, player_row, player_col, player)
     elif board[player_guess_row][player_guess_col] == "X":
         print("")
         print("You already guessed that!")   
         turn(board, player_row, player_col, player)     
     else:
         print ("")
         print("You missed!")
         board[player_guess_row][player_guess_col] = "X"
         print_board(board)
         sleep(2)
play_game()



    
    
























