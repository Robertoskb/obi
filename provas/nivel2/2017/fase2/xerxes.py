# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/xerxes/

options = [
    [1, 2],
    [2, 3],
    [3, 4],
    [0, 4],
    [0, 1]
]

d, x = 0, 0
N = int(input())

for _ in range(N):
    D, X = (int(n) for n in input().split())
    if X in options[D]: d+=1
    else: x+=1
    
print("dario" if d > x else "xerxes")
