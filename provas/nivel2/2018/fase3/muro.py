# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f3/muro/

from collections import defaultdict

dp = defaultdict(int)
mod = 1e9+7

n = int(input())

dp[0], dp[1], dp[2] = 1, 1, 5

for i in range(3, n+1):
    dp[i] = (dp[i-1] + 4*dp[i-2] + 2*dp[i-3]) % mod

print(int(dp[n]))