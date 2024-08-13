# https://neps.academy/br/exercise/2303

from collections import defaultdict


def dentro(x, y):
    return 1 <= x <= m and 1 <= y <= n


direcs = {
    'N': (-1, 0),
    'S': (1, 0),
    'O': (0, -1),
    'L': (0, 1)
}

n, m, k = (int(i) for i in input().split())

dp = defaultdict(int)

for _ in range(k):
    c, l, d = input().split()
    l, c = int(l), int(c)

    dp[l, c] = 1

    while dentro(l, c):
        l += direcs[d][0]
        c += direcs[d][1]

        dp[l, c] = 1

if dp[1, 1]:
    print('N')
    exit()

pilha = [(1, 1)]

while pilha:
    x, y = pilha.pop()

    for dx, dy in direcs.values():
        nx, ny = x + dx, y + dy

        if dentro(nx, ny) and not dp[nx, ny]:
            pilha.append((nx, ny))
            dp[nx, ny] = 2

print('S' if dp[m, n] == 2 else 'N')
