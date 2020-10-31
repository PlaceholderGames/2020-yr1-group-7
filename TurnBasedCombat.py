class FSM:
    def __init__(self):
        self.start = self.start_combat()
        self.player = self.player_turn()
        self.enemy = self.enemy_turn()

        self.current_state = self.start
        self.combat_end = False

    def send(self, char):
        self.current_state(char)

    def start_combat(self):
        while not self.combat_end:
            self.current_state = self.player

    def player_turn(self):
        while not self.combat_end:
            char = yield
            if char == 'a':
                print("Attacking enemy")
                self.current_state = self.enemy
                break
            elif char == 'b':
                print("Defending against enemy")
                self.current_state = self.enemy
                break
            else:
                print("please choose an action")
                self.current_state =self.player


    def enemy_turn(self):
        while not self.combat_end:
            print("Attacking Player")
            self.current_state = self.player
            break

