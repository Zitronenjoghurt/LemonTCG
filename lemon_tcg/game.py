from lemon_tcg.entities.game_state import GameState
from lemon_tcg.libraries.game_state_library import GameStateLibrary

GAME_STATES = GameStateLibrary.get_instance()

class Game():
    def __init__(self, state: GameState) -> None:
        self.state = state

    @staticmethod
    def load_from_game_id(game_id: str) -> 'Game':
        game_state = GAME_STATES.get_by_id(id=game_id)
        if not isinstance(game_state, GameState):
            raise RuntimeError(f"Invalid game id '{game_id}'.")
        return Game(state=game_state)
    
    def save(self) -> None:
        self.state.save_state()