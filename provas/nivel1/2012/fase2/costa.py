# https://neps.academy/br/exercise/329

M, N = [int(x) for x in input().split()]
mapa = ['.' * (N + 2)] + ['.' + input() + '.' for _ in range(M)] + ['.' * (N + 2)]

total = 0

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if mapa[i][j] == '#' and any(mapa[a][b] == '.' for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))):
            total += 1

print(total)
