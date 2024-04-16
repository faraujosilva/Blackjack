from abc import ABC, abstractmethod
from enum import Enum
from deck import Card
from typing import List

class PlayerAction(Enum):
    HIT = 1
    DOUBLE = 2
    STAND = 3
    SPLIT = 4

class ActionsStrategy(ABC):
    @abstractmethod
    def do_action(self, deck: List[Card]) -> Card: pass
    
class HitStrategy(ActionsStrategy):
    def do_action(self, player, deck: List[Card]) -> Card:
        p_card = deck[0]
        if player.dealer_rule:
            print(f"Second card is get by dealer hidden")
        else:
            print(f"Card: {p_card.name} of {p_card.suit} given to {player.name}")
        player.set_player_action(PlayerAction.HIT)
        return p_card
    
class DoubleStrategy(ActionsStrategy):
    def do_action(self, player, deck: List[Card]) -> Card:
        player.set_player_action(PlayerAction.DOUBLE)
        pass
    
class StandStrategy(ActionsStrategy):
    def do_action(self, player, deck: List[Card]) -> Card:
        player.set_player_action(PlayerAction.STAND)
        print(f"Player {player.name} decided to stand")
    
class SplitStrategy(ActionsStrategy):
    def do_action(self, player, deck: List[Card]) -> Card:
        if not player.split_rule:
            print(f"You do not have two card to make split")
        player.set_player_action(PlayerAction.SPLIT)

action_map = {
    PlayerAction.HIT: HitStrategy(),
    PlayerAction.DOUBLE: DoubleStrategy(),
    PlayerAction.STAND: StandStrategy(),
    PlayerAction.SPLIT: SplitStrategy()
}

class Actions:
    def get_action(self, action: PlayerAction) -> ActionsStrategy:
        return action_map.get(action)
