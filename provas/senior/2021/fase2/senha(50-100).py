# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/senha/

from itertools import product
   

N, M, K = (int(i) for i in input().split())

senha = input().replace("#",  "{}")
subs = [input() for _ in range(M)]

ordenadas = sorted(product(*subs))
correta = int(input()) - 1

print(senha.format(*ordenadas[correta]))
