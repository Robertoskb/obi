# https://olimpiada.ic.unicamp.br/pratique/p1/2017/f3/gomoku/

def valid(x, y):
    return 0 <= x <= 14 and 0 <= y <= 14


matriz = [input().split() for i in range(15)]

resp = '0'
for i in range(15):
    for j in range(15):
        ini = matriz[i][j]

        if ini == '0':
            continue

        # horizontais
        for k in range(1, 5):
            if not valid(i, j+k):
                break
            if matriz[i][j+k] != ini:
                break
            if k == 4:
                resp = ini

        # verticais
        for k in range(1, 5):
            if not valid(i+k, j):
                break
            if matriz[i+k][j] != ini:
                break
            if k == 4:
                resp = ini

        # diagonais esquerda direita baixo
        for k in range(1, 5):
            if not valid(i+k, j+k):
                break
            if matriz[i+k][j+k] != ini:
                break
            if k == 4:
                resp = ini

        # diagonais direita esquerda baixo
        for k in range(1, 5):
            if not valid(i+k, j-k):
                break
            if matriz[i+k][j-k] != ini:
                break
            if k == 4:
                resp = ini

print(resp)
