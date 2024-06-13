# https://neps.academy/br/exercise/2318

X, Y = [int(input()) for _ in range(2)]

if abs(X) > 8 or Y < 0 or Y > 8:
    print('N')
else:
    print('S')
