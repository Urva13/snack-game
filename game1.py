import pygame
import time
import random
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
DIS_WIDTH = 500
DIS_HEIGHT = 500
BLOCK_SIZE = 10
SNAKE_SPEED = 10
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(DIS, GREEN, [x[0], x[1], block_size, block_size])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DIS.blit(mesg, [DIS_WIDTH /3, DIS_HEIGHT/3 ])
def gameLoop():
    game_over = False
    game_close = False
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            DIS.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLUE)
        pygame.draw.rect(DIS, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(BLOCK_SIZE, snake_List)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(SNAKE_SPEED)
    pygame.quit()
    quit()
gameLoop()