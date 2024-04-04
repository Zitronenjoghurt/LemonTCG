from pydantic import BaseModel
from src.entities.localized_values import LocalizedValue
from src.utils.file_operations import construct_path, file_exists, file_to_string

CARD_FILE_PATH = construct_path("src/data/cards/{id}.json")

class Card(BaseModel):
    id: str
    name: LocalizedValue
    description: LocalizedValue

    @staticmethod
    def load_from_id(id: str) -> 'Card':
        id = id.lower()
        file_path = CARD_FILE_PATH.format(id=id)
        if not file_exists(file_path=file_path):
            raise RuntimeError(f"Card with id '{id}' does not exist.")
        json_data = file_to_string(file_path=file_path)
        return Card.model_validate_json(json_data)