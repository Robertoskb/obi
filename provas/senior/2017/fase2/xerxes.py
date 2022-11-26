# https://olimpiada.ic.unicamp.br/pratique/ps/2017/f2/xerxes/


dario = xerxes = 0


def check(jogada):
    global dario, xerxes
    jogadas = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (0, 2), (1, 3), (2, 4), (3, 0), (4, 1)
    ]

    if jogada in jogadas:
        dario += 1

    else:
        xerxes += 1


N = int(input())
for _ in range(N):
    check(tuple(int(i) for i in input().split()))

print('dario' if dario > xerxes else 'xerxes')
