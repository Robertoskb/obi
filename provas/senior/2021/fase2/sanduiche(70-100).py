# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/sanduiche/

from itertools import combinations


def descartar(it, x, y):
	for c in it:
		if x in c and y in c:
			continue
		yield c


n, m = (int(i) for i in input().split())

r = range(1, n+1)
combinacoes = (c for i in r for c in combinations(r, r=i))
for _ in range(m):
	x, y = (int(i) for i in input().split())
	combinacoes = descartar(combinacoes, x, y)

print(sum(1 for _ in combinacoes))
