# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f2/supermercado/

n = int(input())

manor = float('inf')
for _ in range(n):
    p, g = (float(x) for x in input().split())
    manor = min(manor, (1000/g)*p)

print(f"{manor:.2f}")
