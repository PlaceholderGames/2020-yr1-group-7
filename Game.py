from Player import Player, Player_State # *** incorporated FSM into Player.py
import pygame
import math
# *** from Game_States import GameStates - I have merged this into Game.py
from pygame import mixer
from enum import Enum

SCALE = 64

class Game_State(Enum):
    NONE = 0
    RUNNING = 1
    GAMEOVER = 2

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.Game_States =  Game_State.NONE #GameStates.NONE
        self.map = []
        self.camera = [0, 0]

    def set_up(self):
        player = Player(1, 0, "Player") # More aesthetically pleasing to have him start on the path :-) -- DoctorMike
        self.player = player
        self.player.state = Player_State.MOVE
        # *** print(self.player.state)
        self.objects.append(player)
        
        # *** NPC code here
        npc = Player(5,5, "NPC")
        npc.state = Player_State.MOVE
        self.objects.append(npc)
        
        self.Game_States = Game_State.RUNNING
        self.load_map("map2") # Changed the map to test X Axis scrolling -- DoctorMike
        # *** print("do the setup")


    def update(self):
        self.screen.fill((0, 0, 0))
        # print("updating")
        self.handle_events()
        self.render_the_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)
            if isinstance(object,Player):
                if object.type == "NPC":        # *** Here we can add other elif clauses to handle different NPCs in different ways
                    print('Found an NPC!!!')    # *** here we would do something with the NPCs
                    object.update()
                    
    def handle_events(self):
        walksoundone = pygame.mixer.Sound('Sounds/Walking sounds/Walk for project one.wav')
        walksoundtwo = pygame.mixer.Sound('Sounds/Walking sounds/Walk for project two.wav')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #this will end the while loop
                self.Game_States = Game_State.GAMEOVER

            elif event.type == pygame.KEYDOWN:          #Key events
                if event.key == pygame.K_ESCAPE:
                    # print('ESCAPE') ~ *** Used to check that Escape was detected
                    self.Game_States = Game_State.GAMEOVER
                elif self.player.state == Player_State.MOVE: # *** We don't want to be able to move if we are in Turn-Based Combat
                    if event.key == pygame.K_LEFT:
                        self.move_unit(self.player, [-1, 0])
                        walksoundone.play()
                    elif event.key == pygame.K_RIGHT:
                        self.move_unit(self.player, [1, 0])
                        walksoundtwo.play()
                    elif event.key == pygame.K_UP:
                        self.move_unit(self.player, [0, -1])
                        walksoundone.play()
                    elif event.key == pygame.K_DOWN:
                        self.move_unit(self.player, [0,1])
                        walksoundtwo.play()
                    elif event.key ==pygame.K_a: # *** This allows us to enter attack mode. Running into an NPC/Monster could automate this
                        print('Attack!!! Cannot move now')
                        self.player.state = Player_State.ATTACK
                    elif event.key ==pygame.K_d:
                    # *** This allows us to enter defend mode. Being run into by an NPC/Monster could automate this
                        print('Defend!!! Cannot move now')
                        self.player.state = Player_State.DEFEND      
                elif event.key ==pygame.K_a:                # *** This would allow us to be in a mode to choose an attack
                    print('Attack!!!')
                    self.player.state = Player_State.ATTACK
                elif event.key ==pygame.K_d:                # *** This would allow us to be in a mode to choose a defence
                    print('Defend!!!')
                    self.player.state = Player_State.DEFEND
                elif event.key == pygame.K_m:               # *** This allows us to move, or run away from an NPC
                    self.player.state = Player_State.MOVE
                    print('Able to move again!!!')
                    
    def load_map(self, file_name):
        with open("maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tile = []
                for i in range(0, len(line) - 1, 2):
                    tile.append(line[i])
                    
                self.map.append(tile)

    def render_the_map(self, screen):

        self.position_camera()
        tile_y = 0
        for line in self.map:
            tile_x = 0
            for tile in line:
                image = images_for_map[tile]
                rect = pygame.Rect((tile_x - self.camera[0]) * SCALE, (tile_y - self.camera[1]) * SCALE, SCALE, SCALE)
                screen.blit(image, rect)
                tile_x += 1
            tile_y += 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1): # *** changed from -2
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1): # *** BUG Fix, as we were not checking the number of rows properly
            return

        unit.update_position(new_position)
        return

    def position_camera(self):
        # Added X Axis Camera Stuff -- DoctorMike
        max_x_position = len(self.map[0]) - 832 / SCALE
        x_position = self.player.position[0] - math.ceil(round(832 / SCALE / 2))

        if x_position < max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position


        # End of additions -- DoctorMike
        
        max_y_position = len(self.map[1]) - 832 / SCALE
        y_position = self.player.position[1] - math.ceil(round(832 / SCALE / 2))

        if y_position < max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position



images_for_map = {
    "G": pygame.transform.scale(pygame.image.load("images\_tile1.png"), (SCALE, SCALE)),
    "R": pygame.transform.scale(pygame.image.load("images\_tile3.png"), (SCALE, SCALE))
}
