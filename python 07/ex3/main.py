from ex3.FantasyCardFactory import FantasyCardFactory


def main():
    card_factory = FantasyCardFactory()
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")
    availbe_types = {}
    print("Available types:", card_factory.registers)


if __name__ == "__main__":
    main()
