# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f2/catador/

n, m = (int(i) for i in input().split())

baldes = [int(i) for i in input().split()]
oper = [int(i) for i in input().split()]

for i in oper:
    i -= 1
    c = baldes[i]
    j = 1

    for j in range(1, n+1):
        if abs(j-i) <= c:
            baldes[j-1] = max(0, baldes[j-1]-1)

print(sum(baldes))
