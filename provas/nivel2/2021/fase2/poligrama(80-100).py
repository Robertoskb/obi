# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/poligrama/

N = int(input())
A = input()

for i in range(1, N//2+1):
    raiz = A[:i]
    sorted_raiz = sorted(raiz)
    
    for j in range(i, N, i):
        if sorted(A[j:i+j]) != sorted_raiz:
            break
    else:
        break
            
else:
    raiz = '*'
  
print(raiz)
