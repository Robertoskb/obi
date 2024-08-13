# https://neps.academy/br/exercise/2622

class Horario:
    def __init__(self, onibus, tempo, tipo):
        self.onibus = onibus
        self.tempo = tempo
        self.tipo = tipo


n = int(input())

horarios = []
for i in range(n):
    c, p = (int(i) for i in input().split())
    horarios.append(Horario(i, c, 'c'))
    horarios.append(Horario(i, p, 'p'))

vagas = 1

# ordena por tempo e prioridade para onibus chegando em caso de empate entre onibus chegando e partindo
horarios.sort(key=lambda x: (x.tempo, x.tipo == 'c'))
max_ = 1
cont = 1

# se os horarios ficarem cpcpcp, o maximo de onibus estacionados ao mesmo tempo foi 1
# se os horarios ficarem ccpp, o maximo de onibus estacionados ao mesmo tempo foi 2
# se os hararios ficarem ccpccppp, o maximo de onibus estacionados ao mesmo tempo foi 3

for h in horarios[1:]:
    if h.tipo == 'p':
        cont -= 1
    else:
        cont += 1
        max_ = max(max_, cont)

print(max_ * 20)
