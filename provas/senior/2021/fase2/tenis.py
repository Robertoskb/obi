# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/tenis/

from itertools import permutations

perms = permutations((int(input()) for _ in range(4)), 4)

menor = 10000

for times in perms:
    soma1, soma2 = sum(times[:2]), sum(times[2:])
    dif = abs(soma1 - soma2)
    if dif < menor:
        menor = dif

print(menor)
