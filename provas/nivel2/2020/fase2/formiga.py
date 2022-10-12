# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/formiga/
# este algorimo está no gabarito da prova


def buscar(k):
    if caminhos[k] == -1:
        caminhos[k] = 0

        for q in grafo[k]:
            caminhos[k] = max(caminhos[k], buscar(q)+1)

    return caminhos[k]


S, T, P = (int(i) for i in input().split())
profundidades = [int(i) for i in input().split()]

grafo = [[] for _ in range(S)]
caminhos = [-1 for _ in range(S)]

for _ in range(T):
    j, i = (int(i) for i in input().split())
    i -= 1
    j -= 1

    if profundidades[i] > profundidades[j]:
        grafo[i].append(j)
    elif profundidades[j] > profundidades[i]:
        grafo[j].append(i)

print(buscar(P-1))
