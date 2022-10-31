# https://olimpiada.ic.unicamp.br/pratique/p2/2016/f2/falta-uma/

from itertools import permutations

fats = [1, 2, 6, 24, 120, 720, 5040, 40320]

N = int(input())

permutacoes = [i for i in permutations(range(1, N+1))]

for _ in range(fats[N-1]-1):
    permutacoes.remove(tuple(int(i) for i in input().split()))

print(' '.join(map(str, permutacoes[0])))
