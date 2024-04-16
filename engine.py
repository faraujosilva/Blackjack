from participant import Participant
from actions import PlayerAction
from deck import Deck
from typing import List

class Engine:
    def __init__(self, players: List[Participant], dealer: Participant, deck: Deck):
        self.players = players
        self.deck = deck
        self.winners = []
        self.current_round = 1
        if self.current_round == 1:
            print('Bets are closed, starting game')
        self.dealer = dealer
    
    @property
    def current_players(self):
        return len(self.players)      
    
    @property
    def stand_players(self):
        return sum(1 for player in self.players if player.current_action == PlayerAction.STAND)
    
    def _update_round(self):
        self.current_round += 1

    def _remove_player(self, p):
        self.players.remove(p)
        
    def _update_game_data(self, p: Participant, card):
        p.update_points(card.point)
        p.udpate_hand(card)
        self.deck.update(card)

    def _check_winners(self):
        for player in self.players:
            if not player.bust:
                if self.dealer.points < player.points or self.dealer.points == player.points:
                    self.winners.append(player.name)
        return self.winners

    def _player_action(self, deck):
        print(f"Dealer points: {self.dealer.points}")
        for player in self.players:
            if player.bust:
                self._remove_player(player)
                print(f"Player: {player.name} busted with {str(player.points)} points")
            action = input(f"Choose your action {player.name}:\n {[str(act.value) + ' - ' + act.name for act in PlayerAction]}: ")
            action = int(action)
            round_card = player.do_action(PlayerAction(action), deck)
            if PlayerAction(action) == PlayerAction.HIT:
                self._update_game_data(player, round_card)
                if player.bust:
                    self._remove_player(player)
                    print(f"Player: {player.name} busted with {str(player.points)} points")
                    
                if player.bjack_rule:
                    self.winners.append(player.name)
                    self._remove_player(player)

    def _first_round(self, deck):
        i = 2 if self.current_round == 1 else 0
        for _ in range(i):
            for player in self.players:
                round_card = player.do_action(PlayerAction.HIT, deck)
                self._update_game_data(player, round_card)
            dealer_card = self.dealer.do_action(PlayerAction.HIT, deck)
            self._update_game_data(self.dealer, dealer_card)
        self._update_round()
        
        
    def run(self):
        deck = self.deck.new()
        
        self._first_round(deck)
        
        while True:
            self._player_action(deck)
            if self.current_players == self.stand_players:
                if not self.dealer.dealer_max_point and self.dealer.points <= 21:
                    dealer_card = self.dealer.do_action(PlayerAction.HIT, deck)
                    self._update_game_data(self.dealer, dealer_card)
                    self._update_round()

                print(f'Dealer reveal a hidden card: {self.dealer.hand[1].name} of {self.dealer.hand[1].suit}')
                winners = self._check_winners()
                if not winners:
                    print('Dealer Winner')
                else:
                    for p in winners:
                        print(f"Player: {p} wins!")
                break
        print(self.dealer.hand)
