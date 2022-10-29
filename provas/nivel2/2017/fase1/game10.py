# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/game10/

from itertools import cycle

n = int(input())
d = int(input())
a = int(input())

ciclo = cycle(range(1, n+1))
  
for i in range(a-1):
  next(ciclo)
 
count = 0
for i in ciclo:
  if i == d:
    break
  count += 1
  
print(count)
