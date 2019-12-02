from jednostki.rycerz import Rycerz


k_army = []
for e in range(4):
    k_army.append(Rycerz())

print(k_army)

for rycerz in k_army:
    rycerz.maszeruj(1000)

print(k_army)

k_army.append(Rycerz())

for rycerz in k_army:
    rycerz.atakuj()

print(k_army)