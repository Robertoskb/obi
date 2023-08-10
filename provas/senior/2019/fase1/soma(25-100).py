# https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/soma/

N, K = (int(i) for i in input().split())
V = [int(i) for i in input().split()]

cont = 0

for i in range(N):
    soma = V[i]

    if soma > K:
        continue

    if soma == K:
        cont += 1

    for j in range(i+1, N):
        soma += V[j]

        if soma == K:
            cont += 1

        if soma > K:
            break

print(cont)

