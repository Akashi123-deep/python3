from ex0.CreatureCard import CreatureCard


def main():
    available_mana = 6
    insufficient_mana = 3
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(creature.get_card_info())
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
    print("Playable:", creature.is_playable(available_mana))
    print("Play result", creature.play(creature.get_card_info()))
    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target())
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", creature.is_playable(insufficient_mana))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
