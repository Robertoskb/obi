# https://neps.academy/exercise/2130

from collections import deque

N, M, K = (int(n) for n in input().split())
sala = [[0] * N for _ in range(M)]
pos = {
    'N': (-1, 0),
    'S': (1, 0),
    'L': (0, 1),
    'O': (0, -1)
}

for _ in range(K):
    C, L, D = input().split()
    C, L = int(C)-1, int(L)-1
    
    sala[L][C] = -1
    
    pl, pc = pos[D]
    L, C = L + pl, C + pc 
    while (L < M and L >= 0) and (C < N and C >= 0):
        sala[L][C] = -1
        L, C = L + pl, C + pc 
        
positions = pos.values()
pilha = deque()
pilha.append((0, 0))

while pilha:
    l, c = pilha.popleft()
    if sala[l][c] != 0:
        continue
    
    sala[l][c] = 1
    for pl, pc in positions:
        l_tmp, c_tmp = l + pl, c + pc
        if (l_tmp >= M or l_tmp < 0) or (c_tmp >= N or c_tmp < 0):
            continue
        
        if sala[l_tmp][c_tmp] == 0:
            pilha.append((l_tmp, c_tmp))
        
print('S' if sala[M-1][N-1] == 1 else 'N')
