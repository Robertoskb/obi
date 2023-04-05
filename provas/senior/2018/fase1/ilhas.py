# https://olimpiada.ic.unicamp.br/pratique/ps/2018/f1/ilhas/

from queue import PriorityQueue

N, M = (int(i) for i in input().split())

grafo = [[] for _ in range(N)]

for _ in range(M):
    U, V, P = (int(i) for i in input().split())
    U -= 1
    V -= 1

    grafo[U].append((V, P))
    grafo[V].append((U, P))

S = int(input()) - 1

min_pings = [float('inf') for _ in range(N)]
marcados = [False] * N

pilha = PriorityQueue()
min_pings[S] = 0

pilha.put((0, S))

while not pilha.empty():
    acm, ilha = pilha.get()

    if marcados[ilha]:
        continue

    marcados[ilha] = True

    for destino, ping in grafo[ilha]:
        novo_ping = acm + ping

        if marcados[destino]:
            continue

        if novo_ping < min_pings[destino]:
            min_pings[destino] = novo_ping
            pilha.put((novo_ping, destino))

min_pings.sort()
print(min_pings[-1] - min_pings[1])
