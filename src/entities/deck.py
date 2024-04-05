from src.entities.base_save_state_entity_group import BaseSaveStateEntityGroup
from src.utils.file_operations import construct_path

class Deck(BaseSaveStateEntityGroup):
    FILE_PATH = construct_path("src/data/save/decks/{id}.json")
    name: str = "No Name"
    cards: dict[str, int] = {}