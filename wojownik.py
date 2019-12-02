class Wojownik:

    def __init__(self):
        self._exp = 0

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}: hp={self._life}, exp={self._exp}."

    def maszeruj(self, dystans):
        name = self.__class__.__name__
        print(f'{name}: przeszedłem {dystans} m.')
        self._exp += 0.2*dystans