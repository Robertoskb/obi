from collections import defaultdict


def find(x):
    if pai[x] == x:
        return x

    pai[x] = find(pai[x])

    return pai[x]


def join(x, y):
    x, y = find(x), find(y)

    if peso[x] == peso[y]:
        pai[y] = x
        peso[y] += 1

    elif peso[x] > peso[y]:
        pai[y] = x
    elif peso[y] > peso[x]:
        pai[x] = y


pai = defaultdict(int)
peso = defaultdict(int)

n, m = (int(i) for i in input().split())


for i in range(n):
    pai[i] = i

arestas = []

for _ in range(m):
    a, b, p = (int(i) for i in input().split())
    arestas.append((a, b, p))

arestas.sort(key=lambda x: x[2])  # ordena as arestas pelo peso

mst = []
for x, y, p in arestas:
    if find(x) != find(y):
        join(x, y)
        mst.append((x, y, p))

for i in mst:
    print(*i)