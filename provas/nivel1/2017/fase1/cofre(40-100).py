# https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/cofre/

N, M = (int(i) for i in input().split())

barra = [int(i) for i in input().split()]
sequencia = [int(i) for i in input().split()]

dp = [[0] * 10 for _ in range(N+1)]

dp[1][barra[0]] = 1
for i in range(2, N+1):
    for j in range(10):
        dp[i][j] += dp[i-1][j]
    dp[i][barra[i-1]] += 1
    # barra[i-1] porque estamos a dp está armazenando a partir de 1 e não de 0


# dp[i][j] armazena o quantas vezes j aparece até a posição i da barra
# N+1 para evitar problemas com i-1

contador = [0] * 10
contador[barra[0]] = 1  # apenas na primeira vez o valor atual é contabilizado

atual = 1
for x in range(1, M):
    proximo = sequencia[x]
    for i in range(10):
        if proximo > atual:
            # soma da esquerda para a direita descartando a posição atual
            contador[i] += dp[proximo][i] - dp[atual][i]
        else:
            # soma da direita para a esquerda descartando a posição atual
            # ou, em um outro ponto de vista, descartando a posição final da esquerda para a direita
            contador[i] += dp[atual-1][i] - dp[proximo-1][i]

        # formula base: dp[proximo][i] - dp[atual-1][i]
        # isso considera o ponto atual e o final

    atual = proximo


print(*contador)
