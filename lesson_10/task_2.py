from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def materials_used(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def materials_used(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def materials_used(self):
        return self.height * 2 + 0.3


coat = Coat(15)
suit = Suit(30)

print(coat.materials_used)
print(suit.materials_used)
