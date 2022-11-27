global N
N = 4
x,y = 0,1
board = [[0 for _ in range(N)] for _ in range(N)]
board[x][y] = 1
  
def printSolution(board): 
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print() 
  

def isSafe(board, row, col):
  
    if 1 in board[row]:
            return False
    
    for i in range(N):
        if board[i][col] == 1:
            return False

    x1 = row
    y1 = col 
    if col < row:
        y1 = 0
        x1 = row - col
    else:
        x1 = 0
        y1 = col - row 
    while(x1 < N and y1 <N):
        if board[x1][y1] == 1:
            return False
        x1 = x1 + 1 
        y1 = y1 + 1
    
    x1 = row
    y1 = col
    
    
    while(x1 < N and y1 <N and x1 >= 0 and y1 >= 0):
        if board[x1][y1] == 1:
            return False
      
        
        x1 = x1 - 1
        y1 = y1 + 1 

    x1 = row
    y1 = col
    
    while(x1 < N and y1 <N and x1 >= 0 and y1 >= 0):
        if board[x1][y1] == 1:
            return False
        x1 = x1 + 1
        y1 = y1 - 1 
    
    return True
  
def solveNQUtil(board, col):
      

    if col >= N:
        return True
    if col == y:
            return solveNQUtil(board, col + 1)
  

    for i in range(N):
        if i == x:
            pass
  
        if isSafe(board, i, col):
              
   
            board[i][col] = 1
  
            if solveNQUtil(board, col + 1) == True:
                return True
  
     
            board[i][col] = 0
  
 
    return False
  

  
if solveNQUtil(board, 0) == False:
    print ("Solution does not exist")
else:
    printSolution(board)
    
 