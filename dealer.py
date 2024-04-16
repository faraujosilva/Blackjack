from participant import Participant
from typing import List
from actions import Actions
from deck import Card

class Dealer(Participant):
    def __init__(self, name: str, action: Actions):
        super().__init__(name, action)
        self.dealer = True
