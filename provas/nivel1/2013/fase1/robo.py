# https://neps.academy/br/exercise/502

L, C = [int(x) for x in input().split()]
A, B = [int(x) - 1 for x in input().split()]

salao = [input().split() for _ in range(L)]

while True:
    direcoes = [
        (A - 1, B), (A + 1, B),
        (A, B - 1), (A, B + 1)
    ]

    for linha, coluna in direcoes:
        if 0 <= linha < L and 0 <= coluna < C and salao[linha][coluna] == '1':
            salao[A][B] = '0'
            A, B = linha, coluna
            break
    else:
        print(A + 1, B + 1)
        break
