import grid
import time
import pygame as pyg
grid1 = grid.Grid()
grid_aux = grid.Grid()
WIDTH = HEIGHT = 1000
FPS = 30
pyg.init()

window = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption("Conway's Game of Life")
clock = pyg.time.Clock()

print(grid1.countNeighbors(HEIGHT//20 - 1, HEIGHT//20 - 1))

grid1.drawGrid(window)

running = True
runSim = False
while running:
    clock.tick(FPS)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
            pyg.display.quit()
            exit()
        elif event.type == pyg.MOUSEBUTTONDOWN:
            x, y = pyg.mouse.get_pos()
            grid1.updateCellStatus(x,y, window)
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                runSim = True
                while runSim:
                    grid1.nextGrid(grid_aux)
                    grid_aux.copyGrid(grid1)
                    grid1.drawGrid(window)
                    for event in pyg.event.get():
                        if event.type == pyg.KEYDOWN:
                            if event.key == pyg.K_LSHIFT:
                                grid1.resetGrid(window)
                                runSim = False
                                
                            if event.key == pyg.K_TAB:
                                running = False
                                pyg.display.quit()
                                exit()
                        elif event.type == pyg.MOUSEBUTTONDOWN:
                            x, y = pyg.mouse.get_pos()
                            grid1.updateCellStatus(x, y, window)
                    pyg.time.wait(100)
                    
            if event.key == pyg.K_LSHIFT:
                grid1.resetGrid(window)              
            if event.key == pyg.K_TAB:
                running = False
                pyg.display.quit()
                exit()