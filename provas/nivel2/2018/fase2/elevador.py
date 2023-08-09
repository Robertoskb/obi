# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/elevador/

N = int(input())

pesos = sorted(int(i) for i in input().split())
pesos.insert(0, 0)

for i in range(N-1):
    if pesos[i+1] - pesos[i] > 8:
        print('N')

        break

else:
    print('S')
