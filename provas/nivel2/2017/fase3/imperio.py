# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/imperio/

from collections import defaultdict
import sys


sys.setrecursionlimit(10**5)


def dfs(u, pai):
    # calcular o numero de cidades conectadas direta ou indireatamente em u
    # basicamente o alg para calcular o tamanho de um sub árvore
    global resp

    size = 1
    for v in grafo[u]:
        if v != pai:  # para não gerar loop, pois o grafo não é direcionado
            size += dfs(v, u)

    dif = abs(size - (n - size))
    resp = min(dif, resp)

    return size


inf = float('inf')

n = int(input())

grafo = defaultdict(list)
for _ in range(n-1):
    a, b = (int(i) for i in input().split())
    grafo[a].append(b)
    grafo[b].append(a)


resp = n

dfs(1, -1)

print(resp)

