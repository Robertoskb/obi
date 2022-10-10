# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/

alfabeto = 'abcdefghijklmnopqrstuvxz'  # sim, não existe o 'w' nessa questão (?)
alfabetozz = 'bcdfghjklmnpqrstvxzz'  # sem as vogais e com "zz"
vogais = 'aeiou'


def vogal_prox(consoante):
    index_consoante = alfabeto.index(consoante)

    def distancia(vogal):
        return abs(index_consoante - alfabeto.index(vogal))  # distancia absoluta entre a vogal e a consoante

    return min(vogais, key=distancia)  # menor vogal com base na distancia, ou seja, a mais próxima


def substituir(caractere):
    if caractere in vogais:
        return caractere

    index = alfabetozz.index(caractere)
    return caractere + vogal_prox(caractere) + alfabetozz[index + 1]


p = input()
cifra = ''

for c in p:
    cifra += substituir(c)

print(cifra)
