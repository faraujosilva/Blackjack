from player import Player
from dealer import Dealer
from deck import Deck
from engine import Engine
from actions import Actions

actions = Actions()
players = [
    Player('++Fernando++', actions),
    Player('++Gabriel++', actions)
]

dealer =  Dealer('++Mr Dealer++', actions)

deck = Deck()

engine = Engine(players, dealer, deck)

engine.run()