# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f2/estrada/

T = int(input())
N = int(input())

cidades = [int(input()) for _ in range(N)]
cidades.sort()

# dobrado as distancias até as fronteiras
cidades.insert(0, -cidades[0])
cidades.append(T+(T-cidades[-1]))

menor_vizinhanca = 10000
for i in range(1, N+1):
    vizinhaca = ((cidades[i] - cidades[i-1]) / 2) + ((cidades[i+1] - cidades[i]) / 2)

    if vizinhaca < menor_vizinhanca:
        menor_vizinhanca = vizinhaca

print(f'{menor_vizinhanca:.2f}')
