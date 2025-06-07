# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/garamana/
from collections import defaultdict

P = defaultdict(int)

for c in input():
    P[c] += 1

for c in input():
    if c == "*":
        continue
    
    if P[c] > 0:
        P[c] -= 1
    else:
        print('N') 
        break    
else:
    print('S')
