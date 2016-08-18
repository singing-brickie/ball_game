import pygame
import sys


pygame.init()
size= width ,  heigth = 500 ,600
screen = pygame.display.set_mode(size)
ball = pygame.image.load('ball.jpg')
ball = pygame.transform.scale(ball, (25, 25))
white= 255,255,255
speed=[2,2]
ballRect= ball.get_rect()
while 1:
    pygame.time.wait(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if speed[0] > 0:
                    speed[0]=-speed[0]
            if event.key == pygame.K_RIGHT:
                if speed[0] < 0:
                    speed[0] = -speed[0]
            if event.key == pygame.K_UP:
                if speed[1] > 0:
                    speed[1] = -speed[1]
            if event.key == pygame.K_DOWN:
                if speed[1] < 0:
                    speed[1] = -speed[1]

    ballRect=ballRect.move(speed)
    if ballRect.left <0 or ballRect.right>500:
        speed[0]=-speed[0]
    if ballRect.bottom<0 or ballRect.top>600:
        speed[1]=-speed[1]
    screen.fill(white)
    screen.blit(ball, ballRect)
    pygame.display.update()
