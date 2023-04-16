# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f1/cor/

N = int(int(input()))

zeros = []
papel = [[] for _ in range(N)]
for i in range(N):
    for c, j in enumerate(input()):
        papel[i].append(j)
        if j == '0':
            zeros.append((i, c))

for i in range(N):
    for j in range(N):
        dif = min(abs(i-x) + abs(j-y) for x, y in zeros)
        papel[i][j] = dif if dif < 10 else 9

    print(''.join(str(l) for l in papel[i]))

