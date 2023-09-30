# https://olimpiada.ic.unicamp.br/pratique/p2/2019/f3/etiquetas/

from collections import defaultdict

n, k, c = (int(i) for i in input().split())

nums = [int(i) for i in input().split()]

pref = defaultdict(int)
pref[0] = nums[0]
for i in range(1, n):
    pref[i] = pref[i-1] + nums[i]

dp = defaultdict(lambda: float('inf'))

dp[-1, 0] = 0
for i in range(n):
    for j in range(k+1):
        dp[i, j] = dp[i-1, j]

        if j and i >= c:
            dp[i, j] = min(dp[i, j], dp[i-c, j-1] + pref[i] - pref[i-c])

print(pref[n-1] - dp[n-1, k])
