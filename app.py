import pygame

pygame.init()

screen_width = 300
screen_height = 300
screen_size = (screen_width, screen_width)
screen = pygame.display.set_mode(screen_size)

FPS = 60

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)


class Board:
    def __init__(self):
        self.block_size = 100

    def draw_board(self):
        for y in range(3):
            if y == 0 or y == 2:
                for x in range(3):
                    if x % 2 == 0:
                        pygame.draw.rect(screen, RED, (x*100,y*100,self.block_size, self.block_size))
                pygame.draw.rect(screen, RED, (100,100,self.block_size, self.block_size))

    def get_pos(self):
        if event.pos[0] < 100 and event.pos[1] < 100:
            return 1
        if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] < 100:
            return 2            
        if event.pos[0] > 200 and event.pos[0] < 300 and event.pos[1] < 100:
            return 3 
        if event.pos[0] < 100 and event.pos[1] > 100 and event.pos[1] < 200:
            return 4 
        if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200:
            return 5 
        if event.pos[0] > 200 and event.pos[1] > 100 and event.pos[1] < 200:
            return 6
        if event.pos[0] < 100 and event.pos[1] > 200:
            return 7
        if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 200:
            return 8
        if event.pos[0] > 200 and event.pos[1] > 200:
            return 9
        else:
            pass
        

class Player:
    def __init__(self, color):
        self.color = color
        self.size = 30

    def draw_circle(self, pos):
        if pos == 1:
            self.pos_x = 50
            self.pos_y = 50
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 2:
            self.pos_x = 150
            self.pos_y = 50
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 3:
            self.pos_x = 250
            self.pos_y = 50
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 4:
            self.pos_x = 50
            self.pos_y = 150
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 5:
            self.pos_x = 150
            self.pos_y = 150
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 6:
            self.pos_x = 250
            self.pos_y = 150
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 7:
            self.pos_x = 50
            self.pos_y = 250
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 8:
            self.pos_x = 150
            self.pos_y = 250
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        if pos == 9:
            self.pos_x = 250
            self.pos_y = 250
            pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        

# def asd(turn):
#     try:
#         if block_list[1] == block_list[2] and block_list[2] == block_list[3]:
#             print(f"{turn} wins")

#     except:
#         pass
block_list = [""]

clock = pygame.time.Clock()

board = Board()
board.draw_board()
player_1 = Player(BLUE)
player_2 = Player(GREEN)

turn = "x"

run = True
while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            

            new_pos = board.get_pos()
            if new_pos not in block_list:
                block_list.insert(new_pos, turn)

                if turn == "x":
                    player_1.draw_circle(new_pos)
                    turn = "o"
                elif turn == "o":
                    new_pos = board.get_pos()
                    player_2.draw_circle(new_pos)
                    turn = "x"
    # asd(turn)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()