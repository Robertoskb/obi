# https://olimpiada.ic.unicamp.br/pratique/p2/2011/f2/vira/

# solução incompleta

def vira(p, i, c):
    p[i] = None

    if i < N-1 and p[i+1] is not None:
        p[i+1] = not p[i+1]

    if i and p[i-1] is not None:
        p[i-1] = not p[i-1]

    for index in range(N):
        if p[index] is not None and not p[index]:
            return vira(p.copy(), index, c+1)

    return c+1 if all(v is None for v in p) else 0


N = int(input())
cont = 0
pecas = [True if i == "B" else False for i in input().split()]
for x in range(N):
    if not pecas[x]:
        cont += vira(pecas.copy(), x, cont)

print(cont)
