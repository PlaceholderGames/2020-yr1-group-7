from Player import Player
import pygame
from Game_States import GameStates


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.Game_States = GameStates.NONE

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.Game_States = GameStates.RUNNING
        print("do the setup")

    def update(self):
        self.screen.fill((0, 0, 0))
        print("updating")
        self.handle_events()

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #this will end the while loop
                self.Game_States = GameStates.GAMEOVER

            elif event.type == pygame.KEYDOWN:          #Key events
                if event.key == pygame.K_ESCAPE:
                    self.Game_States = GameStates.GAMEOVER
                elif event.key == pygame.K_LEFT:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.update_position(1, 0)
                elif event.key == pygame.K_UP:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.update_position(0, 1)