def altura_maxima(k):
    if distancias[k] == -1:
        distancias[k] = 0

        for adjacente in adjacentes[k]:
            distancias[k] = max(distancias[k], altura_maxima(adjacente) + 1)

    return distancias[k]


N, M = [int(i) for i in input().split()]  # N = número de adjacentes, M = número de arestas
adjacentes = [[] for i in range(N)]  # prepara o grafo
distancias = [-1 for _ in range(N)]  # vai armazenar a maior distancia para chegar a cada nó do grafo

for _ in range(M):
    A, B = (int(i) for i in input().split())
    adjacentes[A].append(B)  # conecta A em B

# exemplo de grafo: [[1], [2], [3], []]
# 0 -> 1 -> 2 -> 3

print(altura_maxima(0))  # busca o maior caminho partindo do nó 0
