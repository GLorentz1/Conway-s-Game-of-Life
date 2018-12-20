import pygame as pyg
import cell
import random
class Grid:
    """A Grid is made of multiple cells, it represents the current state of all cells"""
    def __init__(self, width = 1000, height = 1000, cellSize = 20):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.numCellsHorizontal = int(width / cellSize)
        self.numCellsVertical = int(height / cellSize)
        self.data = []

        for i in range(self.numCellsVertical):
            self.data.append([])
            for j in range(self.numCellsHorizontal):
                if i == 0:
                    self.data[i].append(cell.Cell(state=1))
                elif j == 0:
                    self.data[i].append(cell.Cell(state=1))
                elif i == self.numCellsVertical - 1:
                    self.data[i].append(cell.Cell(state=1))
                elif j == self.numCellsHorizontal - 1:
                    self.data[i].append(cell.Cell(state=1))
                elif (i == self.numCellsVertical - 1 and j == self.numCellsHorizontal - 1):
                    self.data[i].append(cell.Cell(state=0))
                else:
                    self.data[i].append(cell.Cell(state=0))

    def drawGrid(self, window):
        y = - 1 * self.cellSize
        for i in range(self.numCellsVertical):
            y += self.cellSize
            x = 0
            for j in range(self.numCellsHorizontal):
                self.data[i][j].drawCell(window, x, y, self.cellSize)
                x += self.cellSize
        pyg.display.update()

    def nextGrid(self, newGrid):
        for i in range(self.numCellsVertical):
            for j in range(self.numCellsHorizontal):
                newGrid.data[i][j].state = (self.data[i][j]).nextState(self.countNeighbors(j,i))

    def isTopLeftCorner(self, pos_x, pos_y):
        if pos_x == 0:
            if pos_y == 0:
                return True
        else:
            return False

    def isTopRightCorner(self, pos_x, pos_y):
        if pos_x == self.numCellsHorizontal - 1:
            if pos_y == 0:
                return True
        else:
            return False

    def isBottomLeftCorner(self, pos_x, pos_y):
        if pos_x == 0:
            if pos_y == self.numCellsVertical - 1:
                return True
        else:
            return False

    def isBottomRightCorner(self, pos_x, pos_y):
        if pos_x == self.numCellsHorizontal - 1:
            if pos_y == self.numCellsVertical - 1:
                return True
        else:
            return False

    def isTop(self, pos_x, pos_y):
        if pos_y ==0:
            if pos_x > 0 and pos_x < self.numCellsHorizontal - 1:
                return True
        else:
            return False

    def isLeft(self, pos_x, pos_y):
        if pos_x ==0:
            if pos_y > 0 and pos_y < self.numCellsVertical - 1:
                return True
        else:
            return False

    def isRight(self, pos_x, pos_y):
        if pos_x == self.numCellsHorizontal - 1:
            if pos_y > 0 and pos_y < self.numCellsVertical - 1:
                return True
        else:
            return False

    def isBottom(self, pos_x, pos_y):
        if pos_y == self.numCellsVertical - 1:
            if pos_x > 0 and pos_x < self.numCellsHorizontal - 1:
                return True
        else:
            return False

    def countNeighbors(self, pos_x, pos_y):
        countNeighbor = 0
        if self.isTopLeftCorner(pos_x, pos_y):
            if (self.data[pos_y][pos_x + 1]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y + 1][pos_x]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y + 1][pos_x + 1]).state == 1:
                countNeighbor += 1
        elif self.isTopRightCorner(pos_x, pos_y):
            if (self.data[pos_y][pos_x - 1]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y + 1][pos_x - 1]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y + 1][pos_x]).state == 1:
                countNeighbor += 1
        elif self.isBottomLeftCorner(pos_x, pos_y):
            if (self.data[pos_y - 1][pos_x]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y - 1][pos_x + 1]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y][pos_x + 1]).state == 1:
                countNeighbor += 1
        elif self.isBottomRightCorner(pos_x, pos_y):
            if (self.data[pos_y - 1][pos_x - 1]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y - 1][pos_x]).state == 1:
                countNeighbor += 1
            if (self.data[pos_y][pos_x - 1]).state == 1:
                countNeighbor += 1
        elif self.isTop(pos_x, pos_y):
            for i in range (0, 2):
                for j in range(-1, 2):
                    check_x = pos_x + j
                    check_y = pos_y + i

                    if not (i == 0 and j == 0):
                        if self.data[check_y][check_x].state == 1:
                            countNeighbor += 1
        elif self.isLeft(pos_x, pos_y):
            for i in range(-1, 2):
                for j in range(0, 2):
                    check_x = pos_x + j
                    check_y = pos_y + i

                    if not (i == 0 and j == 0):
                        if self.data[check_y][check_x].state == 1:
                            countNeighbor += 1
        elif self.isBottom(pos_x, pos_y):
            for i in range(-1, 1):
                for j in range(-1, 2):
                    check_x = pos_x + j
                    check_y = pos_y + i

                    if not (i == 0 and j == 0):
                        if self.data[check_y][check_x].state == 1:
                            countNeighbor += 1
        elif self.isRight(pos_x, pos_y):
            for i in range(-1, 2):
                for j in range(-1, 1):
                    check_x = pos_x + j
                    check_y = pos_y + i

                    if not (i == 0 and j == 0):
                        if self.data[check_y][check_x].state == 1:
                            countNeighbor += 1
        else:
           # print("Pos x = %d e Pos y = %d" % (pos_x, pos_y))
            for i in range(-1, 2):
                for j in range(-1, 2):
                    check_x = pos_x + j
                    check_y = pos_y + i
                   # print("Check x = %d e Check y = %d" % (check_x, check_y))
                    if not (i == 0 and j == 0):
                        if self.data[check_y][check_x].state == 1:
                            countNeighbor += 1
        return countNeighbor

    def updateCellStatus(self, x, y, window):
        grid_x = (x // self.cellSize)
        grid_y = (y // self.cellSize)

        if self.data[grid_y][grid_x].state == 1:
            self.data[grid_y][grid_x].state = 0
        else:
            self.data[grid_y][grid_x].state = 1
        self.data[grid_y][grid_x].drawCell(window, grid_x * self.cellSize, grid_y * self.cellSize, self.cellSize)
        pyg.display.update()

    def copyGrid(self, newGrid):
        for i in range(self.numCellsVertical):
            for j in range(self.numCellsHorizontal):
                newGrid.data[j][i].state = self.data[j][i].state