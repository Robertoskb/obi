INF = float('inf')

N, M = (int(n) for n in input().split())
distancia = [[INF]*N for _ in range(N)]

for _ in range(M):
    U, V, W = (int(n) for n in input().split())
    distancia[U][V] = distancia[V][U] = W
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            distancia[i][j] = min(distancia[i][j], distancia[i][k] + distancia[k][j])
            
menor = INF

for i in range(N):
    maior = -1
    for j in range(N):
        maior = max(maior, distancia[i][j])
    if maior < menor:
        menor = maior
            
print(menor)