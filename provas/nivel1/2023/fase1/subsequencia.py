# https://neps.academy/br/exercise/2320

B = int(input().split()[1])
Sa, Sb = [input().split() for _ in range(2)]

i = 0

for n in Sa:
    if n == Sb[i]:
        i += 1

        if i == B:
            print('S')
            exit()

print('N')
