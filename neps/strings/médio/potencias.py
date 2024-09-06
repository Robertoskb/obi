# https://neps.academy/br/exercise/1722

soma = 0

n = int(input())

for _ in range(n):
    x = input()
    soma += int(x[:-1]) ** int(x[-1])

print(soma)
