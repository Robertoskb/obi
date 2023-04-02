# https://olimpiada.ic.unicamp.br/pratique/p2/2012/f2/soma/

N = int(input())
casas = {int(input()): i for i in range(N)}
K = int(input())

for casa in casas:
    c = k - casa
    if c in casas and casas[c] != casas[casa]:
        print(casa, c)
        break