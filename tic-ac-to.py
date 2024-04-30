import pygame
pygame.init()
def game():

    d = pygame.display.set_mode((400,600))
   
    pygame.display.set_caption("tic-tac-to")
    pygame.display.update()
    xim = []
    oim = []
    ii = []
    p = []
    x_x = []
    x_y = []
    o_x = []
    o_y = []
    a = []
    a = []
    h = 95
    w = 95
    o_x = []
    o_y = []
    turn = "x"
    board = [1,2,3,
            4,5,6,
            7,8,9]
    x = True
    click = False

    def text_screen(text, color, x, y,size):
        font = pygame.font.SysFont(None, size)
        screen_text = font.render(text, True, color)
        d.blit(screen_text, [x, y])
    winning_combinations = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]

    # Function to check for win
    def check_win(mark):
        for combo in winning_combinations:
            if all(board[i] == mark for i in combo):
                return True
        return False
    def draw_box():
        pygame.draw.line(d, (0, 0, 0), (145, 45), (145, 375), 5)
        pygame.draw.line(d, (0, 0, 0), (255, 45), (255, 375), 5)
        pygame.draw.line(d, (0, 0, 0), (30, 145), (375, 145), 5)
        pygame.draw.line(d, (0, 0, 0), (30, 255), (375, 255), 5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos = pygame.mouse.get_pos()
                        
        v1 = pygame.Rect(40, 40,h,w)
        pygame.draw.rect(d, (0,0,0), v1)
        
        v2 = pygame.Rect(40, 155,h,w)
        pygame.draw.rect(d, (0,0,0), v2)
        
        v3 = pygame.Rect(40, 155+95+15,h,w)
        pygame.draw.rect(d, (0,0,0), v3)
        
        v4 = pygame.Rect(30+25+95, 40,h,w)
        pygame.draw.rect(d, (0,0,0), v4)
        
        v5 = pygame.Rect(30+25+95, 155,h,w)
        pygame.draw.rect(d, (0,0,0), v5)
        
        v6 = pygame.Rect(30+25+95,155+95+15,h,w)
        pygame.draw.rect(d, (0,0,0), v6)
        
        v7 = pygame.Rect(30+25+95+95+20, 40,h,w)
        pygame.draw.rect(d, (0,0,0), v7)
        
        v8 = pygame.Rect(30+25+95+95+20, 155,h,w)
        pygame.draw.rect(d, (0,0,0), v8)
        
        v9 = pygame.Rect(30+25+95+95+20, 155+95+15,h,w)
        pygame.draw.rect(d, (0,0,0), v9)
                
                



        d.fill((255,255,255))
        
        
        if pygame.Rect.collidepoint(v1, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                
                click = True
                if (40, 40) not in zip(x_x, x_y) and (40, 40) not in zip(o_x, o_y):
                    if turn == "x":
                        x_x.append(40)
                        x_y.append(40)
                        turn = "o"
                        board[0] = "x"
                    elif turn == "o":
                        o_x.append(40)
                        o_y.append(40)
                        turn = "x"
                        board[0] = "o"
            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v2, pos[0], pos[1]): 
                    if pygame.mouse.get_pressed()[0] == 1 and click == False:
                        click = True
                        
                        if (40, 155) not in zip(x_x, x_y) and (40, 155) not in zip(o_x, o_y):
                            if turn == "x":
                                
                                x_x.append(40)
                                x_y.append(155)
                                turn = "o"
                                board[1] = "x"

                            elif turn == "o":
                                o_x.append(40)
                                o_y.append(155)
                                turn = "x"
                                board[1] = "o"

        if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v3, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (40, 155+95+15) not in zip(x_x, x_y) and (40, 155+95+15) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(40)
                        x_y.append(155+95+15)
                        turn = "o"
                        board[2] = "x"

                    elif turn == "o":
                        o_x.append(40)
                        o_y.append(155+95+15)
                        turn = "x"
                        board[2] = "o"

            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v4, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (30+25+95,40) not in zip(x_x, x_y) and (30+25+95, 40) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(30+25+95)
                        x_y.append(40)
                        turn = "o"
                        board[3] = "x"

                    elif turn == "o":
                        o_x.append(30+25+95)
                        o_y.append(40)
                        turn = "x"
                        board[3] = "o"

            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v5, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (30+25+95, 155) not in zip(x_x, x_y) and (30+25+95, 155) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(30+25+95)
                        x_y.append(155)
                        turn = "o"
                        board[4] = "x"

                    elif turn == "o":
                        o_x.append(30+25+95)
                        o_y.append(155)
                        turn = "x"
                        board[4] = "o"

            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v6, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (30+25+95,155+95+15) not in zip(x_x, x_y) and (30+25+95,155+95+15) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(30+25+95)
                        x_y.append(155+95+15)
                        turn = "o"
                        board[5] = "x"

                    elif turn == "o":
                        o_x.append(30+25+95)
                        o_y.append(155+95+15)
                        turn = "x"
                        board[5] = "o"
            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v7, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (30+25+95+95+20,40) not in zip(x_x, x_y) and (30+25+95+95+20,40) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(30+25+95+95+20)
                        x_y.append(40)
                        turn = "o"
                        board[6] = "x"

                    elif turn == "o":
                        o_x.append(30+25+95+95+20)
                        o_y.append(40)
                        turn = "x"
                        board[6] = "o"

            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v8, pos[0], pos[1]): 
            if pygame.mouse.get_pressed()[0] == 1 and click == False:
                click = True
                
                if (30+25+95+95+20, 155) not in zip(x_x, x_y) and (30+25+95+95+20, 155) not in zip(o_x, o_y):
                    if turn == "x":
                        
                        x_x.append(30+25+95+95+20)
                        x_y.append(155)
                        turn = "o"
                        board[7] ="x"

                    elif turn == "o":
                        o_x.append(30+25+95+95+20)
                        o_y.append(155)
                        turn = "x"
                        board[7] = "o"


            if pygame.mouse.get_pressed()[0] == 0:
                click = False

        if pygame.Rect.collidepoint(v9, pos[0], pos[1]): 
                    if pygame.mouse.get_pressed()[0] == 1 and click == False:
                        click = True
                    
                        if (30+25+95+95+20, 155+95+15) not in zip(x_x, x_y) and (30+25+95+95+20, 155+95+15) not in zip(o_x, o_y):
                            if turn == "x":
                                board[8] = "x"
                                x_x.append(30+25+95+95+20)
                                x_y.append(155+95+15)
                                turn = "o"

                            elif turn == "o":
                                o_x.append(30+25+95+95+20)
                                o_y.append(155+95+15)
                                turn = "x"
                                board[8] = "o"
                    if pygame.mouse.get_pressed()[0] == 0:
                        click = False
        draw_box()
        for x_pos, y_pos in zip(x_x, x_y):
            text_screen("X", "red", x_pos, y_pos, 180)
        

        for xo_pos, yo_pos in zip(o_x, o_y):
            text_screen("O", "blue", xo_pos, yo_pos, 180)

        if check_win('x'):
            
            pygame.draw.rect(d,"green", (90, 200, 250, 70))
            text_screen("X wins!", "blue", 90, 200, 100)
            pygame.draw.rect(d,"green", (50, 300, 300, 80))
            text_screen("play again!", "blue", 50, 300, 80)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                  game()
                  turn = "o" if turn == "x" else "x"
            # You can add code here to handle end of the game, such as displaying a message and resetting the game
        elif check_win('o'):
        
            pygame.draw.rect(d,"green", (90, 200, 250, 70))
            text_screen("O wins!", "red", 90, 200, 100)
            pygame.draw.rect(d,"green", (50, 300, 300, 80))
            text_screen("play again!", "red", 50, 300, 80)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                  game()
                  turn = "o" if turn == "x" else "x"
            
            

            # You can add code here to handle end of the game, such as displaying a message and resetting the game
        elif all(cell in ['x', 'o'] for cell in board):
            pygame.draw.rect(d,"green", (90, 200, 250, 70))
            text_screen("Draw!", "blue", 90, 200, 100)
            pygame.draw.rect(d,"green", (50, 300, 300, 80))
            text_screen("play again!", "blue", 50, 300, 80)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                  game()
                  turn = "o" if turn == "x" else "x"
        
        
        #print(turn)
        text_screen(f"{turn}'s Turn", "black", 90, 400, 100)
        pygame.display.update()
        
game()