# https://neps.academy/br/exercise/110

N = int(input())
valores = input().split()

atual = 1
pontos = 1

for i in range(1, N):
    if valores[i] == valores[i-1]:
        atual += 1
        pontos = max(pontos, atual)
    else:
        atual = 1

print(pontos)
