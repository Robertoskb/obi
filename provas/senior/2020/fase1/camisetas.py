# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/camisetas/

n = int(input())
camisetas = input().split()
p = int(input())
m = int(input())

if camisetas.count('1') >= p and camisetas.count('2') >= m:
    print('S')

else:
    print('N')
