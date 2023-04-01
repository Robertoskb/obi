# https://olimpiada.ic.unicamp.br/pratique/p2/2012/f1/cavalo/

x = 4
y = 3
# Movimentos possíveis do cavalo
mov = [
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
    [-2, -1],
    [-2, 1],
    [-1, 2]
]
# Definindo as posições com buraco
buracos = [
    [1, 3],
    [2, 3],
    [2, 5],
    [5, 4]
]

N = int(input())
m = [int(n) for n in input().split()]
count = 0
pos = [x, y]

for i in m:
    pos.clear()
    count += 1
    x += mov[i-1][0]
    y += mov[i-1][1]
    pos = [x, y]
    if pos in buracos:
        break
    
print(count)