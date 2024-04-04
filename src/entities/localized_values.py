from typing import Optional
from pydantic import BaseModel

class LocalizedValues(BaseModel):
    en: Optional[str] = None
    de: Optional[str] = None
    fr: Optional[str] = None