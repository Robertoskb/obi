# https://neps.academy/exercise/2131
from collections import defaultdict

n = int(input())
s = input()

dp = defaultdict(bool)

for i in range(n):
    dp[i, i] = True

ans = 1
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i] == s[j] and (j-i == 1 or dp[i+1, j-1]):
            dp[i, j] = True

            ans = max(ans, j-i+1)

print(ans)
