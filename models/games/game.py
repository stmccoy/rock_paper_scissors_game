class Game:

    def __init__(self, player_1_object, player_2_object):

        self.player_1_object = player_1_object
        self.player_2_object = player_2_object
        self.move_list = ['rock', 'paper', 'scissors']
    
    def winner(self):
        if player_1_object.move == 'rock':
            if player_2_object == 'paper':
                return "Player 2 wins"
            elif player_2_object == 'paper':
                return "Player 1 wins"
            else:
                return "It's a draw"
        elif player_1_object.move == 'paper':
            if player_2_object == 'scissors':
                return "Player 2 wins"
            elif player_2_object == 'rock':
                return "Player 1 wins"
            else:
                return "It's a draw"
        else: 
            if player_2_object == 'rock':
                return "Player 2 wins"
            elif player_2_object == 'paper':
                return "Player 1 wins"
            else:
                return "It's a draw"