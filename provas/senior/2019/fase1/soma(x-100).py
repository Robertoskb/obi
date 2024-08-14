# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f1/soma/

n, k = (int(i) for i in input().split())
v = [int(i) for i in input().split()]

somas = [0] * (n + 1)
for i in range(1, n + 1):
    somas[i] = somas[i-1] + v[i-1]

cont = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if somas[j] - somas[i-1] == k:
            cont += 1

print(cont)
