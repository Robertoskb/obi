# https://olimpiada.ic.unicamp.br/pratique/p2/2007/f2/tele/

from collections import deque

n, l = (int(i) for i in input().split())

contador = [0] * n
ocupados = [0] * n

ligacoes = []

for i in range(l):
    t = int(input())
    if i < n:
        contador[i] += 1
        ocupados[i] = t

    else:
        ligacoes.append(t)

ligacoes = deque(ligacoes)

while ligacoes:
    for i in range(n):
        if ocupados[i]:
            ocupados[i] -= 1

        if ocupados[i] == 0 and ligacoes:
            contador[i] += 1
            ocupados[i] = ligacoes.popleft()

for i in range(n):
    print(i + 1, contador[i])
