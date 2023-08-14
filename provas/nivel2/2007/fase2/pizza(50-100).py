# https://olimpiada.ic.unicamp.br/pratique/p2/2007/f2/pizza/

def sub_soma(s, e):
    soma_max = -float("inf")
    max_atual = 0

    for i in range(s, e):
        max_atual += lista[i % n]
        if soma_max < max_atual:
            soma_max = max_atual
        max_atual = max(0, max_atual)

    return soma_max


n = int(input())
lista = [int(i) for i in input().split()]

resp = 0
i = 0
for j in range(n, n * 2):
    resp = max(resp, sub_soma(i, j))
    i += 1

print(resp)
