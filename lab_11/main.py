import pygame
import random

screen = pygame.display.set_mode((620, 620))
pygame.display.set_caption("Snake game")
icon=pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

size_block = 40
kolonki = 15

background = (0, 8, 255)
white = (255, 255, 255)
blue = (0, 200, 245)
snake_color = (0, 200, 0)
red=(255, 42, 0)

snake_block = [[7, 5], [7, 6], [7, 7]]

def draw(color, x, y):
    pygame.draw.rect(screen, color, [10 + x * size_block, 10 + y * size_block, size_block, size_block])

def apple_generate(snake_block):
    while (True):
        x=random.randint(0,14)
        y=random.randint(0,14)
        if [x,y] not in snake_block:
            return [x,y]

timer = pygame.time.Clock()

m_x = 1 
m_y = 0
apple=0
zap=0

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and m_y != 1:
                m_y = -1
                m_x = 0
            elif event.key == pygame.K_DOWN and m_y != -1:
                m_y = 1
                m_x = 0
            elif event.key == pygame.K_LEFT and m_x != 1:
                m_y = 0
                m_x = -1
            elif event.key == pygame.K_RIGHT and m_x != -1:
                m_y = 0
                m_x = 1
# Поле
    screen.fill(background)
    for y in range(kolonki):
        for x in range(kolonki):
            if (y + x) % 2 == 0:
                color = white
            else:
                color = blue
            draw(color, x, y)

# Змея
    for i in snake_block:
        x,y = i
        draw(snake_color, x, y)

    head = snake_block[-1]
    x, y = head
    new_head = [x+m_x, y+m_y]
    if new_head in snake_block:
        runing=False
    snake_block.append(new_head)
    if zap!=1:
        snake_block.pop(0)
    else:
        zap=0

# Яблоко
    if apple==0:
        apple=apple_generate(snake_block)
        x_app,y_app=apple
        apple=1
    draw(red,x_app,y_app)

    if x_app==x+m_x and y_app==y+m_y:
        apple=0
        zap=1

    pygame.display.update()
    timer.tick(4)

# Проверка на выход за края  
    if not(0<=x+m_x<kolonki and 0<=y+m_y<kolonki):
        runing = False
pygame.quit()