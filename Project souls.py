import pygame
from Game import Game, Game_State, Menu
# *** from Game_States import GameStates - I have merged this into Game.py
from pygame import mixer

pygame.init()       #initiatin pygame

mixer.music.load('Music/backgroundMusicFixed.wav')
mixer.music.play(-1)

GameWindow = pygame.display.set_mode((832, 832))        #Creating the game window

pygame.display.set_caption("Project Souls")      #adding the project name

clock = pygame.time.Clock()         #creating the framerate


GameWindow.fill((0, 0, 0))


game = Game(GameWindow)
menu = Menu(GameWindow)


menu.set_up_menu() # Setting up the menu
game.set_up()   #Setting up the objects


while game.Game_States == Game_State.RUNNING and menu.Game_States_Menu == Game_State.RUNNING:  # Keeps the game running while the state is in RUNNING
    clock.tick(60)  # setting the fps to 60
    if menu.isMenu:  # if "isMenu" is true then that means the game is on the menu screen and should use the menu update function
        menu.update()
    else:  # if "isMenu" is false then that means the game is on the game screen and should use the game update function
        game.update()  # Updating the game

    pygame.display.flip()  # Update the full display Surface to the screen

pygame.quit()  # *** Added to end the game


pygame.quit() # *** Added to end the game





