import pygame as pyg
import random

class Cell:
    """A cell represents one element of the grid, it can be either dead or alive, and has x and y coordinates"""
    def __init__(self, state = 0):
        """Cretes a cell with given state (0 - Dead / 1 - Alive)"""
        self.state = state

    def drawCell(self, window, x , y, size):
        if self.state == 1:
            color = (random.randint(0,255),255,0)
        else:
            color = (0,0,0)

        window.fill((255,255,255), [x, y, size, size])
        window.fill(color, [x + 1, y + 1, size - 2, size - 2])

    def nextState(self, countNeighbor):
        """Determines cell's next state based on how many neighbors the cell has"""
        newState = 0
        if self.state == 1:
            if countNeighbor < 2:
                newState = 0
            elif countNeighbor < 4:
                newState = 1
            else:
                newState = 0
        else:
            if countNeighbor == 3:
                newState = 1
        return newState
        
    def setState(self, newState):
        self.state = newState