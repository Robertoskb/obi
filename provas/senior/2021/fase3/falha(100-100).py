# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f3/falha/

# Eu encontrei este código no gabarito da prova, consiste em contar quantas strings são subcadeias de outras dada uma
# array de strings usando um dicionário como contador, se uma subcadeia das strings já está no dicionário, o seu valor
# será incrementado, se não, uma nova chave é adicionada com o valor 1, para poder ser incrementado posteriormente

n = int(input())
contador = {}
senhas = []

for _ in range(n):
    senha = input()
    senhas.append(senha)
    subcadeias = set()

    for j in range(len(senha)):
        corrente = ''
        for k in range(j, len(senha)):
            corrente += senha[k]
            subcadeias.add(corrente)

    for sub in subcadeias:
        if sub in contador.keys():
            contador[sub] += 1

        else:
            contador[sub] = 1

cont = -n
for senha in senhas:
    cont += contador[senha]

print(cont)
