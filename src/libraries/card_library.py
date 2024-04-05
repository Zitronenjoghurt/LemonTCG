from src.entities.card import Card
from src.utils.file_operations import construct_path, files_in_directory

CARDS_DIRECTORY_PATH = construct_path("src/data/cards")

class CardLibrary():
    _instance = None

    def __init__(self) -> None:
        if CardLibrary._instance is not None:
            raise RuntimeError("Tried to initialize multiple instances of CardLibrary.")
        files = files_in_directory(path=CARDS_DIRECTORY_PATH, suffix=".json")
        self.cards: dict[str, Card] = {}
        for file in files:
            file_name = file[:-5]
            try:
                card = Card.load_from_id(id=file_name)
            except Exception as e:
                raise RuntimeError(f"An error occured while loading card '{file_name}': {e}")
            self.cards[card.id] = card
        
    @staticmethod
    def get_instance() -> 'CardLibrary':
        if CardLibrary._instance is None:
            CardLibrary._instance = CardLibrary()
        return CardLibrary._instance