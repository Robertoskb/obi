# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/torneio/

count = 0
for _ in range(6):
    if input() == 'V':
        count += 1

resp = -1
if count > 0:
    resp = 3

if count > 2:
    resp = 2

if count > 4:
    resp = 1

print(resp)
