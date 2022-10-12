# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/3por2/

n = int(input())
doces = sorted(int(input()) for _ in range(n))
print(sum(doces[n//3:]))
