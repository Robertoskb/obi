from collections import defaultdict


def find(x):
    if pai[x] == x:
        return x

    pai[x] = find(pai[x])

    return pai[x]


def join(x, y):
    x, y = find(x), find(y)

    if peso[x] == peso[y]:
        pai[x] = y
        peso[y] += 1

    elif peso[x] > peso[y]:
        pai[y] = x
    elif peso[y] > peso[x]:
        pai[x] = y


pai = defaultdict(int)
peso = defaultdict(int)
