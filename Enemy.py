import pygame
import random
from enum import Enum, unique

SCALE = 64

class Entity_1():
    def __init__(self):
        self.health = 25

    def attack(self, player):
        player.health += -7

    def defence(self):
        self.health += 5

    def counter(self):
        return random.randint(0, 100)

    def critical_attack(self, target):
        target.health += -50
        print("GRRRRRRRR!!!!!!")

    def get_health(self):
        return self.health

    def __setstate__(self, state):
        self.state = state

    def set_health(self, health):
        self.health = health

class Enemy_State(Enum):
    DEFAULT = 0  # this is for the setup
    MOVE = 1  # when the enemy is moving
    ATTACK = 2  # Enemy can attack
    DEFEND = 3  # Enemy can Defend
    DEAD = 4  #When the enemy dies

class Enemy(Entity_1):
    def __init__(self, xpos, ypos):
        super(Enemy, self).__init__()
        self.position = [xpos, ypos]
        self.image = pygame.image.load("Art_FIles\Monsters\Fish-men.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)
        self.state = Enemy_State.DEFAULT

    def render(self, screen, camera):
        if self.state != Enemy_State.DEAD:
            self.rect = pygame.Rect((self.position[0] - camera[0]) * SCALE, (self.position[1] - camera[1]) * SCALE, SCALE, SCALE)
            screen.blit(self.image, self.rect)
