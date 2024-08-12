# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/poligrama/

def divisores(n):
    divisores = [1]

    i = 2
    while i * i <= n:  # O(sqrt(n))
        if n % i == 0:
            divisores.append(i)
            divisores.append(n // i)
        i += 1

    # divisores.append(n) // não é necessário
    divisores.sort()

    return divisores


def verifica(A, d):
    raiz = A[:d]
    sorted_raiz = sorted(raiz)

    for j in range(d, N, d):
        if sorted(A[j:d+j]) != sorted_raiz:
            return False
    return True


N = int(input())
A = input()

for div in divisores(N):
    if verifica(A, div):
        print(A[:div])
        break
else:
    print('*')
