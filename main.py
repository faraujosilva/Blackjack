from player import Player
from dealer import Dealer
from engine import Engine
from deck import Deck

players = [
    Player('Fernando', 14000),
    Player('Gabriel', 5000),
    Dealer('MrDealer', 0),
]

deck_inst = Deck()

engine = Engine(players, deck_inst)

engine.start()