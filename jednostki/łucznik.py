from wojownik import Wojownik

class Łucznik(Wojownik):

    def __init__(self):
        super().__init__()
        self._life = 40
        self.arrows = 10

    def atakuj(self):
        if self.arrows > 0:
            print('Łucznik: wypuściłem strzały!')
            self._exp += 0.4
            self.arrows -= 1
        else:
            print('Nie masz strzał, nie masz już czym strzelać')