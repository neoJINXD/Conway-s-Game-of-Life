import pyglet
import random as rand


class gameOfLife:
    def __init__(self, win_width, win_height, size):
        self.grid_width = win_width // size
        self.grid_height = win_height // size
        self.cell_size = size
        self.cells = []
        self.next = []
        self.generate_cells()

    def get_size(self):
        return self.cell_size

    def generate_cells(self):
        for row in range(self.grid_height):
            self.cells.append([])
            for col in range(self.grid_width):
                if (rand.random() > 0.49):
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)
        for row in range(self.grid_height):
            self.next.append([])
            for col in range(self.grid_width):
                self.next[row].append(0)

    def draw(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.cells[row][col]==1:
                    coords = (row*self.cell_size                 , col*self.cell_size                 ,
                              row*self.cell_size                 , col*self.cell_size + self.cell_size,
                              row*self.cell_size + self.cell_size, col*self.cell_size                 ,
                              row*self.cell_size + self.cell_size, col*self.cell_size + self.cell_size)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                [0,1,2, 1,2,3],
                                                ('v2i', coords))

    def neighbourCount(self,row, col):
        sum = 0

        sum += self.cells[(row-1) % self.grid_height][(col-1) % self.grid_width]
        sum += self.cells[(row-1) % self.grid_height][(col  ) % self.grid_width]
        sum += self.cells[(row-1) % self.grid_height][(col+1) % self.grid_width]
        sum += self.cells[(row  ) % self.grid_height][(col-1) % self.grid_width]
        sum += self.cells[(row  ) % self.grid_height][(col+1) % self.grid_width]
        sum += self.cells[(row+1) % self.grid_height][(col-1) % self.grid_width]
        sum += self.cells[(row+1) % self.grid_height][(col  ) % self.grid_width]
        sum += self.cells[(row+1) % self.grid_height][(col+1) % self.grid_width]

        return sum

    def update(self):
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.cells[row][col] == 1 and self.neighbourCount(row, col) <2 or self.neighbourCount(row, col) >3:
                    self.next[row][col] = 0
                elif self.cells[row][col] == 0 and self.neighbourCount(row, col) == 3:
                    self.next[row][col] = 1
                else:
                    self.next[row][col] = self.cells[row][col]

        self.cells,self.next = self.next,self.cells
