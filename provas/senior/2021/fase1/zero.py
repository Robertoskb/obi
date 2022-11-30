# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/zero/

numeros = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        numeros.pop()
    else:
        numeros.append(x)

print(sum(numeros))
