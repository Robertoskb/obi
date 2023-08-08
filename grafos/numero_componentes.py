# https://noic.com.br/materiais-informatica/curso/graphs-02/

from queue import PriorityQueue

A, V = (int(i) for i in input().split())

grafo = [[] for _ in range(V)]

for _ in range(A):
    a, b = (int(i) - 1 for i in input().split())
    grafo[a].append(b)
    grafo[b].append(a)


componentes = [-1] * V

cont = 0

for i in range(V):

    if componentes[i] == -1:
        cont += 1
        componentes[i] = cont

        pilha = PriorityQueue()
        pilha.put(i)

        while not pilha.empty():
            componente = pilha.get()

            for vizinho in grafo[componente]:
                if componentes[vizinho] == -1:
                    componentes[vizinho] = componentes[componente]

                    pilha.put(vizinho)

print(cont)
