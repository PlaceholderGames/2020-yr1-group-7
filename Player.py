import pygame
#from enum import Enum, unique
SCALE = 64

class Player:
    def __init__(self, xpos, ypos): #Initializin Player
        self.position = [xpos, ypos]
        self.image = pygame.image.load("images\player.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)

        print("Player")

    def update(self):       #This is where the player will be updated
        print("Update")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self, screen, camera):           #Drawing the player to the screen, of course this is just temporeraly
        self.rect = pygame.Rect((self.position[0] - camera[0]) * SCALE, (self.position[1] - camera[1]) * SCALE, SCALE, SCALE)

        # Error identified and fixed -- DoctorMike
        # Your error was in the above. You had (self.position[1] - camera[1]*SCALE)*SCALE
        # What you needed was (self.position[1] - camera[1])* SCALE
        # I also added a camera[0] for the x axis, in case you ever wanted side scrolling
        # These changes occurred in Game.py too

        screen.blit(self.image, self.rect)
