# https://neps.academy/br/exercise/2436

from collections import defaultdict

e, m, d = (int(i) for i in input().split())

gostam = defaultdict(lambda: (False, True))
for _ in range(m):
    x, y = sorted(int(i) for i in input().split())
    gostam[(x, y)] = True, False

nao_gostam = defaultdict(lambda: (False, True))
for _ in range(d):
    x, y = sorted(int(i) for i in input().split())
    nao_gostam[(x, y)] = True, True

grupos = [sorted(int(i) for i in input().split()) for _ in range(e//3)]

for grupo in grupos:
    p1 = grupo[0], grupo[1]
    p2 = grupo[0], grupo[2]
    p3 = grupo[1], grupo[2]

    if gostam[p1][0]:
        gostam[p1] = True, True
    if gostam[p2][0]:
        gostam[p2] = True, True
    if gostam[p3][0]:
        gostam[p3] = True, True

    if nao_gostam[p1][0]:
        nao_gostam[p1] = True, False
    if nao_gostam[p2][0]:
        nao_gostam[p2] = True, False
    if nao_gostam[p3][0]:
        nao_gostam[p3] = True, False

resp = 0
for p, (i, sats) in gostam.items():
    if not sats:
        resp += 1
for p, (i, sats) in nao_gostam.items():
    if not sats:
        resp += 1

print(resp)
