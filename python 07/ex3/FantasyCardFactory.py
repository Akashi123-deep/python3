from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class FantasyCardFactory:
    def __init__(self) -> None:
        self.registers = {
            "creature": [
                CreatureCard("dragon", 5, "Legendary", 7, 5),
                CreatureCard("goblin", 5, "Legendary", 7, 5),
            ],
            "artifact": [
                ArtifactCard(
                    "mana_ring", 2, "Rare", 3, "Permanent: +1 mana per turn"
                )
            ],
            "spell": [
                SpellCard(
                    "fireball", 3, "Common", "Deal 3 damage to target"
                )
            ],
        }

    def Create_creature(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> CreatureCard:
        return CreatureCard(name, cost, rarity, attack, health)

    def create_artifact(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> ArtifactCard:
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_spell(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> SpellCard:
        return SpellCard(name, cost, rarity, effect_type)

    def register_card_type(self, type_name: str, card: Card) -> None:
        if type_name not in self.registers:
            self.registers[type_name] = []
        self.registers[type_name].append(card)
