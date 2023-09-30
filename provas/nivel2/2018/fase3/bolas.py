from collections import defaultdict

contador = defaultdict(int)

bolas = [int(i) for i in input().split()]

resp = 'S'
for bola in bolas:
    contador[bola] += 1
    if contador[bola] == 5:
        resp = 'N'

print(resp)
