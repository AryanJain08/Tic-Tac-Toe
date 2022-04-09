import pygame
import sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=600
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLS=3
CIRCLE_RADIUS=60
CIRCLE_WIDTH=15
CIRCLE_COLOR=(218,165,32)
CROSS_WIDTH=25
SPACE=55

RED=(255,0,0)
bg_color=(128,0,0)
line_color=(255,255,255)
cross_color=(0,0,0)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(bg_color)

board=np.zeros((BOARD_ROWS,BOARD_COLS))

def draw_figures():
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(c*200+100),int(r*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[r][c]==2:
                pygame.draw.line(screen, cross_color,(c*200+SPACE,r*200+200-SPACE),(c*200+200-SPACE,r*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen, cross_color,(c*200+SPACE,r*200+SPACE),(c*200+200-SPACE,r*200+200-SPACE),CROSS_WIDTH)

def mark_square(row,col,player):
    board[row][col]=player

def available_square(row,col):
    return board[row][col]==0

def isboard_full():
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c]==0:
                return False
    
    return True

def draw_lines():
    # horizontal
    pygame.draw.line(screen,line_color,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,line_color,(0,400),(600,400),LINE_WIDTH)

    #vertical
    pygame.draw.line(screen,line_color,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,line_color,(400,0),(400,600),LINE_WIDTH)


def check_win(player):
    #vertical win
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col,player)
            return True
    
    #horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonal win
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    
    #desc diagonal win
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col,player):
    posX=col*200+100

    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=cross_color
    
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_winning_line(row,player):
    posY=row*200+100

    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=cross_color
    
    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

def draw_asc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=cross_color
    
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=cross_color
    
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart():
    screen.fill(bg_color)
    draw_lines()
    player=1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0
    
draw_lines()

player=1
game_over=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
           
            X=event.pos[0]   #x coordinate
            Y=event.pos[1]   #y coordinate

            clicked_row=int(Y//200)
            clicked_col=int(X//200)

        
            if available_square(clicked_row,clicked_col):
                if player==1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over=True
                    player=2

                elif player==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over=True
                    player=1

            draw_figures()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                game_over=False
                
    pygame.display.update()
