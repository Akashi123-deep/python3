from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, rating: int):
        super().__init__(name, cost, rarity)
        self._wins = 0
        self._losses = 0
        self._rating = rating

    def play(self, game_state: dict) -> dict:
        return {}

    def attack(self, target) -> dict:
        return {}

    def defend(self, incoming_damage: int) -> dict:
        return {}

    def get_combat_stats(self) -> dict:
        return {}

    def calculate_rating(self) -> int:
        return self._rating + 16

    def update_wins(self, wins: int) -> None:
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses

    def get_rank_info(self) -> dict:
        return {}

    def get_tournament_stats(self) -> dict:
        return {}
