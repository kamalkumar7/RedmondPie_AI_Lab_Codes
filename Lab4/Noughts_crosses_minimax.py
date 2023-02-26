from math import inf
import sys,os

PERSON=1 
AGENT=-1

board=[[0,0,0],[0,0,0],[0,0,0]]

def evaluate(currentBoard) :
    if win(currentBoard,PERSON) :
        score=1
    elif win(currentBoard,AGENT) :
        score=-1
    else :
        score=0
    
    return score

def empty_board(currentBoard) :
    """ Function for extracting the empty cells in board"""
    empty_position =[] # array for storing empty positions
    for i,row in enumerate(currentBoard):
        for j,col in enumerate(row) :
            if currentBoard[i][j]==0:
                empty_position.append([i,j])

    return empty_position

def win(currentBoard,player):
    """ This function is used to determine who wins the game
        player win if X or 0 belongs in horizontal,vertical or diagonal  in consecutive 3 times
    """
    win_current_board = [
        #row Postions
        [currentBoard[0][0], currentBoard[0][1], currentBoard[0][2]],
        [currentBoard[1][0], currentBoard[1][1], currentBoard[1][2]],
        [currentBoard[2][0], currentBoard[2][1], currentBoard[2][2]],
        #Column Positions
        [currentBoard[0][0], currentBoard[1][0], currentBoard[2][0]],
        [currentBoard[0][1], currentBoard[1][1], currentBoard[2][1]],
        [currentBoard[0][2], currentBoard[1][2], currentBoard[2][2]],
        #disgonal positions
        [currentBoard[0][0], currentBoard[1][1], currentBoard[2][2]],
        [currentBoard[2][0], currentBoard[1][1], currentBoard[0][2]],
    ]

    if [player,player,player] in win_current_board :
        return True
    else :
        return False

def game_over(currentBoard) :
    """ Function to know whether the game is over or not """
    return win(currentBoard,PERSON) or win(currentBoard,AGENT) 

def minimax(currentBoard,depth,player):
    """ Minimax implementation for agents move, its a recursive function.
        It tries to find the best possible move to hinder other player winning move
    """
    eval_nodes=0
    if player==PERSON :
        best=[-1,-1,-inf,0]  #[best_row,best_column,best_score,eval_nodes] intial values for person
    else :
        best=[-1,-1,inf,0] #[best_row,best_column,best_score,eval_nodes] intial values for person

    if depth ==0 or game_over(currentBoard):
        score=evaluate(currentBoard)
        
        return [-1,-1,score,0] 

    for cell in empty_board (currentBoard) : #determining the empty positions in board
        x,y=cell[0],cell[1] 
        currentBoard[x][y]=player # commiting the move
        score =minimax(currentBoard,depth-1,-player) # finding score of the move
        eval_nodes=score[3]+1+eval_nodes
        currentBoard[x][y]=0 #undo the current move
        score[0],score[1]=x,y # change the best_row,best_colum value 

        if player == AGENT : #Minimizing 
           if score[2]< best[2] :# comparing the best_score
              best=score
        else:   #Maximizing 
            if score[2]>best[2] :
                best = score
    best[3]=eval_nodes

    return best

def person_turn(currentBoard):
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    empty=empty_board(currentBoard) #finding the empty positions in the board
    isTurn=True
    print("Person's Turn")
    while isTurn:
        try:
            move=int(input("Enter the value (1-9) : "))
            if moves.get(move) in empty :
                x,y=moves.get(move)
                currentBoard[x][y]=PERSON
                isTurn=False
            else :
                print("Wrong Move")
        except ValueError:
            print("Enter the digit between 1 and 9")
    else:
        print_board(currentBoard)

def agent_turn(currentBoard):
    depth=len(empty_board(currentBoard))
    row,col,score,eval_nodes=minimax(currentBoard,depth,AGENT)
    currentBoard[row][col]=AGENT
    print("Agent's Turn")
    print(f"No of evaluated Nodes :{eval_nodes}")
    print_board(currentBoard)
    

def print_board(currentBoard):
    symbol={0:" ",1:"X",-1:"0"}
    currentBoard=list(map(lambda x:[symbol[y] for y in x],currentBoard))
    result="{}\n{}\n{}\n".format(*currentBoard) # converting into the string
    print(result)

def main():
    print("Lets Start the game : \n")
    print_board(board)
    while not win(board,AGENT) and not win(board,PERSON) :
        person_turn(board)
        if (len(empty_board(board))==0): break
        agent_turn(board)

    if win(board, AGENT):
        print("Agent wins")
    elif win(board, PERSON):
        print("Person win")
    else:
        print("It's a Draw.")


if __name__ == '__main__':
    main()



    
    




  

    


    

   



