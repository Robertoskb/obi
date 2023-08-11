# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/retangulo/

N = int(input())
arvores = [int(i) for i in input().split()]

somas = [0] * N

for i in range(N):
    somas[i] = somas[i-1] + arvores[i]

circunferencia = sum(arvores)

if circunferencia % 2 != 0:
    print("N")
    exit()

meia_circ = circunferencia // 2
cont = 0
for inicio in range(N-1):
    fim = N-1

    while inicio < fim:
        soma = somas[fim] - somas[inicio]

        if soma == meia_circ:
            cont += 1

            break

        if soma > meia_circ:
            fim -= 1

        else:
            break


print('S' if cont > 1 else 'N')
