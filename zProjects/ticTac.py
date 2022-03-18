# For game we need
#board
#display board
#play game
#the flow of the functions
#check Win
  #check Rew
  #check col
  #check diag
#check Tie
#flip player 0-X X-0
#--------GLOBAL VARS-------
game_ongoing= True
winner=None
current_player="X"

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

def display_board():
  print (board[0] + " | " +board[1] +" | "+board[2])
  print (board[3] + " | " +board[4] +" | "+board[5])
  print (board[6] + " | " +board[7] +" | "+board[8])
  
def play_game():
  #display board
  display_board()

  while game_ongoing:
    
    handleturn(current_player)

    checkifGameOver()
    flip_player()

  if winner=="X" or winner=="0":
   print(winner+" won")
  elif winner==None : 
   print(" TIE ") 
  # the game has ended
  
def handleturn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()

  
def checkifGameOver():
  checkwinner()
  checkTie()

def checkwinner():
  global winner
  #checkrows
  row_winner=checkrows()

  col_winner=checkcol()

  diag_winner=check_diag()

  if row_winner:
    winner=row_winner
  elif col_winner:
    winner=col_winner

  elif diag_winner:   
     winner=diag_winner
  else:
    winner=None
    
      
  return
def checkrows():

  #set up global variable
  global game_ongoing
  #check if rows are equal
  row_1=board[0]==board[1]==board[2] != "-"
  row_2=board[3]==board[4]==board[5] != "-"
  row_3=board[6]==board[7]==board[8] != "-"

  if row_1 or row_2 or row_3:
    game_ongoing=False
  if row_1:
    return board[0]
  elif row_2:  
    return board[3]
  elif row_3:
    return board[6]
  return

  
def checkcol():

  global game_ongoing
  #check if rows are equal
  col_1=board[0]==board[3]==board[6] != "-"
  col_2=board[1]==board[4]==board[7] != "-"
  col_3=board[2]==board[5]==board[8] != "-"
  
  if col_1 or col_2 or col_3:
    game_ongoing=False
  if col_1:
    return board[0]
  elif col_2:  
    return board[1]
  elif col_3:
    return board[2]
  return
def check_diag():
  
  global game_ongoing
  #check if rows are equal
  d_1=board[0]==board[4]==board[8] != "-"
  d_2=board[6]==board[4]==board[2] != "-"
  
  if d_1 or d_2:
    game_ongoing=False
  if d_1:
    return board[0]
  elif d_2:  
    return board[2]
  return

  
def checkTie():
  global game_ongoing

  if "-" not in board:
    game_ongoing=False
  return

def flip_player():
  global current_player
  if current_player=="X":
      current_player="O"
  elif current_player=="O":
      current_player="X"
  return  
play_game()
#