# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/bingo/

N, K, U = (int(i) for i in input().split())

cartelas = [input().split() for _ in range(N)]
sorteados = input().split()

for s in sorteados:
    for cartela in cartelas:
        if s in cartela:
            cartela.remove(s)

    if any(not cartela for cartela in cartelas):
        break

print(' '.join(str(i+1) for i in range(N) if not cartelas[i]))
