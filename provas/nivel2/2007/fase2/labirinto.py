# https://olimpiada.ic.unicamp.br/pratique/p2/2007/f2/lab/

from queue import PriorityQueue


def altura_turno(i, j, turno):
    return (labirinto[i][j] + turno) % 10


def dentro(i, j):
    return (0 <= i <= n - 1) and (0 <= j <= m - 1)


def pode_pular(ie, je, id, jd, turno):
    altura_a = altura_turno(ie, je, turno)
    altura_b = altura_turno(id, jd, turno)

    return altura_b <= altura_a + 1


n, m = (int(i) for i in input().split())

labirinto = [[int(i) for i in input().split()] for _ in range(n)]

min_turnos = [[float("inf")] * m for _ in range(n)]
min_turnos[0][0] = 0

marcados = [[[False] * 10 for _ in range(m)] for _ in range(n)]

pilha = PriorityQueue()

pilha.put((0, 0, 0))

dl = (1, -1, 0, 0, 0)
dc = (0, 0, 1, -1, 0)

while not pilha.empty():
    turno_atual, i, j = pilha.get()

    altura = altura_turno(i, j, turno_atual)

    if marcados[i][j][altura]:
        continue

    marcados[i][j][altura] = True

    for d in range(5):
        turno = turno_atual

        i_d = i + dl[d]
        j_d = j + dc[d]

        if not dentro(i_d, j_d):
            continue

        altura_d = altura_turno(i_d, j_d, turno + 1)
        while not pode_pular(i, j, i_d, j_d, turno):
            turno += 1
            altura_d = altura_turno(i_d, j_d, turno + 1)

        if marcados[i_d][j_d][altura_d]:
            continue

        novo_custo = turno + 1
        if novo_custo < min_turnos[i_d][j_d]:
            min_turnos[i_d][j_d] = novo_custo

            pilha.put((turno + 1, i_d, j_d))

print(min_turnos[n - 1][m - 1])
