# https://olimpiada.ic.unicamp.br/pratique/p2/2014/f2/mapa/

from collections import defaultdict
from itertools import combinations

grafo = defaultdict(list)

n = int(input())

for _ in range(n-1):
    a, b, c = (int(i) for i in input().split())

    if not c:
        grafo[a-1].append(b-1)
        # grafo[b-1].append(a-1) // não é necessário


visitados = [-1] * n

for i in range(n):
    if visitados[i] == -1:
        visitados[i] = i

        pilha = grafo[i]

        while pilha:
            vizinho = pilha.pop()
            if visitados[vizinho] == -1:
                visitados[vizinho] = i

                pilha.extend(grafo[vizinho])


contador = defaultdict(int)
for v in visitados:
    contador[v] += 1

print(sum(a*b for a, b in combinations(contador.values(), 2)))
