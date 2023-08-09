# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/wifi/

class Evento:

    def __init__(self, x, yi, yf, tipo):
        self.x = x
        self.yi = yi
        self.yf = yf
        self.tipo = tipo  # 0 para abertura, 1 para fechamento

    def __lt__(self, other):  # possibilita o .sort() ordenar com base no x
        return self.x < other.x


N = int(input())

eventos = []
for _ in range(N):
    xi, yf, xf, yi = (int(i) for i in input().split())
    # canto inferior esquerdo (abertura): xi, yi
    # canto superior direito (fechamento): xf, yf
    eventos.append(Evento(xi, yi, yf, 0))
    eventos.append(Evento(xf, yi, yf, 1))

eventos.sort()

cont = 0
y_ocupados = dict()
for evento in eventos:
    if evento.tipo == 0:
        y_ocupados[evento.yi] = 0
        y_ocupados[evento.yf] = 1

    else:
        if y_ocupados[evento.yi] == 0:
            cont += 1

        y_ocupados_keys = sorted(y_ocupados.keys())
        index = y_ocupados_keys.index(evento.yi)

        anterior = y_ocupados_keys[index-1]
        y_ocupados[anterior] = 1

        y_ocupados.pop(evento.yi)
        y_ocupados.pop(evento.yf)


print(cont)
