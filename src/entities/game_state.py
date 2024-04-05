from src.entities.base_save_state_entity_group import BaseSaveStateEntityGroup
from src.entities.board import Board
from src.entities.player import Player
from src.utils.file_operations import construct_path

class GameState(BaseSaveStateEntityGroup):
    FILE_PATH = construct_path("src/data/save/games/{id}.json")
    board: Board = Board()
    players: list[Player] = []