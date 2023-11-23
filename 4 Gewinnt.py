import pygame, sys
import copy
from pygame. locals import QUIT
pygame. init()

#import kivy
#kivy.require('2.1.0')

#from kivy.app import App


board = [[None]* 7 for i in range(6)]

rect_width = (350, 300)
rect_position = (25 , 0)
rect = (rect_position, rect_width)


blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
radius = (15)



x_positions = []
y_positions = []

index_list= []


def draw_board():
  pygame.draw.rect (DISPLAYSURF,blue,rect)
  y_circle = (276)

  for i in range(6):
    x_circle = (57.5)
    x_positions.append(x_circle)
    circle_position = (x_circle, y_circle)
    pygame.draw.circle(DISPLAYSURF,white,circle_position,radius)
    for i in range(6):
      x_circle += 47.5
      circle_position = (x_circle, y_circle)
      pygame.draw.circle(DISPLAYSURF,white,circle_position,radius)
      x_positions.append(x_circle)
    y_positions.append(y_circle)
    y_circle -= 47.5 
    
def four_in_row(board):
  for row in board:
    for i in range(len(row)-3):
      if row[i]==row[i+1]==row[i+2]==row[i+3] != None:
        return True

  for col in range(len(board[0])):
    for row in range(len(board)-3):
      if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != None:
        return True

  for row in range(len(board)-3):
    for col in range(len(board[0])-3):
      if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != None:
        return True

  for row in range(3, len(board)):
    for col in range (len(board[0])-3):
      if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != None:
        return True
        
  return False

def game_over():
  if four_in_row(board) is True:
    if current_player == "red":
      print("Congratulations! Yellow wins!")
      while True:
        for event in pygame.event.get():
          if event.type == QUIT:
            sys.exit()

    elif current_player == "yellow":
      print("Congratulations! Red wins!")
      while True:
        for event in pygame.event.get():
          if event.type == QUIT:
            sys.exit()



current_player = "yellow"
row = 0

DISPLAYSURF = pygame.display.set_mode((400, 300))

draw_board()
while True:

  for event in pygame.event.get( ):
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        
          
          x = event.pos[0]
          if x < 81.25:
            col = 0
          elif 81.25 < x < 128.75:
            col = 1
          elif 128.75 < x < 176.25:
            col = 2
          elif 176.25 < x < 223.75:
            col = 3
          elif 223.75 < x < 271.25:
            col = 4
          elif 271.25 < x < 318.75:
            col = 5
          elif 318.75 < x < 375:
            col = 6

          if current_player == "yellow":
            if row <=5: 
              if board[row][col] is None: 
                row = 0 
                pygame.draw.circle(DISPLAYSURF, yellow, (x_positions[col],y_positions[row]),radius)
                board[row][col] = "yellow"
                current_player = "red"  
              else:
                if board[5][col] is not None:
                  row = 0
                else: 
                  while board[row][col] is not None:
                    if row >4:
                      break
                    row += 1
                  if board[row][col] is None:
                    pygame.draw.circle(DISPLAYSURF, yellow, (x_positions[col],y_positions[row]),radius)
                    board[row][col] = "yellow"
                    current_player = "red"
                    row = 0

          elif current_player == "red":
            if row <=5: 
              if board[row][col] is None: 
                row = 0 
                pygame.draw.circle(DISPLAYSURF, red, (x_positions[col],y_positions[row]),radius)
                board[row][col] = "red"
                current_player = "yellow"  
              else:
                if board[5][col] is not None:
                  row = 0
                else: 
                  while board[row][col] is not None:
                    if row >4:
                      break
                    row += 1
                  if board[row][col] is None:
                    pygame.draw.circle(DISPLAYSURF, red, (x_positions[col],y_positions[row]),radius)
                    board[row][col] = "red"
                    current_player = "yellow"
                    row = 0

        
          
  pygame.display.update()
  game_over()
