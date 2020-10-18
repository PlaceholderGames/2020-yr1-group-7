from Player import Player
import pygame
from Game_States import GameStates

SCALE = 64

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.Game_States = GameStates.NONE
        self.map = []

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.Game_States = GameStates.RUNNING
        self.load_map("map1")
        print("do the setup")

    def update(self):
        self.screen.fill((0, 0, 0))
        print("updating")
        self.handle_events()
        self.render_the_map(self.screen)

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
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_RIGHT:
                    self.move_unit(self.player, [1, 0])
                elif event.key == pygame.K_UP:
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_DOWN:
                    self.move_unit(self.player, [0, 1])

    def load_map(self, file_name):
        with open("maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tile = []
                for i in range(0, len(line) - 1, 2):
                    tile.append(line[i])
                    
                self.map.append(tile)

    def render_the_map(self, screen):
        tile_y = 0
        for line in self.map:
            tile_x = 0
            for tile in line:
                image = images_for_map[tile]
                rect = pygame.Rect(tile_x * SCALE, tile_y * SCALE, SCALE, SCALE)
                screen.blit(image, rect)
                tile_x += 1
            tile_y += 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 2):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map[0]) - 2):
            return

        unit.update_position(new_position)


images_for_map = {
    "G": pygame.transform.scale(pygame.image.load("images\_tile1.png"), (SCALE, SCALE)),
    "R": pygame.transform.scale(pygame.image.load("images\_tile3.png"), (SCALE, SCALE))
}