# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f3/mancha/

# solução incompleta

N = int(input())

matriz = []
manchas = []

for i in range(N):
    cadeia = input()
    matriz.append(cadeia)
    for j in range(N):
        if cadeia[j] == '*':
            manchas.append((i, j))

inf = N * 2 - 1
t = len(manchas)
for i in range(t - 1):
    for j in range(i + 1, t):
        contador = [[inf for _ in range(N)] for _ in range(N)]

        P, Q = manchas[i], manchas[j]

        manhattan = abs(P[0] - Q[0]) + abs(P[1] - Q[1])
        contador[P[0]][P[1]] = 0

        pilha = [(P[0], P[1])]

        while pilha:
            x, y = pilha.pop()
            acm = contador[x][y] + 1

            if matriz[x][y] == '*':
                if x < N - 1 and contador[x + 1][y] > acm:
                    contador[x + 1][y] = acm
                    pilha.append((x + 1, y))

                if y < N - 1 and contador[x][y + 1] > acm:
                    contador[x][y + 1] = acm
                    pilha.append((x, y + 1))

                if x and contador[x - 1][y] > acm:
                    contador[x - 1][y] = acm
                    pilha.append((x - 1, y))

                if y and contador[x][y - 1] > acm:
                    contador[x][y - 1] = acm
                    pilha.append((x, y - 1))

        if contador[Q[0]][Q[1]] != manhattan:
            print('N')
            break

    else:
        continue

    break

else:
    print('S')
