from jednostki.łucznik import Łucznik


a_army = []
for e in range(3):
    a_army.append(Łucznik())

print(a_army)

for łucznik in a_army:
    łucznik.maszeruj(1000)

print(a_army)

for łucznik in a_army:
    łucznik.atakuj()

print(a_army)