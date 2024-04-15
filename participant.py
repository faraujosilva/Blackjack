from deck import Card
from typing import List
from abc import ABC, abstractmethod
from enum import Enum

class ParticipantAction(Enum):
    HIT = 1
    STAND = 2
    DOUBLE = 3

class ActionStrategy(ABC):
    @abstractmethod
    def execute(self, participant, deck):
        """Executa a ação para o participante usando o deck fornecido."""
        pass

class HitStrategy(ActionStrategy):
    def execute(self, participant, deck):
        card = deck.get_card()
        participant.update_hand(card)
        participant.update_points(card.point)
        if participant.get_points() > 21:
            print(f"++{participant.name}++: Busted with: {participant.get_points()}")
            
class StandStrategy(ActionStrategy):
    def execute(self, participant, deck):
        print(f"++{participant.name}++ has decided to stand.")

class DoubleStrategy(ActionStrategy):
    def execute(self, participant, deck):
        participant.current_bet *= 2  # Assuming you have a method to double the bet.
        self.hit_strategy.execute(participant, deck)
        print(f"++{participant.name}++ has doubled down.")


class Participant:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.hand_cards: List[Card] = []
        self.points = 0
        self.balance = balance
        self.current_bet = 0
        self.dealer = False #Default
        self.current_action = ''
        self.action_strategies = {
            ParticipantAction.HIT: HitStrategy(),
            ParticipantAction.STAND: StandStrategy(),
            ParticipantAction.DOUBLE: DoubleStrategy()
        }
    def get_points(self):
        return self.points
    
    def update_points(self, new_point):
       self.points = self.points + new_point
    
    def get_hand(self):
        return self.hand_cards
    
    def update_hand(self, card: Card):
        self.hand_cards.append(card)
        
    def update_balance(self, current_bet: int):
        self.balance = self.balance - current_bet
    
    @property
    def is_dealer(self):
        return self.dealer
    
    def execute_action(self, action: ParticipantAction, deck):
        strategy = self.action_strategies.get(action)
        if strategy:
            strategy.execute(self, deck)
        else:
            raise ValueError("Invalid action")
