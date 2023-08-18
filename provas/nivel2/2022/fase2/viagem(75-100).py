# https://neps.academy/exercise/2132

# uma solução errada porem que pontua mais por ser mais rápida

from queue import PriorityQueue

V, N, M = (int(i) for i in input().split())

ilhas = [[] for _ in range(N)]
tempos = [float('inf')] * N
marcados = [False] * N

for _ in range(M):
    a, b, t, p = (int(i) for i in input().split())
    ilhas[a-1].append((b-1, t, p))
    ilhas[b-1].append((a-1, t, p))

x, y = (int(i)-1 for i in input().split())

tempos[x] = 0

pilha = PriorityQueue()
pilha.put(((0, V), x))

while not pilha.empty():
    (acm, disp), ilha = pilha.get()

    if marcados[ilha]:
        continue

    marcados[ilha] = True

    for destino, td, pd in ilhas[ilha]:
        if marcados[destino]:
            continue

        novo_tempo = acm + td
        if disp >= pd and novo_tempo < tempos[destino]:
            tempos[destino] = novo_tempo
            pilha.put(((novo_tempo, disp-pd), destino))

if tempos[y] == float("inf"):
    print(-1)

else:
    print(tempos[y])
