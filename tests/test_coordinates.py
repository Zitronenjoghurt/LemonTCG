from lemon_tcg.entities.coordinates import Coordinates

BOARD_WIDTH = 5
BOARD_HEIGHT = 6

def test_user_to_global():
    TEST_VALUES = [
        (Coordinates(x=0, y=0), [Coordinates(x=0, y=3), Coordinates(x=4, y=2)]),
        (Coordinates(x=1, y=0), [Coordinates(x=1, y=3), Coordinates(x=3, y=2)]),
        (Coordinates(x=0, y=1), [Coordinates(x=0, y=4), Coordinates(x=4, y=1)]),
        (Coordinates(x=1, y=1), [Coordinates(x=1, y=4), Coordinates(x=3, y=1)]),
        (Coordinates(x=2, y=2), [Coordinates(x=2, y=5), Coordinates(x=2, y=0)]),
        (Coordinates(x=3, y=1), [Coordinates(x=3, y=4), Coordinates(x=1, y=1)]),
        (Coordinates(x=4, y=2), [Coordinates(x=4, y=5), Coordinates(x=0, y=0)])
    ]

    for original, results in TEST_VALUES:
        assert original.user_to_global(user_index=0, board_height=BOARD_HEIGHT, board_width=BOARD_WIDTH) == results[0]
        assert original.user_to_global(user_index=1, board_height=BOARD_HEIGHT, board_width=BOARD_WIDTH) == results[1]

def test_global_to_user():
    TEST_VALUES_0 = [
        (Coordinates(x=0, y=3), Coordinates(x=0, y=0)),
        (Coordinates(x=1, y=3), Coordinates(x=1, y=0)),
        (Coordinates(x=0, y=4), Coordinates(x=0, y=1)),
        (Coordinates(x=1, y=4), Coordinates(x=1, y=1)),
        (Coordinates(x=2, y=5), Coordinates(x=2, y=2)),
        (Coordinates(x=3, y=4), Coordinates(x=3, y=1)),
        (Coordinates(x=4, y=5), Coordinates(x=4, y=2))
    ]

    TEST_VALUES_1 = [
        (Coordinates(x=4, y=2), Coordinates(x=0, y=0)),
        (Coordinates(x=3, y=2), Coordinates(x=1, y=0)),
        (Coordinates(x=4, y=1), Coordinates(x=0, y=1)),
        (Coordinates(x=3, y=1), Coordinates(x=1, y=1)),
        (Coordinates(x=2, y=0), Coordinates(x=2, y=2)),
        (Coordinates(x=1, y=1), Coordinates(x=3, y=1)),
        (Coordinates(x=0, y=0), Coordinates(x=4, y=2))
    ]

    for original, result in TEST_VALUES_0:
        assert original.global_to_user(user_index=0, board_height=BOARD_HEIGHT, board_width=BOARD_WIDTH) == result

    for original, result in TEST_VALUES_1:
        assert original.global_to_user(user_index=1, board_height=BOARD_HEIGHT, board_width=BOARD_WIDTH) == result

def test_global_to_tile_index():
    TEST_VALUES = [
        (0,0), (1,0), (2,0), (3,0), (4,0),
        (0,1), (1,1), (2,1), (3,1), (4,1),
        (0,2), (1,2), (2,2), (3,2), (4,2),
        (0,3), (1,3), (2,3), (3,3), (4,3),
        (0,4), (1,4), (2,4), (3,4), (4,4),
        (0,5), (1,5), (2,5), (3,5), (4,5)
    ]

    for i, xy in enumerate(TEST_VALUES):
        x, y = xy
        assert Coordinates(x=x, y=y).global_to_tile_index(board_width=BOARD_WIDTH) == i

def test_user_to_tile_index():
    TEST_VALUES = [
        (4,2), (3,2), (2,2), (1,2), (0,2),
        (4,1), (3,1), (2,1), (1,1), (0,1),
        (4,0), (3,0), (2,0), (1,0), (0,0),
        (0,0), (1,0), (2,0), (3,0), (4,0),
        (0,1), (1,1), (2,1), (3,1), (4,1),
        (0,2), (1,2), (2,2), (3,2), (4,2)
    ]

    for i, xy in enumerate(TEST_VALUES):
        x, y = xy
        user_index = 0 if i >= 15 else 1
        assert Coordinates(x=x, y=y).user_to_tile_index(user_index=user_index, board_height=BOARD_HEIGHT, board_width=BOARD_WIDTH) == i