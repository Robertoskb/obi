# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/pandemia/

n, m = (int(i) for i in input().split())
I, r = (int(i) for i in input().split())

infectados = {I}

for i in range(m):
    if i+1 >= r:
        _, *amigos = (int(i) for i in input().split())
        if any(infectado in amigos for infectado in infectados):
            for amigo in amigos:
                infectados.add(amigo)
    else:
        input()

print(len(infectados))
