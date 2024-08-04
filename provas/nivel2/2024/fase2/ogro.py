# https://neps.academy/br/exercise/2710

E, D = (int(input()) for _ in range(2))

if E > D:
    print(E + D)
else:
    print(2 * (D-E))