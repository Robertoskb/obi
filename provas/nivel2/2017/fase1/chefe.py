# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/chefe/

N, M, I = (int(i) for i in input().split())

idades = [int(i) for i in input().split()]
cargos = list(range(N))

grafo = [[] for _ in range(N)]

for _ in range(M):
    x, y = (int(i)-1 for i in input().split())
    grafo[y].append(x)

resps = []
for _ in range(I):
    instr = input().split()

    if instr[0] == "T":
        a, b = (int(i)-1 for i in instr[1:])
        idades[cargos[a]], idades[cargos[b]] = idades[cargos[b]], idades[cargos[a]]
        cargos[a], cargos[b] = cargos[b], cargos[a]

    else:
        e = int(instr[1])-1

        menor_idade = 101

        marcados = [False for _ in range(N)]
        pilha = [cargos[e]]
        while pilha:
            empregado = pilha.pop()

            for chefe in grafo[empregado]:
                if not marcados[chefe]:
                    menor_idade = min(menor_idade, idades[chefe])
                    marcados[chefe] = True
                    pilha.append(chefe)

        if menor_idade > 100:
            resps.append('*')
        else:
            resps.append(menor_idade)

for r in resps:
    print(r)
