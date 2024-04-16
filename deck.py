import random
from typing import List
from enum import Enum
from pydantic import BaseModel


class Cards(Enum):
    ACE = 'ACE'
    TWO = 'TWO'
    THREE = 'THREE'
    FOUR = 'FOUR'
    FIVE = 'FIVE'
    SIX = 'SIX'
    SEVEN = 'SEVEN'
    EIGHT = 'EIGHT'
    NINE = 'NINE'
    TEN = 'TEN'
    JACK = 'JACK'
    QUEEN = 'QUEEN'
    KING = 'KING'

class Suits(Enum):
    SPADES = 'SPADES'
    HEARTS = 'HEARTS'
    DIAMONDS = 'DIAMONDS'
    CLUBS = 'CLUBS'

class Card(BaseModel):
    name: str
    point: int = 0
    suit: str

class Deck:
    def __init__(self):
        self.deck = []

    def new(self) -> List[Card]:
        '''
        4 cartas por nipe
        '''
        self.deck = [Card(name=card.name, suit=suit.value) for suit in list(Suits) for card in list(Cards)]
        self.deck = self._set_card_points()
        self._shuffle()
        return self.deck
        
    def update(self, card_to_remove: Card):
        for card in self.deck:
            if card_to_remove.name == card.name and card.suit == card_to_remove.suit:
                self.deck.remove(card)
    
    def _set_card_points(self):
        mapp = {
            'ACE': 10,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'SEVEN': 7,
            'EIGHT': 8,
            'NINE': 9,
            'TEN': 10,
            'JACK': 10,
            'QUEEN': 10,
            'KING': 10
        }
        for card in self.deck:
            card.point = mapp.get(card.name)
        return self.deck
        
    def _shuffle(self):
        print(f"Shuffling deck right now!")
        self.deck = random.sample(self.deck, len(self.deck))
    