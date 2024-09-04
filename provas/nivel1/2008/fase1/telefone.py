# https://olimpiada.ic.unicamp.br/pratique/p1/2008/f1/telefone/

letras_numeros = {2: 'abc', 3: 'def', 4: 'ghi',
                  5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
identificador = {l.upper(): n for n, letras in letras_numeros.items()
                 for l in letras}

for i in range(0, 10):
    identificador[str(i)] = i

identificador['-'] = '-'

entrada = input()

saida = ''.join(str(identificador[l]) for l in entrada)
print(saida)
