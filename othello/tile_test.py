from tile import Tile


def test_constrcutor():
    tile = Tile(0, 0, "black")
    assert tile.TILE_SIZE == 90
    assert tile.GRID_SIZE == 100
    assert tile.column == 0
    assert tile.row == 0
    assert tile.color == "black"
