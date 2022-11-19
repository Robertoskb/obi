# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/passatempo/

L, C = (int(i) for i in input().split())

linhas = []
colunas = [[] for _ in range(C)]
soma_linhas = []
vars_ = {}

for _ in range(L):
    *variaveis, soma_linha = input().split()
    linhas.append(variaveis)
    soma_linhas.append(int(soma_linha))

    for i in range(C):
        colunas[i].append(variaveis[i])

    for v in variaveis:
        vars_[v] = v


soma_colunas = [int(i) for i in input().split()]


def passatempo():
    for linha in range(L):
        soma = soma_linhas[linha]
        divisor = C
        set_linhas = set()
        for l in linhas[linha]:
            if type(vars_[l]) == str:
                set_linhas.add(vars_[l])
            else:
                soma -= vars_[l]
                divisor -= 1

        if len(set_linhas) == 1:
            vars_[set_linhas.pop()] = soma // divisor

    for coluna in range(C):
        soma = soma_colunas[coluna]
        divisor = L
        set_colunas = set()
        for c in colunas[coluna]:
            if type(vars_[c]) == str:
                set_colunas.add(vars_[c])
            else:
                soma -= vars_[c]
                divisor -= 1

        if len(set_colunas) == 1:
            vars_[set_colunas.pop()] = soma // divisor


while any(type(i) == str for i in vars_.values()):
    passatempo()

for k, v in sorted(vars_.items()):
    print(k, v)
