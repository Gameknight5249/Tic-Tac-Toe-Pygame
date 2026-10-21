import pygame
import math
pygame.init()


screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Tic Tac Toe")

clicked_boxes = []
X_clicked = False
current_player = "X"   
game_over = False


## Starting coordinates of the top left square
x_coordinate = 170
y_coordinate = 100


## Checking if the box is taken
def box_checker (row, col):
    for clicked_row, clicked_col, player  in clicked_boxes:
      if clicked_row == row and clicked_col == col:
        return True
    return False



## Placing "O" or "X"
def drawX(row, col, current_player):
    if current_player == "X":
        if row == 0 and col == 0:
          pygame.draw.line(screen, (0,0,0), (x_coordinate - 80, y_coordinate -80), (x_coordinate + 80,y_coordinate +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate +80, y_coordinate - 80), (x_coordinate - 80, y_coordinate+ 80), 5)
          
        if row == 1 and col == 0:
          pygame.draw.line(screen, (0,0,0), (x_coordinate - 80, y_coordinate + 200 - 80), (x_coordinate + 80,y_coordinate + 200 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate +80, y_coordinate + 200  - 80), (x_coordinate - 80, y_coordinate + 200 + 80), 5)
          
        if row == 2 and col == 0:
          pygame.draw.line(screen, (0,0,0), (x_coordinate - 80, y_coordinate + 400 -80), (x_coordinate + 80,y_coordinate + 400 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate +80, y_coordinate + 400 - 80), (x_coordinate - 80, y_coordinate + 400 + 80), 5)
          
        if row == 0 and col == 1:
          pygame.draw.line(screen, (0,0,0), (x_coordinate  + 280 - 80, y_coordinate -80), (x_coordinate + 280 + 80,y_coordinate +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 280 +80, y_coordinate - 80), (x_coordinate + 280 - 80, y_coordinate+ 80), 5)
          
        if row == 1 and col == 1:
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 280 - 80, y_coordinate + 200 -80), (x_coordinate + 280 + 80,y_coordinate + 200 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 280 +80, y_coordinate + 200 - 80), (x_coordinate+ 280 - 80, y_coordinate + 200 + 80), 5)
          
        if row == 2 and col == 1:
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 280 - 80, y_coordinate + 400 - 80),(x_coordinate + 280 + 80, y_coordinate + 400 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 280 +80, y_coordinate + 400  - 80), (x_coordinate + 280 - 80, y_coordinate + 400 + 80), 5)
           
        if row == 0 and col == 2: 
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 - 80, y_coordinate -80), (x_coordinate + 560 + 80,y_coordinate +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 +80, y_coordinate - 80), (x_coordinate + 560 - 80, y_coordinate+ 80), 5)
          
        if row == 1 and col == 2:
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 - 80, y_coordinate + 200 -80), (x_coordinate + 560 + 80,y_coordinate + 200 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 +80, y_coordinate + 200 - 80), (x_coordinate +560 - 80, y_coordinate + 200 + 80), 5)
          
        if row == 2 and col == 2:
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 - 80, y_coordinate + 400 -80), (x_coordinate + 560 + 80,y_coordinate + 400 +80), 5)
          pygame.draw.line(screen, (0,0,0), (x_coordinate + 560 +80, y_coordinate + 400 - 80), (x_coordinate + 560 - 80, y_coordinate + 400 + 80), 5)
          
    if current_player == "O":
        if row == 0 and col == 0:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate, y_coordinate), (75), 5)
            
        if row == 1 and col == 0:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate, y_coordinate + 200), (75), 5)
            
        if row == 2 and col == 0:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate, y_coordinate + 400), (75), 5)
            
        if row == 0 and col == 1:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 280, y_coordinate), (75), 5)
            
        if row == 1 and col == 1:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 280, y_coordinate + 200), (75), 5)
            
        if row == 2 and col == 1:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 280, y_coordinate + 400), (75), 5)
            
        if row == 0 and col == 2:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 560, y_coordinate ), (75), 5)
            
        if row == 1 and col == 2:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 560, y_coordinate+ 200 ), (75), 5)
            
        if row == 2 and col == 2:
            pygame.draw.circle(screen, (0,0,0), (x_coordinate + 560, y_coordinate+ 400 ), (75), 5)
            







running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                   
            mouse_x, mouse_y = event.pos

            col = math.floor(mouse_x // 300)
            row = math.floor(mouse_y // 200)

            
            if not box_checker(row, col):
              clicked_boxes.append((row, col, current_player))

              if current_player == "O":
                current_player = "X"
              else:
                current_player = "O"

            
      
            

            

            
               


        
        
    screen.fill((255, 255, 255))     

    pygame.draw.line(screen,(0,0,0),(300,0),(300,600), 3)
    pygame.draw.line(screen,(0,0,0),(600,0),(600,600), 3)
    pygame.draw.line(screen,(0,0,0),(0,200),(900,200), 3)
    pygame.draw.line(screen,(0,0,0),(0,400),(900,400), 3)           

    for row, col, player  in clicked_boxes:
        drawX(row, col, player)   

   



    if game_over == False:
      
      ## O Win Conditions

      if (0,0,"O") in clicked_boxes and (0,1,"O") in clicked_boxes and (0,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True
      
      if (1,0,"O") in clicked_boxes and (1,1,"O") in clicked_boxes and (1,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (2,0,"O") in clicked_boxes and (2,1,"O") in clicked_boxes and (2,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (0,0,"O") in clicked_boxes and (1,0,"O") in clicked_boxes and (2,0,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (0,1,"O") in clicked_boxes and (1,1,"O") in clicked_boxes and (2,1,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (0,2,"O") in clicked_boxes and (1,2,"O") in clicked_boxes and (2,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (0,0,"O") in clicked_boxes and (1,1,"O") in clicked_boxes and (2,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True

      if (2,0,"O") in clicked_boxes and (1,1,"O") in clicked_boxes and (0,2,"O")  in clicked_boxes:
        print("Yay O won")
        game_over = True


      ## X Win Conditions

      if (0,0,"X") in clicked_boxes and (0,1,"X") in clicked_boxes and (0,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True
      
      if (1,0,"X") in clicked_boxes and (1,1,"X") in clicked_boxes and (1,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (2,0,"X") in clicked_boxes and (2,1,"X") in clicked_boxes and (2,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (0,0,"X") in clicked_boxes and (1,0,"X") in clicked_boxes and (2,0,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (0,1,"X") in clicked_boxes and (1,1,"X") in clicked_boxes and (2,1,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (0,2,"X") in clicked_boxes and (1,2,"X") in clicked_boxes and (2,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (0,0,"X") in clicked_boxes and (1,1,"X") in clicked_boxes and (2,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True

      if (2,0,"X") in clicked_boxes and (1,1,"X") in clicked_boxes and (0,2,"X")  in clicked_boxes:
        print("Yay X won")
        game_over = True
    
    
    pygame.display.update()


pygame.quit()