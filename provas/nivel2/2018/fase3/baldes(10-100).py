# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f3/baldes/

def perguntar(ini, fim):
    resp = -1

    maiores = [max(baldes[i]) for i in range(ini, fim)]
    menoroes = [min(baldes[i]) for i in range(ini, fim)]

    for i in range(fim-ini):
        for j in range(fim-ini):
            if i != j:
                resp = max(maiores[i] - menoroes[j], resp)

    return resp


N, M = (int(i) for i in input().split())
baldes = tuple([int(i)] for i in input().split())

resps = []

for _ in range(M):
    op = [int(i) for i in input().split()]

    if op[0] == 1:
        baldes[op[2]-1].append(op[1])

    else:
        resps.append(perguntar(op[1]-1, op[2]))

for r in resps:
    print(r)
