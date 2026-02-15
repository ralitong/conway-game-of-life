import pytest
from main import Game
from main import Cell


def test_there_should_be_a_game_class():
    game = Game()


def test_there_should_be_a_grid_in_the_game():
    game = Game()
    assert hasattr(game, "grid")


def test_the_game_should_accept_grid_size():
    size = 20
    game = Game(size=20)
    assert game.size == size


def test_there_should_be_a_cell_class():
    cell = Cell()


def test_cell_should_have_alive_property():
    cell = Cell()
    assert hasattr(cell, "alive")


def test_cell_alive_property_should_be_false_by_default():
    cell = Cell()
    assert cell.alive == False


def test_cell_should_have_an_row_property():
    cell = Cell()
    assert hasattr(cell, "row")


def test_cell_row_should_be_parameterized():
    cell = Cell(row=1)
    assert cell.row == 1


def test_cell_row_default_should_be_zero():
    cell = Cell()
    assert cell.row == 0


def test_cell_should_have_a_column_property():
    cell = Cell()
    assert hasattr(cell, "column")


def test_cell_column_should_be_parameterized():
    cell = Cell(column=1)
    assert cell.column == 1


def test_cell_column_default_should_be_zero():
    cell = Cell()
    assert cell.column == 0


def test_cell_should_return_the_coordinates_of_the_left_neighbor_coordinates():
    cell_row = 5
    cell_column = 5
    cell = Cell(row=cell_row, column=cell_column)
    neighbor_row, neighbor_column = cell.get_left_neighbor_coordinates()
    assert neighbor_row == cell_row - 1
    assert neighbor_column == cell_column

def test_cell_should_return_the_coordinates_of_the_upper_left_neighbor_coordinates():
    cell_row = 5
    cell_column = 5
    cell = Cell(row=cell_row, column=cell_column)
    neighbor_row, neighbor_column = cell.get_upper_left_neighbor_coordinates()
    assert neighbor_row == cell_row - 1
    assert neighbor_column == cell_column + 1

def test_cell_should_return_the_coordinates_of_the_up_neighbor_coordinates():
    cell_row = 5
    cell_column = 5
    cell = Cell(row=cell_row, column=cell_column)
    neighbor_row, neighbor_column = cell.get_up_neighbor_coordinates()
    assert neighbor_row == cell_row
    assert neighbor_column == cell_column + 1

def test_cell_should_return_the_coordinates_of_the_right_neighbor_coordinates():
    cell_row = 5
    cell_column = 5
    cell = Cell(row=cell_row, column=cell_column)
    neighbor_row, neighbor_column = cell.get_right_neighbor_coordinates()
    assert neighbor_row == cell_row + 1
    assert neighbor_column == cell_column
    


@pytest.mark.skip(reason="Not ready")
def test_cell_should_have_get_neighbors_function():
    pass


@pytest.mark.skip(reason="Not ready")
def test_cell_should_be_dead_if_it_has_less_than_two_neighbors():
    pass
