import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("シューティングゲーム")
img = pygame.image.load("player.png")
img2 = pygame.image.load("enemy.png")
x = 370
y = 480
x2 = 200
y2 = 200


running = True
while running:
    screen.blit(img, (x, y))
    screen.blit(img2, (x2, y2))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                screen.fill((255, 0, 0))
                x +=1
            if event.key == K_LEFT:
                screen.fill((0, 0, 255))
                x -=1
            if event.key == K_UP:
                screen.fill((0, 255, 0))

            if event.key == K_DOWN:
                screen.fill((255, 255, 255))

    pygame.display.update()