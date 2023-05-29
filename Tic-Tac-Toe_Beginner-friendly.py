
import random


#global variables
#print the board
board =\
    [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
current_player="X"
winner= None
game_running= True


#printing the game board
def print_board(board):
    for row in board:
        print("|".join(row)) #+ "\n-----")


#take player input
def player_input(board):
    global current_player
    try:
        row = int(input("Enter number 1-3 for position in row:"))-1
        col = int(input("Enter number 1-3 for position in column:"))-1
        if board[row][col] == "-":
            board[row][col] = current_player
            return board
        else:
            print("That space is already occupied.")
            switch_player()

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        switch_player()
    except IndexError:
        print("Invalid input. Please enter a number between 1 and 3.")
        switch_player()


#define game if game has been won
def check_win(board):
    global winner
    for i in range(3):
        #check for rows
        if board[i][0] == board[i][1]== board [i][2] and board [i][0] != "-":
            winner = board[i][1]
            return True
        #check for columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            winner = board [0][i]
            return True
    #check for diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        winner = board[0][2]
        return True
    return False


def check_win_global():
    if check_win(board):
        print_board(board)
        print(f"The winner is {winner}!")
        exit()


#check for tie
def check_tie(board):
    global game_running
    if any("-" in row for row in board):
        game_running = True
    else:
        print_board(board)
        print("It's a tie!")
        game_running = False
        exit()


#switch player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


#random generator as a second player "O"
def computer(board):
    while current_player == "O":
        random_row = random.randint(0,2)
        random_col = random.randint(0,2)
        if board[random_row][random_col] == "-":
            board[random_row][random_col] = "0"
            switch_player()
            break


while game_running:
    print_board(board)
    player_input(board)
    check_win_global()
    check_tie(board)
    switch_player()
    computer(board)
    check_win_global()
    check_tie(board)
