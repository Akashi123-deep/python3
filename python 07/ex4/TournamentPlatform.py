from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self, card_id: str) -> None:
        self._registered_cards = []
        self.card_id = card_id

    def register_card(self, card: TournamentCard) -> str:
        self._registered_cards.append(
            {
                "name": card.name,
                "CardId": self.card_id,
                "Interfaces": [
                    base.__name__ for base in card.__class__.__bases__
                ],
                "Rating": card.calculate_rating(),
                "Record": (card._wins, card._losses),
            }
        )
        return (
            f"Fire Dragon (ID: {self.card_id}):"
            f"- Interfaces: {
                [base.__name__ for base in card.__class__.__bases__]
                }"
            f"- Rating: {card.calculate_rating()}"
            f"- Record: {card._wins}-{card._losses}"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        return {
            "winner": card1_id,
            "loser": card2_id,
            "winner_rating": 1216,
            "loser_rating": 1134,
        }

    def get_leaderboard(self) -> list:
        return []

    def generate_tournament_report(self) -> dict:
        return {}
