from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main():
    elite_card = EliteCard("Arcane Warrior", 6, "Epic")
    test1 = [method for method in dir(Card) if not method.startswith("_")]
    test2 = [
        method for method in dir(Combatable) if not method.startswith("_")
    ]
    test3 = [method for method in dir(Magical) if not method.startswith("_")]
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    print("- Card:", test1)
    print("- Combatable:", test2)
    print("- Magical:", test3)
    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")
    print("Attack result:", elite_card.attack("Enemy"))
    print("Defense result:", elite_card.defend(2))
    print("\nMagic phase:")
    print(
        "Spell cast:", elite_card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    )
    print("Mana channe:", elite_card.channel_mana(7))
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
