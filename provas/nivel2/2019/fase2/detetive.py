# https://olimpiada.ic.unicamp.br/pratique/p2/2019/f2/detetive/

E, I, V = (int(i) for i in input().split())

conexoes = tuple(([], []) for i in range(E))

for _ in range(I):
    a, b = (int(i) - 1 for i in input().split())
    conexoes[a][1].append(b)  # adiciona b nas consequencias de a
    conexoes[b][0].append(a)  # adiciona a nas causas de b

ocorridos = [int(i) - 1 for i in input().split()]


# busca as causas iniciais dos eventos ocorridos
i = 0
while i < len(ocorridos):
    evento = ocorridos[i]
    causas = conexoes[evento][0]

    # enquanto o evento tiver apenas uma causa
    while len(causas) == 1:
        # atualiza o evento, a lista de ocorridos e as causas atuais
        evento = ocorridos[i] = causas[0]
        causas = conexoes[evento][0]

    # se o evento tiver mais de uma causa, busca uma causa em comum e adiciona na lista de ocorridos
    if len(causas) > 1:
        terminais = set()

        while causas:
            causa = causas.pop()
            super_causas = conexoes[causa][0]

            if super_causas:
                causas.extend(super_causas)

            else:
                terminais.add(causa)

        if len(terminais) == 1:
            evento = terminais.pop()

            if evento not in ocorridos:
                ocorridos.append(evento)

    i += 1

# percorre os eventos os eventos ocorridos de causa para consequencia
for evento in ocorridos:
    consequencias = conexoes[evento][1]
    ocorridos.extend(consequencias)

for i in sorted(set(ocorridos)):
    print(i + 1, end=' ')
print()

