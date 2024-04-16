from deck import Cards

class GameRules:
    @property
    def ace_rule(self):
        if Cards.ACE in self.hand and self.points >=21:
            for card in self.hand:
                if card.name == Cards.ACE:
                    self.update_points(-card.point)
                    print(f"ACE rule applied")

    @property
    def split_rule(self):
        seen_names = set()
        duplicates = set()
        for card in self.hand:
            if card.name in seen_names:
                duplicates.add(card.name)
            seen_names.add(card.name)
        return True if len(duplicates) == 2 else False

    @property
    def bjack_rule(self):
        return list(filter(lambda card: card.name == Cards.ACE, self.hand))

    @property
    def dealer_rule(self) -> bool:
        return (self.dealer and len(self.hand) == 1)

    @property
    def bust(self) -> bool:
        return self.points > 21
    
    @property
    def dealer_max_point(self) -> bool:
        return self.points == 17
