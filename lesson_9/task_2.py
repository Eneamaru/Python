class Road:
    def __init__(self, width, length):
        self._length = length
        self._width = width

    def weight(self, mass_1m, thickness):
        print(f'Необходимая масса асфальта: {int(self._width * self._length * mass_1m * thickness / 1000)}т.')


road_1 = Road(20, 5000)
road_1.weight(25, 5)
