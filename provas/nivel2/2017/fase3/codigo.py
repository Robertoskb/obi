# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/codigo/

N = int(input())

pref, suf, visto = set(), set(), set()

resp = 'ok'

for _ in range(N):
    cadeia = input()
    if cadeia in visto:
        resp = cadeia

    if resp == 'ok':
        visto.add(cadeia)
        for i in range(1, 10):
            p, s = cadeia[:i], cadeia[i:10]

            if p in suf and s in pref:
                resp = cadeia

            pref.add(p)
            suf.add(s)

print(resp)
