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
        game_1.player_1_object.move = request.form.get('move')
        return redirect(url_for('pvp2'))
    return render_template('player-1.html')

@app.route('/pvp2', methods=['POST', 'GET'])
def pvp2():
    if request.method == 'POST':
        game_1.player_2_object.move = request.form.get('move')
        return redirect(url_for('pvpwinner'))
    return render_template('player-2.html')

@app.route('/pvpwinner', methods=['POST', 'GET'])
def pvpwinner():
    return render_template('winner.html')

@app.route('/pvc1', methods=['POST', 'GET'])
def pvc1():
    return render_template('cpu-1.html')

