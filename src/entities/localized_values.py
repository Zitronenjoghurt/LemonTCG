from typing import Optional
from pydantic import BaseModel
from src.context import CONFIG

class LocalizedValue(BaseModel):
    en: Optional[str] = None
    de: Optional[str] = None
    fr: Optional[str] = None

    def get_value(self) -> str:
        return getattr(self, CONFIG.language.value, None) or self.en or "missing_translation"