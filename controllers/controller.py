from app import app
from flask import render_template, request, redirect, url_for
from models.players.player import Player
from models.games.game import Game
from models.games.play import game_1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pvp1', methods=['POST', 'GET'])
def pvp1():
    if request.method == 'POST':
        player_1_move = request.form.get('move')
        game_1.set_player_1_attribute(player_1_move)
        return redirect(url_for('pvp2'))
    return render_template('player-1.html')

@app.route('/pvp2', methods=['POST', 'GET'])
def pvp2():
    if request.method == 'POST':
        player_2_move = request.form.get('move')
        game_1.set_player_2_attribute(player_2_move)
        return redirect(url_for('winner'))
    return render_template('player-2.html')

@app.route('/winner', methods=['POST', 'GET'])
def winner():
    result = game_1.winner()
    player_1_input = game_1.player_1_object.move
    player_2_input = game_1.player_2_object.move
    return render_template('winner.html', result=result, player_1_input=player_1_input, player_2_input=player_2_input)

@app.route('/pvc', methods=['POST', 'GET'])
def pvc1():
    if request.method == 'POST':
        player_1_move = request.form.get('move')
        game_1.set_player_1_attribute(player_1_move)
        game_1.computer_move_select()
        return redirect(url_for('winner'))
    return render_template('cpu.html')

