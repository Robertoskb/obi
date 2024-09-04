# https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/mesa/

mesa = [False, False, False]

a = int(input())
b = int(input())

mesa[a % 3] = True

mesa[b % 3 if not mesa[b % 3] else (b+1) % 3] = True

print(mesa.index(False))
