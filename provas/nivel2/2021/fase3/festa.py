# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f3/festa/

def sortear(it, n):
	for c, i in enumerate(it):
		if (c+1) % n == 0:
			continue
		yield i


N = int(input())
M = int(input())
suditos = range(N)

for _ in range(M):
	suditos = sortear(suditos, int(input()))

for s, _ in zip(suditos, range(10000)):
	print(s+1)
	