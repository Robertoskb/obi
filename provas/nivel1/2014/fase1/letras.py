# https://olimpiada.ic.unicamp.br/pratique/p1/2014/f1/letra/

letra = input()
palavras = input().split()
porcentagem = sum(
    [1 for palavra in palavras if letra in palavra]) / len(palavras) * 100
print(f'{porcentagem:.1f}')
