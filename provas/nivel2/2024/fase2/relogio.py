# https://neps.academy/br/exercise/2713

H, M, S, T = (int(input()) for _ in range(4))
inicio = (H*60*60) + (M * 60) + S
final = inicio + T

M1, S1 = final // 60, final % 60
H1, M1 = M1 // 60, M1 % 60

if H1 > 23:
    H1 = H1 % 24

print(H1)
print(M1)
print(S1)