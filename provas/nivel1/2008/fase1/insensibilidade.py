# https://neps.academy/br/exercise/316

from math import dist


N = int(input())
total = 0

while N:
    X1, Y1, X2, Y2 = [int(x) for x in input().split()]
    total += dist((X1, Y1), (X2, Y2)) ** 2

    N -= 1

print(int(total))
