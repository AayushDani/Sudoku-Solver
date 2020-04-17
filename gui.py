#SUODKU SOLVER USING A BACKTRACKING ALGORITHM
from tkinter import *

'''
board = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ]
'''

board = [
            [1, 0, 0, 4, 8, 9, 0, 0, 6],
            [7, 3, 0, 0, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 0, 1, 2, 9, 5],
            [0, 0, 7, 1, 2, 0, 6, 0, 0],
            [5, 0, 0, 7, 0, 3, 0, 0, 8],
            [0, 0, 6, 0, 9, 5, 7, 0, 0],
            [9, 1, 4, 6, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 3, 7],
            [8, 0, 0, 5, 1, 2, 0, 0, 4]
        ]


see_stepwise = input("Do you want to see a step-wise solution (y/n): ").lower()

def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("---------------------",end='\n')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("|",end=' ')
                print(str(board[i][j])+" ", end='')
            elif j==8:
                print(str(board[i][j])+" ", end='\n')
            else:
                print(str(board[i][j])+" ", end='')


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j) #row, column

    return None

def is_valid(board,value,pos):
    #Check Row
    for j in range(len(board[0])):
        if value==board[pos[0]][j]:
            board[pos[0]][pos[1]]==0
            return False
            
    #Check Column
    for i in range(len(board)):
        if value==board[i][pos[1]]:
            board[pos[0]][pos[1]]=0
            return False

     # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == value and (i,j) != pos:
                return False

    return True


past = []
steps= 0

def main(board,start=1):
    global steps
    
    tup = find_empty(board)

    if not tup:
        print("\nSolved Sudoku: \n")
        gui(board)
        print()
        print("Steps Taken:",str(steps))
        return
    
    ch = False
    for i in range(start,10):
        if is_valid(board,i,tup):
            board[tup[0]][tup[1]] = i
            past.append(tup)
            ch = True
            steps+=1

            if see_stepwise=="y":
                print("\nStep {}:".format(steps))
                print_board(board)
            
            break
    
    if not ch:
        val = board[past[-1][0]][past[-1][1]]
        board[past[-1][0]][past[-1][1]] = 0
        past.pop(-1)
        main(board,val+1)
    else:
        main(board)
        
    
def gui(board):
    wnd = Tk()
    wnd.geometry("450x450+150+150")
    wnd.title("Sudoku")
    wnd.iconbitmap('sudoku.ico')

    canvas = Canvas(wnd,bg="black",width=450,height=450)

    for i in range(1,10):
        if i%3==0:
            line = canvas.create_line(50*i,0,50*i,500,width=5,fill="grey")
        else:
            line = canvas.create_line(50*i,0,50*i,500,width=5,fill="white")
    
    for i in range(1,10):
        if i%3==0:
            line = canvas.create_line(0,50*i,500,50*i,width=5,fill="grey")
        else:
            line = canvas.create_line(0,50*i,500,50*i,width=5,fill="white")
            
    for i in range(1,len(board)+1):
        for j in range(1,len(board[0])+1):
            if board[i-1][j-1]==0:
                canvas.create_text(25+50*(i-1),25+50*(j-1),text="",fill="white",font="Helvetica 20 bold")
            else:
                canvas.create_text(25+50*(i-1),25+50*(j-1),text=str(board[i-1][j-1]),fill="white",font="Helvetica 20 bold")

    canvas.pack()

    wnd.mainloop()

gui(board)

nah = main(board)

