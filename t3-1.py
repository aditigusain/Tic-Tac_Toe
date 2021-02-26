import numpy as np
board=[
    [' ','|',' ','|',' '],
    [' ','|',' ','|',' '],
    ['_','|','_','|','_'],
    [' ','|',' ','|',' '],
    [' ','|',' ','|',' '],
    ['_','|','_','|','_'],
    [' ','|',' ','|',' '],
    [' ','|',' ','|',' '],
    [' ','|',' ','|',' ']]

dict={
    1:{'i':1,'j':0},
    2:{'i':1,'j':2},
    3:{'i':1,'j':4},
    4:{'i':4,'j':0},
    5:{'i':4,'j':2},
    6:{'i':4,'j':4},
    7:{'i':7,'j':0},
    8:{'i':7,'j':2},
    9:{'i':7,'j':4}
    }

def clrBoard():
    board[1][0]=board[1][2]=board[1][4]=board[4][0]=board[4][2]=board[4][4]=board[7][0]=board[7][2]=board[7][4]=" "

def printBoard():
    for i in range(8):
        for j in range(5):
            print(board[i][j],end="")
        print()
    print("\n")

def checkWin(i,j):  #i,j are pos of X placed by user
    d1=[[1,0],[4,2],[7,4]]
    d2=[[1,4],[4,2],[7,0]]
    li=[i,j]
    if board[i][0]== board[i][2]== board[i][4]:
        return 1
    elif board[1][j]==board[4][j]==board[7][j]:
        return 1
    elif li in d1 and board[1][0]==board[4][2]==board[7][4]:
        return 1
    elif li in d2 and board[1][4]==board[4][2]==board[7][0]:
        return 1
    elif li==[4,2]  and board[1][0]==board[4][2]==board[7][4] and board[1][4]==board[4][2]==board[7][0]:
        return 1
    
def boardEmpty():
    flag=0
    for i in range(1,9,3):
        for j in range(0,5,2):
            if board[i][j]==" ":
                flag=1
    if flag==1:
        return 1
    

def comp():
    for i in range(1,9,3):
        for j in range(0,5,2):
            if board[i][j]==" ":
                board[i][j]='O'
                if checkWin(i,j):
                    return i,j
                else:
                    board[i][j]=" "
                    
    for i in range(1,9,3):
        for j in range(0,5,2):
            if board[i][j]==" ":
                board[i][j]="X"
                if checkWin(i,j):
                    board[i][j]="O"
                    return i,j
                else:
                    board[i][j]=" "

    for i in range(1,9,6):
        for j in range(0,5,4):
            if board[i][j]==" ":
                board[i][j]="O"
                return i,j
    
    for i in range(1,9,3):
        for j in range(0,5,2):
            if board[i][j]==" ":
                board[i][j]="O"
                return i,j

def play(m):
    win=False
    if m=='X':
        while win is False:
            if not boardEmpty():
                print("It's a tie!!")
                break
            user=int(input())
            r=dict[user]['i']
            c=dict[user]['j']
            board[r][c]='X'
            if checkWin(r,c):
                win=True
                printBoard()
                print("user wins")
                break
            else:
                printBoard()
            if not boardEmpty():
                print("It's a tie!!")
                break
            i,j=comp()
            if checkWin(i,j):
                    win=True
                    printBoard()
                    print("Computer Wins")
                    break
            else:
                printBoard()
        
    if m=='O':
        while win is False:
            if not boardEmpty():
                print("It's a tie!!")
                break
            i,j=comp()
            if checkWin(i,j):
                win=True
                printBoard()
                print("Computer Wins")
                break
            else:
                printBoard()
            if not boardEmpty():
                print("It's a tie!!")
                break
            user=int(input())
            r=dict[user][i]
            c=dict[user][j]
            board[r][c]='X'
            if checkWin(r,c):
                win=True
                printBoard()
                print("user wins")
                break
            else:
                printBoard()
        
            


def main():
    print("WELCOME TO TIC-TAC-TOE")
    chance=0
    user="X"
    comp="O"
    while input("Play a new game? (Y/N) ").upper() =="Y":
        clrBoard()
        if chance%2==0:
            printBoard()
            play(user)
        else:
            play(comp)

if __name__=="__main__":
    main()

