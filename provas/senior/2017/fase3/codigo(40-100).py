# https://olimpiada.ic.unicamp.br/pratique/ps/2017/f3/codigo/

N = int(input())

cadeias = []

resp = ''
for i in range(N):
    if not resp:
        cadeia = input()
        if cadeia in cadeias:
            resp = cadeia
        for j in range(i - 1):
            for k in range(j + 1, i):
                if cadeia in cadeias[j] + cadeias[k] or cadeia in cadeias[k] + cadeias[j]:
                    resp = cadeia
        cadeias.append(cadeia)
    else:
        input()

print(resp or 'ok')
