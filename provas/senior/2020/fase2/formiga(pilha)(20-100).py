# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f2/formiga/

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


class Salao:

    def __init__(self, salao, salao_ant):
        self.salao = salao
        self.salao_ant = salao_ant
        self.maior_caminho = 0
        self.it = iter(grafo[salao])


pilha = [Salao(P-1, -1)]
resp = 0
while pilha:
    topo = pilha[-1]

    try:
        vizinho = next(topo.it)

        if vizinho != topo.salao_ant:
            pilha.append(Salao(vizinho, topo.salao))

    except StopIteration:
        topo_removido = pilha.pop()
        resp = max(resp, topo_removido.maior_caminho+1)

        if pilha:
            acm = topo_removido.maior_caminho
            topo = pilha[-1]
            topo.maior_caminho = max(topo.maior_caminho, acm+1)

print(resp-1)
