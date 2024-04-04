from pydantic import BaseModel, computed_field
from src.constants.event_type import EventType
from src.entities.coordinates import Coordinates
from src.entities.tile import Tile

class Board(BaseModel):
    height: int
    width: int
    tiles: list[Tile] = []

    @computed_field 
    @property
    def tile_count(self) -> int:
        return self.height * self.width