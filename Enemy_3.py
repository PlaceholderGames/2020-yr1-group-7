import pygame
from enum import Enum, unique

SCALE = 64

class Entity_3():
    def __init__(self):
        self.health = 80

    def attack(self, player):
        player.health += -1000
        print("I mean it's a souls game...what did you expect?! ")

    def defence(self):
        self.health += 5

    def get_health(self):
        return self.health

    def __setstate__(self, state):
        self.state = state

    def set_health(self, health):
        self.health = health

class Enemy_3_State(Enum):
    DEFAULT = 0  # this is for the setup
    MOVE = 1  # when the enemy is moving
    ATTACK = 2  # Enemy can attack
    DEFEND = 3  # Enemy can Defend
    DEAD = 4  #When the enemy dies

class Enemy_3(Entity_3):
    def __init__(self, xpos, ypos):
        super(Enemy_3, self).__init__()
        self.position = [xpos, ypos]
        self.image = pygame.image.load("Art_FIles\Monsters\head-crab.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)
        self.state = Enemy_3_State.DEFAULT

    def render(self, screen, camera):
        if self.state != Enemy_3_State.DEAD:
            self.rect = pygame.Rect((self.position[0] - camera[0]) * SCALE, (self.position[1] - camera[1]) * SCALE, SCALE, SCALE)

            screen.blit(self.image, self.rect)
