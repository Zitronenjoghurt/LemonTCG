from typing import Optional
from src.entities.game_state import GameState
from src.utils.file_operations import construct_path, files_in_directory

GAME_STATE_DIRECTORY_PATH = construct_path("src/data/save/games")

class GameStateLibrary():
    _instance = None

    def __init__(self) -> None:
        if GameStateLibrary._instance is not None:
            raise RuntimeError("Tried to initialize multiple instances of GameStateLibrary.")
        files = files_in_directory(path=GAME_STATE_DIRECTORY_PATH, suffix=".json")
        self.game_states: dict[str, GameState] = {}
        for file in files:
            file_name = file[:-5]
            try:
                game_state = GameState.load_state(id=file_name)
            except Exception as e:
                raise RuntimeError(f"An error occured while loading deck '{file_name}': {e}")
            self.game_states[game_state.id] = game_state
        
    @staticmethod
    def get_instance() -> 'GameStateLibrary':
        if GameStateLibrary._instance is None:
            GameStateLibrary._instance = GameStateLibrary()
        return GameStateLibrary._instance
    
    def get_by_id(self, id: str) -> Optional[GameState]:
        return self.game_states.get(id, None)