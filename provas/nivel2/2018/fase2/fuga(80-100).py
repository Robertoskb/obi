# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/fuga/

N, M = (int(i) for i in input().split())

matriz = [[0] * M for _ in range(N)]

Xe, Ye = (int(i)-1 for i in input().split())
Xs, Ys = (int(i)-1 for i in input().split())


def dentro(i, j):
    return (0 <= i <= N-1) and (0 <= j <= M-1)


resp = 0

dl = (2, -2, 0, 0)
dc = (0, 0, 2, -2)


def dfs(i, j, d):
    global resp

    if (i, j) == (Xs, Ys):
        resp = max(resp, d)

        matriz[i][j] = 0

        return

    matriz[i][j] = 1

    for k in range(4):
        temp_i, temp_j = i + dl[k], j + dc[k]
        if dentro(temp_i, temp_j) and matriz[temp_i][temp_j] == 0:
            dfs(temp_i, temp_j, d+2)

    matriz[i][j] = 0


dfs(Xe, Ye, 1)

print(resp)
