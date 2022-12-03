# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/fissura/

n, f = (int(i) for i in input().split())
matriz = [[int(i) for i in input()] for _ in range(n)]

pilha = [(0, 0)]

while pilha:
    x, y = pilha.pop()
    if matriz[x][y] != '*' and f >= matriz[x][y]:
        matriz[x][y] = '*'
        if x > 0:
            pilha.append((x-1, y))
        if y > 0:
            pilha.append((x, y-1))
        if x < n-1:
            pilha.append((x+1, y))
        if y < n-1:
            pilha.append((x, y+1))

for lista in matriz:
    print(''.join(map(str, lista)))
