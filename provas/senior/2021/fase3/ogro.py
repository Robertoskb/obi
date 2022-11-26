# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f3/ogro/

N = int(input())

print('I' * min(5, N) or '*')
print('I' * (N-5) or '*')
