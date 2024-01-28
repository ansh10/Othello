'''
17th April 2023
This code is for a game called Othella and it has 11, the first 8 functions are the rule
functions to check which cell should be flipped and which should not, while the next 3 are
a functions for flipping X, flipping O and checking which rule should run respectively.
The first function checks which cell should flip in the same row and decreasing cols
The second function checks which cell should flip in the same row and increasing cols
The third function checks which cell should flip in the decreasing row and same cols
The fourth function checks which cell should flip in the increasing row and same cols
The fifth function checks which cell should flip in the decreasing row and decreasing cols
The sixth function checks which cell should flip in the increasing row and increasing cols
The seventh function checks which cell should flip in the decreasing row and increasing cols
The eighth function checks which cell should flip in the increasing row and decreasing cols
The ninth function is a cell flipping function for X
The tenth function is a cell flipping function for O
The eleventh function is a checking function for which cell should be flipped
'''
from tkinter import Tk, Label, Button, Canvas, RAISED, TOP, BOTTOM, LEFT, RIGHT
import math 
root = Tk()

turn = 0

def check_same_row_decreasing_cols(chosen_row,chosen_col):
    '''
    This function checks the same row and decreasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and checks the
    cells from the chosen_row,chosen-1 to chosen_row,0 and if it comes across an empty cell
    then the loop breaks, else if it comes across the players whose turn it is currently,
    it will calculate the difference between that cell and the initial cell (chosen_col).
    Once the difference is found, it will iterate through the difference and find the
    cells which lie in between the 2 cells and flip them all according to whoseever turn
    it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('3. checking same row, decreasing cols')
    for col in range(chosen_col - 1, -1, -1):
        if button_list[chosen_row][col]['text'] == '':
            break
        if button_list[chosen_row][col]['text'] == c_p:
            diff = chosen_col - col 
            break
    if diff > 0:
        for col in range(chosen_col - diff, chosen_col):
            if c_p == 'X':
                update_button_X(chosen_row,col)
                print('board{}{} flipped'.format([chosen_row],[col]))
            else:
                update_button_O(chosen_row,col)
                print('board{}{} flipped'.format([chosen_row],[col]))
    

def check_same_row_increasing_cols(chosen_row,chosen_col):
    '''
    This function checks the same row and increasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and checks the
    cells from the chosen_row,chosen-1 to chosen_row,9 and if it comes across an empty cell
    then the loop breaks, else if it comes across the players whose turn it is currently,
    it will calculate the difference between that cell and the initial cell (chosen_col).
    Once the difference is found, it will iterate through the difference and find the
    cells which lie in between the 2 cells and flip them all according to whoseever turn
    it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('4. checking same row, increasing cols')
    for col in range(chosen_col + 1,10):
        if button_list[chosen_row][col]['text'] == '':
            break
        if button_list[chosen_row][col]['text'] == c_p:
            diff = col - chosen_col 
            break
    if diff > 0:
        for col in range(chosen_col, chosen_col + diff):
            if c_p == 'X':
                update_button_X(chosen_row,col)
                print('board{}{} flipped'.format([chosen_row],[col]))
            else:
                update_button_O(chosen_row,col)
                print('board{}{} flipped'.format([chosen_row],[col]))

def check_same_col_decreasing_rows(chosen_row,chosen_col):
    '''
    This function checks the same col and decreasing rows. It does so by first determining
    which players turn it is and then it iterates through the the chosen_col and checks the
    cells from the chosen_row-1,chosen_col to 0,chosen_col and if it comes across an empty cell
    then the loop breaks, else if it comes across the players whose turn it is currently,
    it will calculate the difference between that cell and the initial cell (chosen_row).
    Once the difference is found, it will iterate through the difference and find the
    cells which lie in between the 2 cells and flip them all according to whoseever turn
    it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('==================================')
    print('1. checking same column, decreasing rows')
    for row in range(chosen_row - 1, -1, -1):
        if button_list[row][chosen_col]['text'] == '':
            break
        if button_list[row][chosen_col]['text'] == c_p:
            diff = chosen_row - row 
            break
    if diff > 0:
        for row in range(chosen_row - diff, chosen_row):
            if c_p == 'X':
                update_button_X(row,chosen_col)
                print('board{}{} flipped'.format([row],[chosen_col]))
            else:
                update_button_O(row,chosen_col)
                print('board{}{} flipped'.format([row],[chosen_col]))

def check_same_col_increasing_rows(chosen_row,chosen_col):
    '''
    This function checks the same col and increasing rows. It does so by first determining
    which players turn it is and then it iterates through the the chosen_col and checks the
    cells from the chosen_row-1,chosen_col to 9,chosen_col and if it comes across an empty cell
    then the loop breaks, else if it comes across the players whose turn it is currently,
    it will calculate the difference between that cell and the initial cell (chosen_row).
    Once the difference is found, it will iterate through the difference and find the
    cells which lie in between the 2 cells and flip them all according to whoseever turn
    it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('2. checking same column, increasing rows')
    for row in range(chosen_row + 1, 10):
        if button_list[row][chosen_col]['text'] == '':
            break
        if button_list[row][chosen_col]['text'] == c_p:
            diff = row - chosen_row 
            break
    if diff > 0:
        for row in range(chosen_row, chosen_row + diff):
            if c_p == 'X':
                update_button_X(row,chosen_col)
                print('board{}{} flipped'.format([row],[chosen_col]))
            else:
                update_button_O(row,chosen_col)
                print('board{}{} flipped'.format([row],[chosen_col]))

def check_diagonal_decreasing_rows_decreasing_cols(chosen_row,chosen_col):
    '''
    This function checks the decreasing row and decreasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and chosen_col
    and checks the cells from the chosen_row,chosen_col to 0,0 and if it comes
    across an empty cell then the loop breaks, else if it comes across the players whose
    turn it is currently, it will calculate the difference between that cell and the
    initial cell (chosen_row,chosen_col). Once the difference is found, it will iterate through the
    difference and find the cells which lie in between the 2 cells and flip them all
    according to whoseever turn it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('5. checking diagonal decreasing row,decreasing cols')
    diff_checker_row = chosen_row
    diff_checker_col = chosen_col
    while chosen_col > 0 and chosen_row > 0:
        chosen_col -= 1
        chosen_row -= 1
        if button_list[chosen_row][chosen_col]['text'] == '':
            break
        if button_list[chosen_row][chosen_col]['text'] == c_p:
            diff = diff_checker_col - chosen_col
            break
    if diff > 0:
        for i in range(diff):
            rowj = diff_checker_row - i 
            colj = diff_checker_col - i 
            if c_p == 'X':
                update_button_X(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))
            else:
                update_button_O(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))
                
def check_diagonal_increasing_rows_increasing_cols(chosen_row,chosen_col):
    '''
    This function checks the increasing row and increasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and chosen_col
    and checks the cells from the chosen_row,chosen_col to 9,9 and if it comes
    across an empty cell then the loop breaks, else if it comes across the players whose
    turn it is currently, it will calculate the difference between that cell and the
    initial cell (chosen_row,chosen_col). Once the difference is found, it will iterate through the
    difference and find the cells which lie in between the 2 cells and flip them all
    according to whoseever turn it is.
    it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('6. checking diagonal increasing row,increasing cols')
    diff_checker_row = chosen_row
    diff_checker_col = chosen_col
    while chosen_col < 9 and chosen_row < 9:
        chosen_col += 1
        chosen_row += 1
        if button_list[chosen_row][chosen_col]['text'] == '':
            break
        if button_list[chosen_row][chosen_col]['text'] == c_p:
            diff = chosen_col - diff_checker_col 
            break
    if diff > 0:
        for i in range(diff):
            rowj = diff_checker_row + i 
            colj = diff_checker_col + i 
            if c_p == 'X':
                update_button_X(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))
            else:
                update_button_O(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))

def check_diagonal_increasing_rows_decreasing_cols(chosen_row,chosen_col):
    '''
    This function checks the increasing row and decreasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and chosen_col
    and checks the cells from the chosen_row,chosen_col to 9,0 and if it comes
    across an empty cell then the loop breaks, else if it comes across the players whose
    turn it is currently, it will calculate the difference between that cell and the
    initial cell (chosen_row,chosen_col). Once the difference is found, it will iterate through the
    difference and find the cells which lie in between the 2 cells and flip them all
    according to whoseever turn it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('7. checking diagonal increasing row,decreasing cols')
    diff_checker_row = chosen_row
    diff_checker_col = chosen_col
    while chosen_col > 0 and chosen_row < 9:
        chosen_col -= 1
        chosen_row += 1
        if button_list[chosen_row][chosen_col]['text'] == '':
            break
        if button_list[chosen_row][chosen_col]['text'] == c_p:
            diff = diff_checker_col - chosen_col
            break
    if diff > 0:
        for i in range(diff):
            rowj = diff_checker_row + i 
            colj = diff_checker_col - i 
            if c_p == 'X':
                update_button_X(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))
            else:
                update_button_O(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))

def check_diagonal_decreasing_rows_increasing_cols(chosen_row,chosen_col):
    '''
    This function checks the decreasing row and increasing cols. It does so by first determining
    which players turn it is and then it iterates through the the chosen_row and chosen_col
    and checks the cells from the chosen_row,chosen_col to 0,9 and if it comes
    across an empty cell then the loop breaks, else if it comes across the players whose
    turn it is currently, it will calculate the difference between that cell and the
    initial cell (chosen_row,chosen_col). Once the difference is found, it will iterate through the
    difference and find the cells which lie in between the 2 cells and flip them all
    according to whoseever turn it is.
    '''
    global turn
    if turn%2!=0:
        c_p = 'X'
    else:
        c_p = 'O'
    diff = 0
    print('8. checking diagonal decreasing row,increasing cols')
    diff_checker_row = chosen_row
    diff_checker_col = chosen_col
    while chosen_col < 9 and chosen_row > 0:
        chosen_col += 1
        chosen_row -= 1
        if button_list[chosen_row][chosen_col]['text'] == '':
            break
        if button_list[chosen_row][chosen_col]['text'] == c_p:
            diff = chosen_col - diff_checker_col 
            break
    if diff > 0:
        for i in range(diff):
            rowj = diff_checker_row - i 
            colj = diff_checker_col + i 
            if c_p == 'X':
                update_button_X(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))
            else:
                update_button_O(rowj, colj)
                print('board{}{} flipped'.format([rowj],[colj]))

        
def update_button_X(row,col):
    '''
    This function is for updating the clicked button or desired fliped cell to X
    '''
    Label_X = Label(master = canvas2,text = 'X', foreground = 'red', background = 'blue', height = 4, width = 10)
    button_list[row][col] = Label_X
    Label_X.grid(row = row+1, column = col+1)

def update_button_O(row,col):
    '''
    This function is for updating the clicked button or desired fliped cell to O
    '''
    Label_O = Label(canvas2,text = 'O', foreground = 'black', background = 'yellow', height = 4, width = 10)
    button_list[row][col] = Label_O
    Label_O.grid(row = row+1, column = col+1)

def checking_flip(chosen_row,chosen_col):
    '''
    This function checks whose turn it is and then changes the label on top of the board
    to Player 'X's or 'O's turn depending on whose turn it is. It then runs all the rule
    functions to check whether the cell can be flipped or not and flips it accordingly. 
    '''
    global diff
    global turn
    global Label_Turn
    Label_Turn.destroy()
    if turn % 2 != 0:
        Label_Turn = Label(master=canvas1, text="The Player 'X's turn")
        Label_Turn.pack()
        turn += 1
        update_button_O(chosen_row,chosen_col)
    elif turn % 2 == 0:
        Label_Turn = Label(master=canvas1, text="The Player 'O's turn")
        Label_Turn.pack()
        turn += 1
        update_button_X(chosen_row,chosen_col)
    check_same_col_decreasing_rows(chosen_row,chosen_col)
    check_same_col_increasing_rows(chosen_row,chosen_col)
    check_same_row_decreasing_cols(chosen_row,chosen_col)
    check_same_row_increasing_cols(chosen_row,chosen_col)
    check_diagonal_decreasing_rows_decreasing_cols(chosen_row,chosen_col)
    check_diagonal_increasing_rows_increasing_cols(chosen_row,chosen_col)                                           
    check_diagonal_increasing_rows_decreasing_cols(chosen_row,chosen_col)
    check_diagonal_decreasing_rows_increasing_cols(chosen_row,chosen_col)

#Creates a canvas1
canvas1 = Canvas(master=root, height=100, width=150)
canvas1.pack(side=TOP)

#Creates a canavs2
canvas2 = Canvas(master=root, height=100, width=150)
canvas2.pack(side=BOTTOM)

#Creates a Label called message
Label_Turn = Label(master=canvas1, text="The Player 'O's Turn!")
Label_Turn.pack()  
    
#Creates an empty list
button_list = []

#This part of the code is for putting the numebr markers for the row and column
num = ['0','1','2','3','4','5','6','7','8','9']
for mark in num:
    c_num = Label(master=canvas2, text=mark)
    c_num.grid(row=0, column=int(mark)+1)

    r_num = Label(master=canvas2, text=mark)
    r_num.grid(row=int(mark)+1, column=0)

#This part of the code is for making a 10X10 grid wtih all the buttons which should be flipped
for i in range(10):
    button_row = []
    for j in range(10):
            button = Button(master = canvas2,
                        height = 4,
                        width = 10,
                        relief = RAISED,
                        background = 'white',
                        command = lambda row = i, col = j: checking_flip(row,col))
            button.grid(row=i+1, column=j+1)
            button_row.append(button)
    button_list.append(button_row)
root.mainloop()
