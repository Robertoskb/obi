# https://neps.academy/br/exercise/2168


n = int(input())
digitos = input().replace(' ', '')

c = 1

maxi = 10**1000+1


def seqstr(r):
    for i in r:
        for s in str(i):
            yield s


while c < maxi:
    ini = int(digitos[:c])

    seq = range(ini, maxi)

    for r, d in zip(seqstr(seq), digitos):
        if r != d:
            c += 1
            break
    else:
        print(ini)
        break
