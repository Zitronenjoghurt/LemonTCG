from src.constants.language import Language
from src.entities.base_save_state_entity import BaseSaveStateEntity
from src.utils.file_operations import construct_path

class Config(BaseSaveStateEntity):
    FILE_PATH = construct_path("src/data/save/config.json")
    language: Language = Language.ENGLISH

    def set_language(self, language: Language) -> None:
        if not isinstance(language, Language):
            raise RuntimeError(f"Tried to change config language, but given language is invalid.")
        self.language = language