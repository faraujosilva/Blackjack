import time
import sys
from deck import Deck
from participant import Participant, ParticipantAction
from typing import List

class NoMoney(BaseException):
    def __init__(self, message: str):
        super().__init__(message)

class Engine:
    def __init__(self, participants: List[Participant], deck: Deck):
        self.participants = participants
        self.deck = deck
        self.round = 1
        self.dealer = self._get_dealer()

    def _get_dealer(self):
        for p in self.participants:
            if self.is_dealer(p):
                return p

    def _get_player_by_name(self, name):
        for p in self.participants:
            if p.name == name:
                return p

    def _remove_player(self, name):
        p = self._get_player_by_name(name)
        if p.name == name:
            print(f'{p.name} out for this round')
            self.participants.remove(p)

    def _set_player_bet(self, name: str, bet: int):
        p = self._get_player_by_name(name)
        return p.update_balance(bet)

    def is_dealer(self, p: Participant):
        return p.is_dealer
    
    def update_round(self):
        self.round += 1

    def _player_action(self, p: Participant):
        action_menu = "\n".join([f"{action.value} - {action.name}" for action in ParticipantAction])
        try:
            action = int(input(f"++{p.name}++: Choose an action:\n{action_menu}\n"))
            participant_action = ParticipantAction(action)
            p.execute_action(participant_action, self.deck)
        except ValueError:
            print("Invalid action. Please try again.")
        
    def _get_bets(self):
        participants = self.participants.copy()
        for participant in participants:
            if self.is_dealer(participant):
                continue
            bet = input(f'Put your bet: {participant.name}: ')
            while True:
                if isinstance(bet, str):
                    bet = int(bet)
                if bet == 0:
                    self._remove_player(participant.name)
                    break
                elif bet > participant.balance:
                    bet = input(f"Sorry, bet is out fo your budget, put another value lower than: {participant.balance}: ")
                    bet = int(bet)
                else:
                    self._set_player_bet(participant.name, bet)
                    break
        if len(self.participants) == 1:
            print(f"Empty bets, waiting for new players!")
            sys.exit()
        else:
            print(f'Bets done for: {", ".join([participant.name for participant in self.participants if not self.is_dealer(participant)])}, starting game')

    def _set_card_points(self):
        return self.deck.get_card_points()

    def start(self):
        if self.round == 1:
            self.deck.new_deck()
            self._set_card_points()
            self._get_bets()
            self.deck.shuffle_deck()

        self.participants.remove(self.dealer)
        game = 1
        while game == 1:
            print(f'Round: {self.round}')
            for p in self.participants:
                self.dealer.deal(self.deck, self.round, p)
                print(f"++{p.name}++: Current Points: {p.get_points()}")
                self._player_action(p)
            self.update_round()
