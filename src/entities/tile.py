from pydantic import BaseModel
from src.constants.tile_state import TileState

class Tile(BaseModel):
    state: TileState = TileState.VOID