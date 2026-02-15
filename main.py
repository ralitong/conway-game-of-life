class Cell:
    def __init__(self, row=0, column=0):
        self.alive = False
        self.row = row
        self.column = column

    def get_left_neighbor_coordinates(self):
        return self.row - 1, self.column

    def get_upper_left_neighbor_coordinates(self):
        return self.row - 1, self.column + 1

    def get_up_neighbor_coordinates(self):
        return self.row, self.column + 1

    def get_right_neighbor_coordinates(self):
        return self.row + 1, self.column

class Game:
    def __init__(self, size=10):
        self.size = size
        self.grid = []
