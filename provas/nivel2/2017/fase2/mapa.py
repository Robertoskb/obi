# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/mapa/

L, C = (int(i) for i in input().split())

mapa = []
pilha = []
for i in range(L):
    linha = input()
    mapa.append(list(linha))

    if 'o' in linha:
        pilha.append((i, linha.index('o')))

resp = pilha[-1]
while pilha:
    x, y = pilha.pop()

    if mapa[x][y] != '.':
        mapa[x][y] = '.'
        resp = x, y

        if x < L-1:
            pilha.append((x+1, y))

        if y < C-1:
            pilha.append((x, y+1))

        if x:
            pilha.append((x-1, y))

        if y:
            pilha.append((x, y-1))


print(resp[0]+1, resp[1]+1)
