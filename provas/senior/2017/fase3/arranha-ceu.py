# https://olimpiada.ic.unicamp.br/pratique/ps/2017/f3/arranhaceu/

from collections import defaultdict


def upd(x, v):
    while x <= n:
        bit[x] += v

        x += x & -x


def soma(x):
    ans = 0

    while x > 0:
        ans += bit[x]

        x -= x & -x

    return ans


bit = defaultdict(int)

n, q = (int(i) for i in input().split())
andares = [int(i) for i in input().split()]

for i in range(1, n+1):
    upd(i, andares[i-1])


resp = []
for _ in range(q):
    query = [int(i) for i in input().split()]

    if query[0] == 0:
        k, p = query[1], query[2]

        alt = p - andares[k-1]  # se no andar[k-1] tinha 10 e agora passa a ter 9, a alteração foi 9 - 10 = -1

        upd(k, alt)

        andares[k-1] = p

    else:
        resp.append(soma(query[1]))

for r in resp:
    print(r)
