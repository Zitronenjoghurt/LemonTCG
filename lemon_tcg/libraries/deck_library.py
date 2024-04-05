from lemon_tcg.entities.deck import Deck
from lemon_tcg.utils.file_operations import construct_path, files_in_directory

DECKS_DIRECTORY_PATH = construct_path("lemon_tcg/data/save/decks")

class DeckLibrary():
    _instance = None

    def __init__(self) -> None:
        if DeckLibrary._instance is not None:
            raise RuntimeError("Tried to initialize multiple instances of DeckLibrary.")
        files = files_in_directory(path=DECKS_DIRECTORY_PATH, suffix=".json")
        self.decks: dict[str, Deck] = {}
        for file in files:
            file_name = file[:-5]
            try:
                deck = Deck.load_state(id=file_name)
            except Exception as e:
                raise RuntimeError(f"An error occured while loading deck '{file_name}': {e}")
            self.decks[deck.id] = deck
        
    @staticmethod
    def get_instance() -> 'DeckLibrary':
        if DeckLibrary._instance is None:
            DeckLibrary._instance = DeckLibrary()
        return DeckLibrary._instance