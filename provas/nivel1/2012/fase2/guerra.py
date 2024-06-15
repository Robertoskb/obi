# https://neps.academy/br/exercise/237

N = int(input())
lista = [int(x) for x in input().split()]

soma = 0
limite = sum(lista) // 2

for i in range(N):
    soma += lista[i]
    if soma == limite:
        print(i + 1)
        break
