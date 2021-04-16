from models.players.player import Player
from models.games.game import Game

player_1 = Player()
player_2 = Player()

game_1 = Game(player_1, player_2)

def set_player_1_attribute(game_object, attribute_to_set):
    game_object.player_1_object.move = attribute_to_set

def set_player_2_attribute(game_object, attribute_to_set):
    game_object.player_2_object.move = attribute_to_set