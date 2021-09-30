class Tile:
    """A tile"""
    def __init__(self, column, row, color):
        """
        :Int column: the column of the tile
        :Int row: the row of the tile
        :Sring color: the color of the tile (Assuming only "black" or "white")
        Tile constuctor
        """
        self.TILE_SIZE = 90
        self.GRID_SIZE = 100
        self.column = column
        self.row = row
        self.color = color

    def display(self):
        """Draws the tile"""
        if (self.color == "white"):
            fill(255, 255, 255)
        if (self.color == "black"):
            fill(0, 0, 0)
        ellipse(self.column * self.GRID_SIZE + self.GRID_SIZE/2,
                self.row * self.GRID_SIZE + self.GRID_SIZE/2,
                self.TILE_SIZE, self.TILE_SIZE)

    def __str__(self):
        return self.color

    def __repr__(self):
        return str(self)
