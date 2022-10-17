# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/botas/

n = int(input())
botas = []

for i in range(n):
    num, pe = input().split()
    botas.append([int(num), pe])
    
count = 0
for i in range(30, 61):
    d, e = botas.count([i, 'D']), botas.count([i, 'E'])
    count += min(d, e)
    
print(count)