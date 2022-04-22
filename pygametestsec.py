import random
import pygame
import sys

pygame.init()

#colors
diceColor = 255, 243, 194
dotColor = 0, 0, 0
red = 255,0,0
green = 34,139,34
textboxcolor = 20, 50, 90
#background and screen settings
screenSize = (600, 338)
screen = pygame.display.set_mode((screenSize))
pygame.display.set_caption('Craps!')
background = pygame.image.load("craptableimage.png")

#dice images
dice1 = pygame.image.load("1.png")
dice2 = pygame.image.load("2.png")
dice3 = pygame.image.load("3.png")
dice4 = pygame.image.load("4.png")
dice5 = pygame.image.load("5.png")
dice6 = pygame.image.load("6.png")

#final screen
winner = pygame.image.load("winScreen.png")
loser = pygame.image.load("losescreen.png")

#text code
font = pygame.font.Font('Didot-01.ttf', 20)
winText = font.render('Congrats you won!', True, green, textboxcolor)
loseText = font.render('Congrats you won!', True, red, textboxcolor)
textBoxWin = winText.get_rect()
textBoxLose = loseText.get_rect()
displaySurface = pygame.display.set_mode((600, 338))

#game loop
end = False
while end == False:

    #game exit code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    #game logic

        if event.type == pygame.KEYDOWN:
            die1 = random.randrange(1, 7)
            die2 = random.randrange(1, 7)
            #first Dice image
            if die1 == 1:
                screen.blit(dice1,(600/2, 338/2))
                pygame.display.flip()
            if die1 == 2:
                screen.blit(dice2,(600/2, 338/2))
                pygame.display.flip()
            if die1 == 3:
                screen.blit(dice3,(600/2, 338/2))
                pygame.display.flip()
            if die1 == 4:
                screen.blit(dice4,(600/2, 338/2))
                pygame.display.flip()
            if die1 == 5:
                screen.blit(dice5,(600/2, 338/2))
                pygame.display.flip()
            if die1 == 6:
                screen.blit(dice6,(600/2, 338/2))
                pygame.display.flip()

            #secound Dice image
            if die2 == 1:
                screen.blit(dice1,(600/4, 338/2))
                pygame.display.flip()
            if die2 == 2:
                screen.blit(dice2,(600/4, 338/2))
                pygame.display.flip()
            if die2 == 3:
                screen.blit(dice3,(600/4, 338/2))
                pygame.display.flip()
            if die2 == 4:
                screen.blit(dice4,(600/4, 338/2))
                pygame.display.flip()
            if die2 == 5:
                screen.blit(dice5,(600/4, 338/2))
                pygame.display.flip()
            if die2 == 6:
                screen.blit(dice6,(600/4, 338/2))
                pygame.display.flip()

            #game  Rules
            tot = die1 + die2

            if tot in (7, 11):
                outcome = "you won"
            #dispay you win
                displaySurface.blit(winText, textBoxWin)
                screen.blit(winner, (600 / 2, 338 / 2))

            elif tot in (2, 3, 12):
                outcome = "you lost"
            #display you lose
                displaySurface.blit(loseText, textBoxLose)
                screen.blit(loser, (600 / 2, 338 / 2))

            else:
                outcome = "keep rolling"
                currentpoint = tot
            #display point

            while outcome == "keep rolling":

                if currentpoint == tot:
                    outcome = "you won"
                #dispay you win
                    displaySurface.blit(winText, textBoxWin)
                    screen.blit(winner, (600 / 2, 338 / 2))

                elif tot == 3:
                    outcome = "you lost"
                 #display you lose
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (600 / 2, 338 / 2))

                elif tot == 7:
                    outcome = "you lost"
                   #display you lose
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (600 / 2, 338 / 2))

                elif tot == 12:
                    outcome = "you lost"
                    #display you lose
                    displaySurface.blit(loseText, textBoxLose)
                    screen.blit(loser, (600 / 2, 338 / 2))






        #craps table background
        screen.blit(background, (0, 0))
        pygame.display.update()

pygame.quit()

