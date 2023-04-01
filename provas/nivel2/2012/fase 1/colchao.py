#https://olimpiada.ic.unicamp.br/pratique/p2/2012/f1/colchao/

c = sorted([int(n) for n in input().split()])[:2] # Dimensões do colchão
H, L = input().split()
H, L = int(H), int(L)
if H - c[0] >= 0 and L - c[1] >= 0:
    print('S')
elif H - c[1] >= 0 and L - c[0] >= 0:
    print('S')
else:
    print('N')