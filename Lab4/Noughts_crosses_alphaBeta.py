from math import inf
import sys,os

PERSON=1 
AGENT=-1

board=[[0,0,0],[0,0,0],[0,0,0]]

def evaluate(current_board) :
    if win(current_board,PERSON) :
        score=1
    elif win(current_board,AGENT) :
        score=-1
    else :
        score=0
    
    return score

def empty_board(current_board) :
    """ Function for extracting the empty cells in board"""
    empty_position =[] # array for storing empty positions
    for i,row in enumerate(current_board):
        for j,col in enumerate(row) :
            if current_board[i][j]==0:
                empty_position.append([i,j])

    return empty_position

def win(current_board,player):
    """ This function is used to determine who wins the game
        player win if X or 0 belongs in horizontal,vertical or diagonal  in consecutive 3 times
    """
    win_current_board = [
        #row Postions
        [current_board[0][0], current_board[0][1], current_board[0][2]],
        [current_board[1][0], current_board[1][1], current_board[1][2]],
        [current_board[2][0], current_board[2][1], current_board[2][2]],
        #Column Positions
        [current_board[0][0], current_board[1][0], current_board[2][0]],
        [current_board[0][1], current_board[1][1], current_board[2][1]],
        [current_board[0][2], current_board[1][2], current_board[2][2]],
        #disgonal positions
        [current_board[0][0], current_board[1][1], current_board[2][2]],
        [current_board[2][0], current_board[1][1], current_board[0][2]],
    ]

    if [player,player,player] in win_current_board :
        return True
    else :
        return False

def game_over(current_board) :
    """ Function to know whether the game is over or not """
    return win(current_board,PERSON) or win(current_board,AGENT) 

def alpha_beta(current_board,depth,player,alpha,beta) :
    """ Implemenation of minimax using aplha-beta pruning,it return the [best_row,best_column,best_score,eval_nodes] 
    """
    eval_nodes=0
    if player==PERSON :
        best=[-1,-1,-inf,0] #[best_row,best_column,best_score,eval_nodes] intial values for person
    if player==AGENT :
        best=[-1,-1,inf,0]#[best_row,best_column,best_score,eval_nodes] intial values for person
    
    if depth ==0 or game_over(current_board):
        score=evaluate(current_board)
        
        return [-1,-1,score,0] 

    for cell in empty_board(current_board) : #determining the empty positions in board
        x,y=cell[0],cell[1]
        current_board[x][y]=player # commiting the move
        score=alpha_beta(current_board,depth-1,-player,alpha,beta) # finding score of the move
        eval_nodes=score[3]+1+eval_nodes
        current_board[x][y]=0 #undo the current move
        score[0],score[1]=x,y # change the best_row,best_colum value 

        if player==AGENT : #Minimizing 
            if score[2]<best[2] : # comparing the best_score
                best=score
            if best[2]<beta : # comparing the beta _value 
                beta=best[2]
            if alpha>=beta : # Condition for pruning the node
                break
        if player==PERSON : #Maximizing 
            if score[2]>best[2] :# comparing the best_score
                best=score
            if best[2]>alpha :# comparing the alpha _value 
                alpha=best[2]
            if alpha>=beta : # Condition for pruning the node
                break

    best[3]=eval_nodes
    return best 

def person_turn(current_board):
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    empty=empty_board(current_board) #finding the empty positions in the board
    isTurn=True
    print("Person's Turn")
    while isTurn:
        try:
            move=int(input("Enter the value (1-9) : "))
            if moves.get(move) in empty :
                x,y=moves.get(move)
                current_board[x][y]=PERSON
                isTurn=False
            else :
                print("Wrong Move")
        except ValueError:
            print("Enter the digit between 1 and 9")
    else:
        print_board(current_board)

def agent_turn(current_board):
    depth=len(empty_board(current_board))
    row,col,score,eval_nodes=alpha_beta(current_board,depth,AGENT,alpha=-inf,beta=inf)
    current_board[row][col]=AGENT
    print("Agent's Turn")
    print(f"No of evaluated Nodes :{eval_nodes}")
    print_board(current_board)
    

def print_board(current_board):
    symbol={0:" ",1:"X",-1:"0"}
    current_board=list(map(lambda x:[symbol[y] for y in x],current_board))
    result="{}\n{}\n{}\n".format(*current_board) # converting into the string
    print(result)

def main():
    print("Lets Start the game : \n")
    print_board(board)
    while not win(board,AGENT) and not win(board,PERSON) :
        person_turn(board)
        if (len(empty_board(board))==0): break
        agent_turn(board)

    if win(board, AGENT):
        print("AGENT wins")
    elif win(board, PERSON):
        print("Person win")
    else:
        print("It's a Draw. No one wins")
        
if __name__ == '__main__':
    main()



    
    




  

    


    

   



