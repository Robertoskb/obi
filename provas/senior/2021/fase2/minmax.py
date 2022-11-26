# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/minmax/

S, A, B = (int(input()) for _ in range(3))

menor = next(i for i in range(A, B+1) if sum(int(c) for c in str(i)) == S)
maior = next(i for i in range(B, A-1, -1) if sum(int(c) for c in str(i)) == S)

print(menor)
print(maior)
