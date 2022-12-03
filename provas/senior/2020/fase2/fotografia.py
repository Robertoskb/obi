# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f2/fotografia/

A, L = (int(i) for i in input().split())
N = int(input())

index = -1
menor_area = 200*200 + 1
for i in range(N):
    x, y = (int(i) for i in input().split())

    if (x >= A and y >= L) or (y >= A and x >= L):
        if x * y < menor_area:
            menor_area = x * y
            index = i+1

print(index)
