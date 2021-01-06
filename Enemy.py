import pygame
from enum import Enum, unique

SCALE = 64

class Entity_1():
    def __init__(self):
        self.health = 100

    def attack(self, player):
        player.health += -30

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
        self.hitbox = (self.position[0] + 20, self.position[1], 28, 60)

    def render(self, screen, camera):
        if self.state != Enemy_State.DEAD:
            self.hitbox = (self.position[0] + 20, self.position[1], 28, 60)
            self.rect = pygame.Rect((self.position[0] - camera[0]) * SCALE, (self.position[1] - camera[1]) * SCALE, SCALE, SCALE)
            screen.blit(self.image, self.rect)
