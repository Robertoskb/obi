# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/promocao/

# Esta solução é exatamente a que o meu professor chegou, ainda estou tentando compreender o seu funcionamento

n = int(input())
grafo = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, e = (int(i) for i in input().split())
    grafo[a-1].append((b-1, e))
    grafo[b-1].append((a-1, e))


class Vertice:
    def __init__(self, vertice, vertice_anterior, empresa):
        self.vertice = vertice
        self.vertice_anterior = vertice_anterior
        self.empresa = empresa
        self.maior_caminho = [0, 0]
        self.it = iter(grafo[vertice])


pilha = [Vertice(0, -1, None)]
resp = 0
while pilha:
    topo = pilha[-1]
    try:
        vizinho, empresa = next(topo.it)
        if vizinho != topo.vertice_anterior:
            pilha.append(Vertice(vizinho, topo.vertice, empresa))

    except StopIteration:
        topo_removido = pilha.pop()
        resp = max(resp, sum(topo_removido.maior_caminho)+1)

        if pilha:
            sub_camiho, empresa = topo_removido.maior_caminho, topo_removido.empresa
            topo = pilha[-1]
            topo.maior_caminho[empresa] = max(topo.maior_caminho[empresa], sub_camiho[1-empresa] + 1)

print(resp)
