# https://neps.academy/exercise/2132

# Solução correta, porém que pontua menos por TLE

from collections import defaultdict
from queue import PriorityQueue

inf = float('inf')

V, N, M = (int(i) for i in input().split())

ilhas = defaultdict(list)  # [[[] for _ in range(V+1)] for _ in range(N)]

for _ in range(M):
    A, B, T, P = (int(i) for i in input().split())

    # tomando V = 10 e P = 3
    # Só é possível de sair de A até B tendo gasto até 7 reais
    # para ir até B gastando 3, pois o limite é 10 reais, 10-3 = 7
    for val in range(0, (V-P)+1):
        ilhas[A, val].append(((B, val+P), T))
        ilhas[B, val].append(((A, val+P), T))

tempos = defaultdict(lambda: inf)  # [[inf] * (V+1) for _ in range(N)]
marcados = defaultdict(bool)  # [[False] * (V+1) for _ in range(N)]

X, Y = (int(i) for i in input().split())

# só nos resta calcular o caminho mínimo de X tendo gasto 0 reais
# até Y gastando de 0 a V reais, depois retornar qual desses custos
# tiveram o menor tempo

pilha = PriorityQueue()
pilha.put((0, (X, 0)))
while not pilha.empty():
    acm, (ilha, gasto) = pilha.get()

    if marcados[ilha, gasto]:
        continue
    marcados[ilha, gasto] = True

    for (destino, gasto_d), tempo in ilhas[ilha, gasto]:
        if marcados[destino, gasto_d]:
            continue

        novo_custo = acm + tempo

        if novo_custo < tempos[destino, gasto_d]:
            tempos[destino, gasto_d] = novo_custo

            pilha.put((novo_custo, (destino, gasto_d)))

resp = inf
for gasto in range(V+1):
    resp = min(resp, tempos[Y, gasto])

print(-1 if resp == inf else resp)
