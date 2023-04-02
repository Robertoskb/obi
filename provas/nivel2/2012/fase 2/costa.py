# https://olimpiada.ic.unicamp.br/pratique/p1/2012/f2/costa/

def costa(x: int, y: int, ilhas: list):
    M = len(ilhas)
    N = len(ilhas[0])
    
    if ilhas[x][y] == "#":
        if x == 0 or ilhas[x-1][y] == ".":
            return True
        elif x == M-1 or ilhas[x+1][y] == ".":
            return True
        elif y == 0 or ilhas[x][y-1] == ".":
            return True
        elif y == N-1 or ilhas[x][y+1] == ".":
            return True
        
    else:
        return False

M, N = (int(n) for n in input().split())
ilhas = []
for _ in range(M):
    ilhas.append(input().strip())
costas = 0    

for i in range(M):
    for j in range(N):
        if costa(i, j, ilhas):
            costas += 1
            
print(costas)