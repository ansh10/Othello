from tkinter import Tk, Label, Button, Canvas, RAISED, TOP, BOTTOM, LEFT, RIGHT
import math 

# Initialize the main Tkinter window
root = Tk()

# Global variable to keep track of the current turn (X: 1, O: 0)
turn = 0

def check_same_row_decreasing_cols(chosen_row, chosen_col):
    '''
    Check cells in the same row and decreasing columns for possible flips.
    '''
    global turn
    # Determine the current player
    current_player = 'X' if turn % 2 != 0 else 'O'
    diff = 0
    
    print('3. Checking same row, decreasing cols')
    
    # Iterate through the chosen row, moving left
    for col in range(chosen_col - 1, -1, -1):
        # Break if an empty cell is encountered
        if button_list[chosen_row][col]['text'] == '':
            break
        # If the current player's symbol is found, calculate the difference
        if button_list[chosen_row][col]['text'] == current_player:
            diff = chosen_col - col 
            break
    
    # Flip cells based on the calculated difference
    if diff > 0:
        for col in range(chosen_col - diff, chosen_col):
            if current_player == 'X':
                update_button_X(chosen_row, col)
                print('board{}{} flipped'.format([chosen_row], [col]))
            else:
                update_button_O(chosen_row, col)
                print('board{}{} flipped'.format([chosen_row], [col]))

# Define similar functions for other directions and flipping operations...

def update_button_X(row, col):
    '''
    Update the clicked button or desired flipped cell to 'X'.
    '''
    Label_X = Label(master=canvas2, text='X', foreground='red', background='blue', height=4, width=10)
    button_list[row][col] = Label_X
    Label_X.grid(row=row + 1, column=col + 1)

def update_button_O(row, col):
    '''
    Update the clicked button or desired flipped cell to 'O'.
    '''
    Label_O = Label(canvas2, text='O', foreground='black', background='yellow', height=4, width=10)
    button_list[row][col] = Label_O
    Label_O.grid(row=row + 1, column=col + 1)

def checking_flip(chosen_row, chosen_col):
    '''
    Check whose turn it is, update the turn label, and flip cells based on game rules.
    '''
    global turn
    global Label_Turn
    Label_Turn.destroy()
    
    # Determine the current player
    current_player = 'X' if turn % 2 != 0 else 'O'
    
    # Update the turn label
    Label_Turn = Label(master=canvas1, text=f"The Player '{current_player}'s turn")
    Label_Turn.pack()
    
    # Increment the turn counter
    turn += 1
    
    # Update the chosen cell to the current player's symbol
    if current_player == 'X':
        update_button_O(chosen_row, chosen_col)
    else:
        update_button_X(chosen_row, chosen_col)
    
    # Call rule-checking functions for different directions
    check_same_col_decreasing_rows(chosen_row, chosen_col)
    check_same_col_increasing_rows(chosen_row, chosen_col)
    check_same_row_decreasing_cols(chosen_row, chosen_col)
    check_same_row_increasing_cols(chosen_row, chosen_col)
    check_diagonal_decreasing_rows_decreasing_cols(chosen_row, chosen_col)
    check_diagonal_increasing_rows_increasing_cols(chosen_row, chosen_col)
    check_diagonal_increasing_rows_decreasing_cols(chosen_row, chosen_col)
    check_diagonal_decreasing_rows_increasing_cols(chosen_row, chosen_col)

# GUI Setup
canvas1 = Canvas(master=root, height=100, width=150)
canvas1.pack(side=TOP)

canvas2 = Canvas(master=root, height=100, width=150)
canvas2.pack(side=BOTTOM)

Label_Turn = Label(master=canvas1, text="The Player 'O's Turn!")
Label_Turn.pack()  

button_list = []

# Display numeric markers for rows and columns
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for mark in num:
    c_num = Label(master=canvas2, text=mark)
    c_num.grid(row=0, column=int(mark) + 1)

    r_num = Label(master=canvas2, text=mark)
    r_num.grid(row=int(mark) + 1, column=0)

# Create a 10x10 grid of buttons
for i in range(10):
    button_row = []
    for j in range(10):
        button = Button(master=canvas2,
                        height=4,
                        width=10,
                        relief=RAISED,
                        background='white',
                        command=lambda row=i, col=j: checking_flip(row, col))
        button.grid(row=i + 1, column=j + 1)
        button_row.append(button)
    button_list.append(button_row)

# Run the Tkinter main loop
root.mainloop()
