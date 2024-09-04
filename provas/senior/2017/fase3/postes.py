# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/postes/

n = int(input())
postes = (int(i) for i in input().split())
resp = [0, 0]

for p in postes:
    if p < 50:
        resp[0] += 1
    elif p < 85:
        resp[1] += 1

print(*resp)
