from participant import Participant
from actions import Actions


class Player(Participant):
    def __init__(self, name: str, action: Actions):
        super().__init__(name, action)
