from participant import Participant

class Player(Participant):
    def __init__(self, name: str, balance: int):
        super().__init__(name, balance)
