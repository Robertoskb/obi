# https://neps.academy/br/exercise/2128

n = int(input())

for i in range(n):
    for j in range(n):
        print(min(i, j, n-i-1, n-j-1)+1, end=' ')
    print()
