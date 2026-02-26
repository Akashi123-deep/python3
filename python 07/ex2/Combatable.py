from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        return {}

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        return {}

    @abstractmethod
    def get_combat_stats(self) -> dict:
        return {}
