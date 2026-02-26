from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.magic_power = 10

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
        }

    def attack(self, target) -> dict:
        return {
            "attacker": "Arcane Warrior",
            "target": target,
            "damage": 5,
            "combat_type": "melee",
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": "Arcane Warrior",
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": "Arcane Warrior",
            "damage_taken": incoming_damage,
            "damage_blocked": 3,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense_bonus": 3
        }

    def channel_mana(self, amount: int) -> dict:
        return {"channeled": 3, "total_mana": amount}

    def get_magic_stats(self) -> dict:
        return {
            "spell_power": self.magic_power,
            "mana_bonus": 2
        }
