# https://neps.academy/br/exercise/2438

n = int(input())
sequencia = [int(input()) for _ in range(n)]

passou = {}
left = 0
resp = 0
for i in range(n):
    num = sequencia[i]
    if passou.get(num, -1) >= left:
        left = passou[num] + 1
    else:
        resp = max(resp, i - left + 1)
    passou[num] = i
print(resp)
