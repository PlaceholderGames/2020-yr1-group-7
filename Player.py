import pygame
from enum import Enum, unique
SCALE = 64

class Entity():
    def __init__(self):
        self.health = 100

    def attack(self, target):
        target.health += -15

    def defence(self):
        self.health += 5

    def get_health(self):
        return self.health

    def __setstate__(self, state):
        self.state = state

    def set_health(self, health):
        self.health = health


class Player_State(Enum):
    DEFAULT = 0 # *** Only used before set up
    MOVE = 1    # *** The default mode to move
    ATTACK = 2  # *** Could be used in Turn-Based Combat
    DEFEND = 3  # *** Could be used in Turn-Based Combat
    DEAD = 4    # *** Obvious really
    
class Player(Entity):
    def __init__(self, xpos, ypos): #Initializin Player
        super(Player, self).__init__()
        self.position = [xpos, ypos]
        self.image = pygame.image.load("images\player.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)
        self.state = Player_State.DEFAULT
        # print("Player")

    def update(self):       #This is where the player will be updated
        print("Update")     #It would need to be called from Game.py for each update, but could automate the state

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def render(self, screen, camera):  # Drawing the player to the screen, of course this is just temporeraly
        if self.state != Player_State.DEAD:
            self.rect = pygame.Rect((self.position[0] - camera[0]) * SCALE, (self.position[1] - camera[1]) * SCALE, SCALE, SCALE)

        # Error identified and fixed -- DoctorMike
        # Your error was in the above. You had (self.position[1] - camera[1]*SCALE)*SCALE
        # What you needed was (self.position[1] - camera[1])* SCALE
        # I also added a camera[0] for the x axis, in case you ever wanted side scrolling
        # These changes occurred in Game.py too
            screen.blit(self.image, self.rect)
