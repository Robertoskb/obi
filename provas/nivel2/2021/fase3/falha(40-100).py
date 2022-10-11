# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f3/falha/

n = int(input())

senhas = sorted((input() for _ in range(n)), key=len, reverse=True)

cont = 0
for i in range(n-1):
    maior = senhas[i]
    for j in range(i+1, n):
        menor = senhas[j]

        if maior == menor:
            cont += 2
        elif menor in maior:
            cont += 1

print(cont)
