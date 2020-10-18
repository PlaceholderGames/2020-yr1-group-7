import pygame
SCALE = 64

class Player:
    def __init__(self, xpos, ypos): #Initializin Player
        self.position = [xpos, ypos]
        self.image = pygame.image.load("images\player.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)

        print("Player")

    def update(self):       #This is where the player will be updtated
        print("Update")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)

    def render(self, screen):       #Drwaing the player to the screen, of course this is just temporeraly
        screen.blit(self.image, self.rect)

