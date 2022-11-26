# https://olimpiada.ic.unicamp.br/pratique/ps/2018/f3/muro/

N = int(input())

muro = [None for _ in range(10**4)]
muro[0], muro[1], muro[2] = 1, 1, 5

for i in range(3, N+1):
    muro[i] = (muro[i-1] + 4*muro[i-2] + 2*muro[i-3]) % (10**9+7)

print(muro[N])
