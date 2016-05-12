import math

resultat = 0
for tal in range(101):
    resultat = resultat + tal*tal

print(resultat)

resultat2 = sum(range(101)) ** 2

print(resultat2)

print(resultat2 - resultat)
