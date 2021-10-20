import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("^-^")
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bullet = pygame.image.load("bullet.png")
playerX = 400 - player.get_width() / 2
playerY = 500
enemyX = 200
enemyY = 200


running = True
while running:
    screen.fill((0, 0, 0,))
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    # screen.blit(bullet,(playerX+ player.get_width() / 2 - bullet.get_width()/2, playerY- bullet.get_width()))

    key_press = pygame.key.get_pressed()
    if key_press[K_RIGHT]:
        if playerX < 800-player.get_width():
            playerX += 1.5
    if key_press[K_LEFT]:
        if playerX > 0:
            playerX -= 1.5
    if key_press[K_UP]:
        playerY -= 1.5
    if key_press[K_DOWN]:
        playerY += 1.5
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False




    pygame.display.update()