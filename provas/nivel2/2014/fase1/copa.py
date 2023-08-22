# https://olimpiada.ic.unicamp.br/pratique/p2/2014/f1/copa/

# é práticamente a aplicação pura de MST,
# porém com a adição de uma prioridade a mais na hora de ordenar as arestas

def find(x):
    if pai[x] == x:
        return x

    pai[x] = find(pai[x])

    return pai[x]


def join(x, y):
    x, y = find(x), find(y)

    if peso[x] > peso[y]:
        pai[y] = x
    elif peso[y] > peso[x]:
        pai[x] = y

    else:
        pai[x] = y
        peso[y] += 1


n, f, r = (int(i) for i in input().split())

pai = list(range(n))
peso = [0] * n

arestas = []
for _ in range(f):
    a, b, c = (int(i) for i in input().split())
    arestas.append((0, a-1, b-1, c))

for _ in range(r):
    i, j, k = (int(i) for i in input().split())
    arestas.append((1, i-1, j-1, k))

arestas.sort(key=lambda x: (x[0], x[3]))

resp = 0
for _, x, y, c in arestas:
    if find(x) != find(y):
        join(x, y)
        resp += c

print(resp)
