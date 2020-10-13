import pygame
SCALE = 15

class Player:
    def __init__(self, xpos, ypos): #Initializin Player
        self.position = [xpos, ypos]
        print("Player")

    def update(self):       #This is where the player will be updtated
        print("Update")

    def render(self, screen):       #Drwaing the player to the screen, of course this is just temporeraly
        pygame.draw.rect(screen, (255, 255, 255), (self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE), 6)


    def update_position(self, xpos, ypos):
        self.position[0] += xpos
        self.position[1] += ypos



