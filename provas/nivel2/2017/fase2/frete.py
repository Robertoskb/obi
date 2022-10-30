# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/frete/

from queue import PriorityQueue

N, M = (int(i) for i in input().split())

cidades = [[] for _ in range(N)]
custos = [float('inf') for _ in range(N)]
marcados = [False for _ in range(N)]

for _ in range(M):
    A, B, C = (int(i) for i in input().split())
    cidades[A-1].append((B-1, C))
    cidades[B-1].append((A-1, C))


custos[0] = 0

pilha = PriorityQueue()
pilha.put((0, 0))
while not pilha.empty():
    acm, cidade = pilha.get()

    if marcados[cidade]:
        continue

    marcados[cidade] = True

    for destino, custo in cidades[cidade]:
        novo_custo = acm + custo
        if marcados[destino]:
            continue
        if custos[destino] > novo_custo:
            custos[destino] = novo_custo
            pilha.put((novo_custo, destino))


print(custos[N-1])
