from lemon_tcg.entities.base_save_state_entity_group import BaseSaveStateEntityGroup
from lemon_tcg.entities.board import Board
from lemon_tcg.entities.player import Player
from lemon_tcg.utils.file_operations import construct_path

class GameState(BaseSaveStateEntityGroup):
    FILE_PATH = construct_path("lemon_tcg/data/save/games/{id}.json")
    board: Board = Board()
    players: list[Player] = []