from participant import Participant
from typing import List
from deck import Deck

class Dealer(Participant):
    def __init__(self, name: str, balance: int):
        super().__init__(name, balance)
        self.dealer = True

    def deal(self, deck: Deck, current_round: int, player: Participant, action = None):        
        if current_round == 1:
            if len(self.hand_cards) == 0:
                print(f"++{self.name}++: Get first card hidden")
                dealer_card = deck.get_card()
                self.update_hand(dealer_card)
                self.update_points(dealer_card.point)
            
            player_card  = deck.get_card()
            print(f"++{player.name}++: Get {player_card.name} of {player_card.suit}")
            player.update_hand(player.update_hand(player_card))
            player.update_points(player_card.point)
            return
        else:
            dealer_card = deck.get_card()
            self.update_hand(dealer_card)
            self.update_points(dealer_card.point)
            print(f"++{self.name}++: Get {dealer_card.name} of {dealer_card.suit}")
            