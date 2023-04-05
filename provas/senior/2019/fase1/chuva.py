# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f1/chuva/

N, M = (int(i) for i in input().split())

parede = [list(input()) for _ in range(N)]

i, j = (0, parede[0].index('o'))

pilha = []
pilha.append((i+1, j))
if j > 0:
    pilha.append((i,  j-1))
if j < M-1:
    pilha.append((i, j+1))

while pilha:
    i, j = pilha.pop()

    if parede[i][j] == '.':
        if i == N-1:
            parede[i][j] = 'o'

            continue

        if i > 0 and parede[i-1][j] == 'o':
            parede[i][j] = 'o'

        if j > 0 and parede[i][j-1] == 'o' and parede[i+1][j-1] == '#':
            parede[i][j] = 'o'

        if j < M-1 and parede[i][j+1] == 'o' and parede[i+1][j+1] == '#':
            parede[i][j] = 'o'

        if parede[i][j] == 'o':
            pilha.append((i + 1, j))
            if j < M - 1:
                pilha.append((i, j + 1))

            if j > 0:
                pilha.append((i, j - 1))

for linha in parede:
    print(''.join(linha))
