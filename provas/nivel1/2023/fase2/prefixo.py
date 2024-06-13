# https://neps.academy/br/exercise/2437

N, Pi = int(input()), input()
M, Si  = int(input()), input()

resultado = 0

for i in range(min(N, M)):
    if Pi[i] == Si[i]:
        resultado += 1
    else:
        break

print(resultado)
