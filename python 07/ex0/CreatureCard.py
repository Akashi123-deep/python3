from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.__attack,
            "health": self.__health,
        }

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self) -> dict:
        return {
            "attacker": self.name,
            "target": "Goblin Warrior",
            "damage_dealt": self.__attack,
            "combat_resolved": True,
        }

    def get_attack(self):
        return self.__attack

    def set_attack(self, attack: int) -> None:
        if attack > 0:
            self.__attack = attack
        else:
            self.__attack = 0

    def set_health(self, health: int) -> None:
        if health > 0:
            self.__health = health
        else:
            self.__health = 0

    def get_health(self):
        return self.__health

    def is_playable(self, available_mana: int) -> bool:
        if available_mana < self.cost:
            return False
        return True
