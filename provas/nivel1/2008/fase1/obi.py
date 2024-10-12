# https://neps.academy/br/exercise/221

N, P = [int(x) for x in input().split()]
total = 0

while N:
  if sum([int(x) for x in input().split()]) >= P:
    total += 1
  N -= 1

print(total)
