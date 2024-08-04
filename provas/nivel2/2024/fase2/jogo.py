# https://neps.academy/br/exercise/2714

from collections import defaultdict

N, Q = (int(n) for n in input().split())

# Posições adjacentes
pos = defaultdict(tuple)
pos[0] = (0, 1) # right
pos[1] = (0, -1) # left
pos[2] = (-1, 0) # top
pos[3] = (1, 0) # down
pos[4] = (-1, 1) # top-right
pos[5] = (-1, -1) # top-left
pos[6] = (1, 1) # down-right
pos[7] = (1, -1) # down-left

matriz = defaultdict(int)

for i in range(N):
    m = [int(n) for n in input()]
    for j in range(N):
        matriz[i, j] = m[j]


def next_stage():
    global matriz
    new_matriz = defaultdict(int)
    for i in range(N):
        for j in range(N):
            el = matriz[i,j]
            adj_vivo, adj_morto = 0, 0
            for k in range(8):
                tmp_i, tmp_j = pos[k]
                new_i, new_j = i + tmp_i, j + tmp_j

                if (new_i >= N or new_i < 0 or new_j >= N or new_j < 0):
                    continue

                adj = matriz[new_i,new_j]
                if adj == 0:
                    adj_morto += 1
                else:
                    adj_vivo += 1
            if el == 0:
                if adj_vivo == 3:
                    new_matriz[i, j] = 1
                else:
                    new_matriz[i,j] = 0
                
            elif el == 1:
                if adj_vivo == 2 or adj_vivo == 3:
                    new_matriz[i,j] = 1
                else:
                    new_matriz[i,j] = 0
            # print((i, j), el, adj_morto, adj_vivo)

    return new_matriz

for _ in range(Q):
    matriz = next_stage()
for i in range(N):
    for j in range(N):
        print(matriz[i, j], end='')
    print()