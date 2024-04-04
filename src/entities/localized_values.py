from typing import Optional
from pydantic import BaseModel
from src.constants.language import Language
from src.context import CONFIG

class LocalizedValue(BaseModel):
    en: Optional[str] = None
    de: Optional[str] = None
    fr: Optional[str] = None

    def get_value(self, language: Optional[Language] = None) -> str:
        if isinstance(language, Language):
            language_str = language.value
        else:
            language_str = CONFIG.language.value
        return getattr(self, language_str, None) or self.en or "missing_translation"