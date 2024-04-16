from deck import Card
from rules import GameRules
from typing import List
from deck import Deck
from actions import Actions, PlayerAction

class Participant(GameRules):
    def __init__(self, name: str, action: Actions):
        self.dealer = False
        self.name = name
        self.hand: List[Card] = []
        self.points = 0
        self.action = action
        self.current_action = None
        super().__init__()
        
    def get_hand(self) -> List[Card]:
        return self.hand
    
    def get_points(self):
        return self.points
    
    def update_points(self, point: int):
        self.points += point        

    def udpate_hand(self, card: Card):
        self.hand.append(card)
        
    def do_action(self, action: PlayerAction, deck: Deck):
        action = self.action.get_action(action)
        return action.do_action(self, deck)
    
    def set_player_action(self, action: PlayerAction):
        self.current_action = action
        

        # if all(player.current_action == PlayerAction.STAND for player in self.players):
        #     print('All players deceided to stand')
        #     while True:
        #         if self.dealer.dealer_max_point:
        #             winners = self._check_winners()
        #             if not winners:
        #                 print(f"Sorry, this game is mine!!! HAHAHAH\n\n{[player.name + ' - Score: ' + str(player.points) for player in self.players if player.name not in winners]}")
        #                 for p in self.players:
        #                     self._remove_player(p)
        #                 break
        #         dealer_card = self.dealer.do_action(PlayerAction.HIT, deck)
        #         self._update_game_data(self.dealer, dealer_card)
        #         if self.dealer.bust:
        #             winners = self._check_winners()
        #             print(winners)
        #             if not winners:
        #                 print(f"Sorry, this game is mine!!! HAHAHAH\n\n{[player.name + ' - Score: ' + str(player.points) for player in self.players if player.name not in winners]}")
        #                 for p in self.players:
        #                     self._remove_player(p)
        #             break

        # self._update_round()