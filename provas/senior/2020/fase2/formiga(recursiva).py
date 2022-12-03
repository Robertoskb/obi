# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f2/formiga/
# este algorimo está no gabarito da prova


def buscar(inicio):
    if distancias[inicio] == -1:
        distancias[inicio] = 0

        for destino in grafo[inicio]:
            distancias[inicio] = max(distancias[inicio], buscar(destino)+1)

    return distancias[inicio]


S, T, P = (int(i) for i in input().split())
profundidades = [int(i) for i in input().split()]

grafo = [[] for _ in range(S)]
distancias = [-1 for _ in range(S)]

for _ in range(T):
    j, i = (int(i)-1 for i in input().split())

    if profundidades[i] > profundidades[j]:
        grafo[i].append(j)
    elif profundidades[j] > profundidades[i]:
        grafo[j].append(i)

print(buscar(P-1))
