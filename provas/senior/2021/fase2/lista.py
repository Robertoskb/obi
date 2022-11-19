# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/lista/

N = int(input())

lista = [int(i) for i in input().split()]

esquerda, direita = 0, N-1

operacoes = 0
while esquerda < direita:
    if lista[esquerda] == lista[direita]:
        esquerda += 1
        direita -= 1

        continue

    if lista[direita] > lista[esquerda]:
        lista[esquerda+1] += lista[esquerda]
        esquerda += 1

    elif lista[direita] < lista[esquerda]:
        lista[direita-1] += lista[direita]
        direita -= 1

    operacoes += 1

print(operacoes)
