class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Income: {self._income["wage"] + self._income["bonus"]}$')


Ilon = Position('Mask', 'Ilon', 'CEO', 1000000000, 500000000)

Ilon.get_full_name()
Ilon.get_total_income()
