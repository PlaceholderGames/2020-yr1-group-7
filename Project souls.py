import pygame
from Game import Game
from Game_States import GameStates

pygame.init()       #initiatin pygame

GameWindow = pygame.display.set_mode((600, 600))        #Creating the game window

pygame.display.set_caption("Poject Souls")      #adding the project name

clock = pygame.time.Clock()         #creating the framerate


GameWindow.fill((0, 0, 0))

game = Game(GameWindow)


game.set_up()   #Setting up the objects


while game.Game_States == GameStates.RUNNING:     #Keeps the game running while the state is in RUNNING
    clock.tick(60)      #setting the fps to 60
    game.update()       #Updating the game
    pygame.display.flip() #Update the full display Surface to the screen




