# https://olimpiada.ic.unicamp.br/pratique/p2/2014/f2/mapa/

from collections import defaultdict
from itertools import combinations


def find(x):
    if pai[x] == x:
        return x

    pai[x] = find(pai[x])

    return pai[x]


def join(x, y):
    x, y = find(x), find(y)

    x, y = sorted((x, y), reverse=True, key=lambda x: peso[x])

    pai[x] = y
    peso[y] += peso[x]


n = int(input())

peso = [1] * n
pai = [i for i in range(n)]

for i in range(n-1):
    a, b, c = (int(i) for i in input().split())

    if not c:
        join(a-1, b-1)


contador = defaultdict(int)
for i in range(n):
    contador[find(i)] += 1

print(sum(a*b for a, b in combinations(contador.values(), 2)))
