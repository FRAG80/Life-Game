from project import decide_next_whole, drawGrid, cell_on, arr_conv1
import pygame

pygame.init()
display = pygame.display.set_mode((100, 100))

def test_decide_next_whole():
    assert decide_next_whole([[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,0]]
    assert decide_next_whole([[0,1,0,0]],[[1,1,1,1]]) == [[1,1,1,0]]

def test_drawGrid():
    global display
    assert drawGrid(10, 10, display) == None

def test_cell_on():
    global display
    assert cell_on(0, 0, 10, display) == "dummy output"

def test_arr_conv1():
    assert arr_conv1([["0","0","0","0"]]) == [[0,0,0,0]]