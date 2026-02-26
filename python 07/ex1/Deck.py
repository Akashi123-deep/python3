import random
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for item in self.cards:
            if item.name == card_name:
                self.cards.remove(item)
        return True

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "creatures": len(
                [item for item in self.cards if isinstance(item, CreatureCard)]
            ),
            "spells": len(
                [item for item in self.cards if isinstance(item, SpellCard)]
            ),
            "artifacts": len(
                [item for item in self.cards if isinstance(item, ArtifactCard)]
            ),
            "avg_cost": round(
                sum([item.cost for item in self.cards]) / len(self.cards), 2
            ),
        }
