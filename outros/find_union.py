def find(x):
    if pai[x] == x:
        return x

    pai[x] = find(pai[x])

    return pai[x]


def join(x, y):
    x, y = find(x), find(y)

    x, y = sorted((x, y), reverse=True, key=lambda x: peso[x])

    pai[x] = y
    peso[y] += peso[x]


n = int(input())
pai = [i for i in range(n)]
peso = [1] * n
