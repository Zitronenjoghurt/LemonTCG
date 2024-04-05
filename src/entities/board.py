from pydantic import BaseModel, computed_field
from src.constants.event_type import EventType
from src.entities.coordinates import Coordinates
from src.entities.tile import Tile
from src.context import Context

CONTEXT = Context.get_instance()

class Board(BaseModel):
    height: int = CONTEXT.config.default_board_height
    width: int = CONTEXT.config.default_board_width
    tiles: list[Tile] = []

    @computed_field 
    @property
    def tile_count(self) -> int:
        return self.height * self.width