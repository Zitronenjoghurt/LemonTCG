from pydantic import BaseModel

class Player(BaseModel):
    index: int
    display_name: str