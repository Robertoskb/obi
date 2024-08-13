# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/senha/

n, m, k = (int(i) for i in input().split())
senha = input().replace("#", "{}")

subs = [sorted(input()) for _ in range(m)]

p = int(input())-1


resp = []
for i in range(m-1, -1, -1):
    resp.append(subs[i][p % k])
    p //= k

print(senha.format(*resp[::-1]))
