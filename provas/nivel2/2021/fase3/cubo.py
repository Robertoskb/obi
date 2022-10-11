# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f3/cubo/

a = int(input())
b = int(input()) + 1

raiz_cubica = int(a**(1/3))
cubo = raiz_cubica ** 3

if cubo < a:
    raiz_cubica += 1
    cubo = raiz_cubica ** 3

cont = 0
while cubo < b:
    raiz_quadrada = int(cubo**0.5)
    quadrado = raiz_quadrada**2

    if quadrado == cubo:
        cont += 1

    raiz_cubica += 1
    cubo = raiz_cubica**3

print(cont)
