from wojownik import Wojownik

class Rycerz(Wojownik):

    def __init__(self):
        super().__init__()
        self._life = 60

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self._exp += 0.3