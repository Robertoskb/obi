# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

deck = {'C': [], 'E': [], 'U': [], 'P': []}

entrada = input()

for i in range(0, len(entrada), 3):
    deck[entrada[i+2]].append(entrada[i:i+3])

for cartas in deck.values():
    if any(cartas.count(c) > 1 for c in cartas):
        print('erro')
    else:
        print(13-len(cartas))
