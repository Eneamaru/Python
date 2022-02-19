class Cell:
    def __init__(self, cells):
        self.my_cells = int(cells)

    def __add__(self, other):
        return Cell(self.my_cells + other.my_cells)

    def __sub__(self, other):
        if Cell(self.my_cells - other.my_cells).my_cells < 0:
            raise ValueError('Value must be positive')
        else:
            return Cell(self.my_cells - other.my_cells)

    def __mul__(self, other):
        return Cell(self.my_cells * other.my_cells)

    def __floordiv__(self, other):
        return Cell(self.my_cells // other.my_cells)

    def make_order(self, row):
        x = 0
        result = ''
        for i in range(row, self.my_cells + 1, row):
            result += '*' * (i - x) + '\n'
            x = i
        result += '*' * (self.my_cells - x)
        return print(result)


cell_1 = Cell(36)
cell_2 = Cell(7)
cell_3 = cell_1 + cell_2

Cell.make_order(cell_3, 10)
