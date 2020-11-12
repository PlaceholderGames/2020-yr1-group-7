import pygame
from enum import Enum, unique

SCALE = 64


class Enemy_State(Enum):
    DEFAULT = 0  # this is for the setup
    MOVE = 1  # when the enemy is moving
    ATTACK = 2  # Enemy can attack
    DEFEND = 3  # Enemy can Defend
    DEAD = 4  #When the enemy dies

class Enemy:
    def __init__(self, xpos, ypos):
        self.position = [xpos, ypos]
        self.image = pygame.image.load("Art_FIles\Monsters\Fish-men.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)
        self.state = Enemy_State.DEFAULT

    def render(self, screen):
        self.rect = pygame.Rect(self.position[0] * SCALE, self.position[1] * SCALE, SCALE, SCALE)

        screen.blit(self.image, self.rect)