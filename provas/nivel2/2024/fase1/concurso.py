# https://neps.academy/br/exercise/2711

N, K = (int(n) for n in input().split())
notas = sorted([int(n) for n in input().split()], reverse=True)
count = 0

i = 0
while count < K:
    corte = notas[i]
    count += 1
    i += 1

print(corte)