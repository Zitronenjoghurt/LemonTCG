import pytest
from lemon_tcg.entities.game_state import GameState
from lemon_tcg.event.events.game_state import game_state_tick

@pytest.fixture
def game_state():
    return GameState.create_new(players=[])

@pytest.mark.asyncio
async def test_game_state_tick(game_state: GameState):
    assert game_state.event_tick == 0
    await game_state_tick(game_state_id=game_state.id)
    assert game_state.event_tick == 1