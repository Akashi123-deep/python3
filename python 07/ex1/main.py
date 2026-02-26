from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main():
    deck_manager = Deck()
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    crystal = ArtifactCard(
        "Mana Crystal", 2, "Rare", 3, "Permanent: +1 mana per turn"
    )
    deck_manager.add_card(dragon)
    deck_manager.add_card(crystal)
    deck_manager.add_card(bolt)
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    print("Deck stats:", deck_manager.get_deck_stats())
    print("\nDrawing and playing cards:")
    for _ in range(len(deck_manager.cards)):
        card = deck_manager.draw_card()
        card_type = card.__class__.__name__.replace("Card", "")
        print(f"\nDrew: {card.name} ({card_type})")
        print("Play result:", card.play({}))
    print(
        "\nPolymorphism in action: Same interface," "different card behaviors!"
    )


if __name__ == "__main__":
    main()
