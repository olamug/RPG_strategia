from wojownik import Wojownik
from jednostki.rycerz import Rycerz
from jednostki.łucznik import Łucznik
from strategia_2 import k_army
from strategia_3 import a_army

def main():
    knight = Rycerz()
    print(knight)
    knight.maszeruj(10)
    knight.atakuj()
    print(knight)

    archer = Łucznik()
    archer.maszeruj(20)
    archer.atakuj()
    print(archer)

    print(k_army)
    print(a_army)

    army = k_army + a_army
    print(army)

    for warrior in army:
        warrior.atakuj()

    print(army)

if __name__ == "__main__":
    main()