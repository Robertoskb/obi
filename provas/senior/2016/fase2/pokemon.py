# https://olimpiada.ic.unicamp.br/pratique/ps/2016/f2/pokemon/

n = int(input())
pokemons = [int(input()) for _ in range(3)]
pokemons.sort()

cont = 0
for p in pokemons:
    if n >= p:
        n -= p
        cont += 1

print(cont)
