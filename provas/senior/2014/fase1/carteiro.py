N, M = (int(n) for n in input().split())
casas = {n: i for i, n in enumerate(input().split())}
tempo = 0
casa_atual = 0

for casa in input().split():
    casa_destino = casas[casa]
    tempo += abs(casa_destino - casa_atual)
    casa_atual = casa_destino
    
print(tempo)