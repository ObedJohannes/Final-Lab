import random

import pygame, sys

pygame.init()

width = 600
height = 600

eggWhite = 255, 243, 194
backgroundColor = 145, 100, 146
dots = 15, 200, 16

x = 50
y = 50
hgt = 50
wdth = 50
vel = 80


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Craps!')
screen.fill(backgroundColor)

runtime = True
while runtime == True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
        if event.type == pygame.K_SPACE:
            roll = random.randint(1,6)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        x += vel
    def drawDieDot():
        pygame.draw.rect(screen, (dots), (x, y, 11, 11))

    screen.fill(backgroundColor)
    pygame.draw.rect(screen, (eggWhite), (x, y, wdth, hgt))
    drawDieDot()
    pygame.display.update()
