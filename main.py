import pygame
import sys
from constants import *
import numpy as np



pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT ))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOUR)

player = 1
#for avoidning an error : UnboundLocalError: cannot access local variable
# 'clicked_row' where it is not associated with a value
clicked_row = None
clicked_col = None

board = np.zeros((BOARD_ROWS, BOARD_COLS))
# argument needs to be a tuple! ()
print(board)

def draw_lines():
    # 1 horizontale line
    pygame.draw.line(screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH)
    # 2 horizontale line
    pygame.draw.line(screen, LINE_COLOUR, (0,400), (600, 400), LINE_WIDTH)
    # 1 vertical line
    pygame.draw.line(screen, LINE_COLOUR,(200,0), (200, 600), LINE_WIDTH)
    # 2 vertical line
    pygame.draw.line(screen, LINE_COLOUR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOUR, ((int( col * 200 + 200/2 )), (int (row * 200 + 200/2 ))), CIRCLE_RAD, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOUR, ( col * 200 +CROSS_SPACE, row * 200 + 200 -CROSS_SPACE) , (col * 200 + 200 -CROSS_SPACE, row *200 +CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen , CROSS_COLOUR, ( col * 200 +CROSS_SPACE, row *200 + CROSS_SPACE), ( col * 200 + 200 -CROSS_SPACE, row * 200 + 200 -CROSS_SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):

    #if row is not None and col is not None:
        # If row and col have valid values, check if the corresponding square on the board is 0
        #return board[row][col] == 0
    # If row or col is None, it means the square is not valid or hasn't been clicked yet
    #return False
    ##these doesnt work
    return  board[row][col] == 0
    #same thing:
    #if board[row][col] == 0:
       # return True
    #else:
        #return False
    #The error occurred in your previous implementation because you were trying to access board[row][col]
    # when row and col were None, which led to a "ValueError: can only convert an array of size 1
    # to a Python scalar." This error happens because None is not a valid index for accessing elements
    # in the board array.
    #By adding the check if row is not None and col is not None, we ensure that the code inside the if block
    # is executed only when row and col have valid values (i.e., they are not None).
    # This avoids accessing the board array with invalid indices and resolves the error.

def is_board_full():
    return 0 not in board

def check_win(player):
    #horizontal win check
    for row in range(BOARD_ROWS):
        #check for rows
        if board[row][0] == board[row][1]== board [row][2] and board [row][0] == player:
            draw_horizontal_winning_line(row, player)
            return True
    #check for vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    #check for diagonals win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == player:
        draw_desc_diagonal_win_line(player)
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == player:
        draw_asc_diagonal_win_line(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 200/2
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player ==2:
        colour = CROSS_COLOUR
    pygame.draw.line( screen, colour, (posX, 15), (posX, HEIGHT-15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 200 / 2
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = CROSS_COLOUR
    pygame.draw.line(screen, colour, ( 15 , posY), ( WIDTH - 15,posY ), 15)

def draw_asc_diagonal_win_line(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = CROSS_COLOUR
    pygame.draw.line( screen, colour, ( 15, HEIGHT - 15), ( WIDTH - 15, 15), 20)

def draw_desc_diagonal_win_line(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player == 2:
        colour = CROSS_COLOUR
    pygame.draw.line(screen, colour, ( 15, 15), ( WIDTH-15, HEIGHT -15), 20)

def restart():
    global game_over
    screen.fill( BG_COLOUR )
    draw_lines()
    player = 1
    game_over = False
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0



draw_lines()
game_over = False

def main():
    #global clicked_row
    #global clicked_col
    global game_over
    global player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # FCE for checking if we click the screen
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_X = event.pos[0] #X
                mouse_Y = event.pos[1] #Y

                # (X,Y) tuple of the coordinates on the screen, fist position [0] == X
                clicked_row = int( mouse_Y // 200)
                clicked_col = int ( mouse_X // 200)
                # // operator for division that rounds down to whole number, cooridnate 100 is equal to 0
                if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        if check_win(player):
                            game_over = True
                        player = 2
                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

        pygame.display.update()

main()


