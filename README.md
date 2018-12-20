Conway's Game of Life

A python implementation of The GoL. The Game of Life is a cellular automata. It has a collection of cells, each being alive, or dead.
The cells reproduce/die according to four rules:
- A live cell with less than 2 live neighbors dies by underpopulation
- A live cell with 2 or 3 live neighbors lives on
- A live cell with more than 3 live neighbors dies by overpopulation
- A dead cell with exactly 3 neighbors will become alive, by reproduction

This program contains 3 files: grid.py, cell.py and __main__.py. It's worth noting that you'll need pygame to run this code.
- cell.py implements the class that represents de cells, it deals with changing it's state and drawing it to the screen
- grid.py implements the grid, essentially a collection of cells. It deals with counting each cell's neighbors.
- __main__.py is the actual program, it deals with pygame's events (like key/mouse pressing) and the game loop, which is calling grid.py functions repeatedly

How to use:
- Have the 3 files in the same directory.
- Make sure you have pygame installed.
- Run __main__.py
- A screen will come up, filled with black rectangles (which means that the cell in that position is dead)
- To make a cell come to life, click inside the desired rectangle. It should turn green/yellow.
- When you're done inserting live cells, press the SPACE key, that will make the program run
- You are still able to change a cell's state by clicking.
- When you want to finish the program, press the TAB key.

