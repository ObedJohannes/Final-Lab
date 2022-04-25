import random
import pygame
from pygame.locals import *

pygame.init()

#colors
diceColor = 255, 243, 194
white = 255, 255, 255
dotColor = 0, 0, 0
red = 255,0,0
green = 170, 255, 0
textboxcolor = 0, 50, 250
#background and screen settings
screenSize = (600, 338)
screen = pygame.display.set_mode((screenSize))
pygame.display.set_caption('Craps!')
background = pygame.image.load("craptableimage.png").convert_alpha()

#dice images
dice1 = pygame.image.load("1.png").convert_alpha()
dice2 = pygame.image.load("2.png").convert_alpha()
dice3 = pygame.image.load("3.png").convert_alpha()
dice4 = pygame.image.load("4.png").convert_alpha()
dice5 = pygame.image.load("5.png").convert_alpha()
dice6 = pygame.image.load("6.png").convert_alpha()

#final screen
winner = pygame.image.load("winScreen.png").convert_alpha()
loser = pygame.image.load("losescreen.png").convert_alpha()


#text code
font = pygame.font.Font('Didot-01.ttf', 50)
font2 = pygame.font.Font('Didot-01.ttf', 30)
winText = font.render('Congrats!', True, green)
loseText = font.render('You lost...', True, red)
retryText = font2.render('Press (R) to retry', True, diceColor)
pressSpace = font2.render('Press Space to roll', True, diceColor)
textBoxWin = winText.get_rect()
textBoxLose = loseText.get_rect()
displaySurface = pygame.display.set_mode((600, 338))



#game loop
end = False
while end == False:
    screen.fill(white)
    screen.blit(background, (0, 0))
    screen.blit(pressSpace, (167, 0))
    #game exit code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True


    #dice roll
        points = []

        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            die1 = random.randrange(1, 7)
            die2 = random.randrange(1, 7)
            tot = (die1 + die2)
            points.append(tot)



            #first Dice image
            if die1 == 1:

                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice1, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die1 == 2:
                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice2, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die1 == 3:
                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice3, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die1 == 4:
                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice4, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die1 == 5:
                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice5, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die1 == 6:
                screen.fill(white)
                screen.blit(background, (0, 0))
                screen.blit(dice6, (600/2, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)

            #secound Dice image
            if die2 == 1:
                screen.blit(dice1, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die2 == 2:
                screen.blit(dice2, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die2 == 3:
                screen.blit(dice3, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die2 == 4:
                screen.blit(dice4, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die2 == 5:
                screen.blit(dice5, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)
            elif die2 == 6:
                screen.blit(dice6, (600/4, 338/2))
                pygame.display.update()
                pygame.time.wait(1000)

            #game Rules

            if tot in (7, 11):
                outcome = "you won"
            #dispay you win


            elif tot in (2, 3, 12):
                outcome = "you lost"
            #display you lose

            else:
                outcome = "keep rolling"


            #display win/lose


            if outcome == "you won":
                screen.fill(white)
                screen.blit(background, (0, 0))
                displaySurface.blit(winText, textBoxWin)
                screen.blit(winner, (150, 50))
                pygame.time.wait(1000)
                screen.blit(retryText, (167, 0))

            if outcome == "you lost":
                screen.fill(white)
                screen.blit(background, (0, 0))
                displaySurface.blit(loseText, textBoxLose)
                screen.blit(loser, (250, 100))
                pygame.time.wait(1000)
                screen.blit(retryText, (167, 0))

            while outcome == "keep rolling" and len(points) > 1:
                point = int(points[0])

                if tot == 3:
                    outcome = "you lost"

                 #display you lose
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (250, 100))
                    pygame.time.wait(1000)
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    screen.blit(pressSpace, (167, 0))
                    pygame.display.update()


                elif tot == 7:
                    outcome = "you lost"

                   #display you lose
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (250, 100))
                    pygame.time.wait(1000)
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    screen.blit(pressSpace, (167, 0))
                    pygame.display.update()


                elif tot == 12:
                    outcome = "you lost"

                    #display you lose
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (250, 100))
                    pygame.time.wait(1000)
                    pygame.display.update()


                elif tot == point:
                    outcome = "you won"
                #dispay you win
                    screen.fill(white)
                    screen.blit(background, (0, 0))
                    displaySurface.blit(winText, textBoxWin)
                    screen.blit(winner, (250, 100))
                    pygame.time.wait(1000)
                    pygame.display.update()


        pygame.display.update()
        pygame.time.wait(1000)


pygame.quit()

