# https://neps.academy/br/exercise/2171

from collections import defaultdict

N = int(input())
total = 0
camelos = defaultdict(int)

for i in range(N):
    p = int(input())
    total += p
    camelos[i] = p
    
media = total // N
for i in range(N):
    print(media - camelos[i])