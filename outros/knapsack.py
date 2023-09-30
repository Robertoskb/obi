from collections import defaultdict

n = 4
val = [50, 100, 150, 200]
p = [8, 16, 32, 40]
c = 64

ans = -1
dp = defaultdict(int)
for i in range(n):
    for j in range(c+1):  # todos os pesos até c
        dp[i, j] = dp[i-1, j]

        if p[i] <= j:
            dp[i, j] = max(dp[i, j],  # nao colocar o item
                           dp[i-1, j-p[i]] + val[i]  # colocar o item
                           )

        ans = max(ans, dp[i, j])

print(dp[n-1, c])  # melhor resultado carregando exatamente o peso c
print(ans)  # melhor resultado

