class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} {Pen.__name__} - ручка')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} {Pencil.__name__} - карандаш')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} {Handle.__name__} - маркер')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
