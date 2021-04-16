from models.players.player import Player
import random

class Game:

    def __init__(self, player_1_object, player_2_object= None):

        self.player_1_object = player_1_object
        self.player_2_object = player_2_object
        self.move_list = ['rock', 'paper', 'scissors']
        
    
    def set_player_1_attribute(self, attribute_to_set):
        self.player_1_object.move = attribute_to_set

    def set_player_2_attribute(self, attribute_to_set):
        self.player_2_object.move = attribute_to_set
    
    def winner(self):
        if self.player_1_object.move == 'rock':
            if self.player_2_object.move == 'paper':
                return "Player 2 wins"
            elif self.player_2_object.move == 'scissors':
                return "Player 1 wins"
            else:
                return "It's a draw"
        elif self.player_1_object.move == 'paper':
            if self.player_2_object.move == 'scissors':
                return "Player 2 wins"
            elif self.player_2_object.move == 'rock':
                return "Player 1 wins"
            else:
                return "It's a draw"
        else: 
            if self.player_2_object.move == 'rock':
                return "Player 2 wins"
            elif self.player_2_object.move == 'paper':
                return "Player 1 wins"
            else:
                return "It's a draw"
            
    def computer_move_select(self):
        cpu_move= random.randint(0,2)
        self.player_2_object = Player()
        self.player_2_object.move = self.move_list[cpu_move]
