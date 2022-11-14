import numpy as np
board = np.zeros((3,3))
board[0][0] = 1
board[0][1] = 1
print(board)


def computer():
    global board
    if (np.sum(board,1) == 2): #if sum is 2
        board[board[0:1]<1] = 5 #make the square 5
       
        print(board)
    else:
        print("o") 



computer()

# board[board[0:1] < 1] = 5
      #  np.where(board[0,:] < 1,5,1)


# def computer_turn():
   # move = random.randint(1,10)
    #print(move)
    #if move == 1 and board[0][0] == 0:
 #       board[0][0] = 5
 #       screen.blit(feather_img, (20, 20))
 #       pg.display.flip() 
 #       raventurn = 0
 #   elif move == 1 and board[0][0] != 0: 
 #       computer_turn()
  #  elif move == 2 and board[0][1] = =0:
  #      board[0][1] = 5
  #      screen.blit(feather_img, (20, 20))
  #      pg.display.flip() 
  #      raventurn = 0
  #  elif move == 2 and board[0][1] != 0:
  #      computer_turn()
  #  elif move == 3 and board[0][2] = 0:
  #      board[0][2] = 5
  #      screen.blit(feather_img, (20, 20))
  #      pg.display.flip() 
  #      raventurn = 0
  #  elif move == 3 and board[0][2] != 0:
   #     computer_turn()
    
    
 #   row1 = board[0]
 #   row2 = board[1]
 #   row3 = board[2]
 #   if (np.sum(row1)== 2):
 #       board[0][2] = 5
 #   elif (np.sum(row2) ==2):
 #       board



   
   
   
    #if (np.sum(board,1) == 2):
        
    
    #or any(np.sum(board,0)==2) or sum(np.diag(board))==2 or sum(np.diag(board[::-1]))==2:
