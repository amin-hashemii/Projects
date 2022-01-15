import pygame as py
from pygame.locals import *
from pygame import draw
import numpy as np
from time import sleep

py.font.init()
WIDTH = 600
WIN = py.display.set_mode((WIDTH, WIDTH + 100))

RED = (255, 0, 0)
BACK_COLOR = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
LINE_THIKNESS = 3
board = np.zeros((3, 3))
FONT = py.font.SysFont('Lucida Calligraphy Italic', 200)
player_font = py.font.SysFont('Arial', 100)
line_code = 0
is_win = False

py.display.set_caption('TIC TOC TOE')


def draw_lines(win):
    draw.line(win, GREY, (0, WIDTH/3), (WIDTH, WIDTH/3), LINE_THIKNESS)
    draw.line(win, GREY, (0, (WIDTH/3)*2), (WIDTH, (WIDTH/3)*2), LINE_THIKNESS)
    draw.line(win, GREY, (WIDTH/3, 0), (WIDTH/3, WIDTH), LINE_THIKNESS)
    draw.line(win, GREY, ((WIDTH/3)*2, 0), ((WIDTH/3)*2, WIDTH), LINE_THIKNESS)

def draw_player_move(win, width):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                text = FONT.render('X', 1, BLACK)
                win.blit(text, [int(col * (width/3) + 50), (int(row * (width/3)) + 50)])
            elif board[row][col] == 2:
                text = FONT.render('O', 1, BLACK)
                win.blit(text, [int(col * (width/3) + 50), int(row * (width/3) + 50)])

def get_player(player):
    if player == 1:
        return 'X'
    elif player == 2:
        return 'O'

def redraw_window(win, width, player, winner, text = ''):
    win.fill(BACK_COLOR)
    draw_lines(win)
    draw_player_move(win, width)
    
    if winner != '/':
        newtext = player_font.render(f'{get_player(player)} Won!', 1, BLACK)
        win.blit(newtext, [width/2 - 130, width])
    else:
        if text == '':
            text = player_font.render(f"{get_player(player)}'s turn", 1, BLACK)
            win.blit(text, [width/2 - 130, width])
        else:
            newtext = player_font.render(text, 1, BLACK)
            win.blit(newtext, [width/2 - 130, width])
    if line_code != 0:
        if line_code == 11:
            draw.line(win, RED, (50, 100), (width-50, 100), 5)
        if line_code == 12:
            draw.line(win, RED, (50, 300), (width-50, 300), 5)
        if line_code == 13:
            draw.line(win, RED, (50, 500), (width-50, 500), 5)
        if line_code == 14:
            draw.line(win, RED, (100, 50), (100, width-50), 5)
        if line_code == 15:
            draw.line(win, RED, (width/2, 50), (width/2, width-50), 5)
        if line_code == 16:
            draw.line(win, RED, (width-100, 50), (width-100, width-50), 5)
        if line_code == 17:
            draw.line(win, RED, (50, 50), (width-50, width-50), 5)
        if line_code == 18:
            draw.line(win, RED, (width-50, 50), (50, width-50), 5)
    py.display.update()

def check_winner(board):
    global line_code
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        line_code = 11
        return 'X'
    if board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        line_code = 12
        return 'X'
    if board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        line_code = 13
        return 'X'
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        line_code = 14
        return 'X'
    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        line_code = 15
        return 'X'
    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        line_code = 16
        return 'X'
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        line_code = 17
        return 'X'
    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        line_code = 18
        return 'X'


    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        line_code = 11
        return 'O'
    if board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        line_code = 12
        return 'O'
    if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        line_code = 13
        return 'O'
    if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        line_code = 14
        return 'O'
    if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        line_code = 15
        return 'O'
    if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        line_code = 16
        return 'O'
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        line_code = 17
        return 'O'
    if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        line_code = 18
        return 'O'

    return '/'

def mark_square(row, col, player):
    board[row][col] = player

def is_available(row, col):
    try:
        return board[row][col] == 0
    except IndexError:
        pass

def is_board_full():
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                return False
    return True

def get_pos(pos, row, width):
    gap = width // row
    y, x = pos

    row, col = y // gap, x // gap

    return row, col

def change_player(player):
    if player == 1:
        return 2
    return 1

def restart(win, width):
    global board
    global line_code
    global is_win
    is_win = False
    board = np.zeros((3, 3))
    line_code = 0
    main(win, width)

def main(win, width):
    global is_win
    run = True
    player = 1
    text = ''
    winer = '/'
    is_full = False
    while run:
        is_full = is_board_full()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                quit()
            
            if event.type == KEYDOWN:
                if event.key == K_q:
                    py.quit()
                    quit()
                if event.key == K_SPACE:
                    run = False
            if not is_win:
                if event.type == MOUSEBUTTONDOWN:
                    y, x = event.pos[0], event.pos[1]
                    row, col = int(x // (width/3)), int(y // (width/3))
                    
                    if is_available(row, col):
                        mark_square(row, col, player)
                        winer = check_winner(board)
                        if winer != '/':
                            print(f'{get_player(player)} won')
                            is_win = True
                        else:
                            player = change_player(player)

        redraw_window(win, width, player, winer, text)

    restart(win, width)


main(WIN, WIDTH)