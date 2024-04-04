from pytest import fixture
from src.entities.board import Board

def test_initialization():
    board = Board(height=5, width=5)
    assert board.tile_count == 25