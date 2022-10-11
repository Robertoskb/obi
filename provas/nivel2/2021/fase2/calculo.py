# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/calculo/

s = int(input())
a = int(input())
b = int(input())

cont = 0
for i in range(a, b+1):
    if sum(int(d) for d in str(i)) == s:
        cont += 1

print(cont)
