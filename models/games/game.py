

class Game:

    def __init__(self, player_1_object, player_2_object):

        self.player_1_object = player_1_object
        self.player_2_object = player_2_object
        self.move_list = ['rock', 'paper', 'scissors']
    
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