#https://olimpiada.ic.unicamp.br/static/extras/obi2023/provas/ProvaOBI2023_f1p1.pdf

estoque = [[int(x) for x in input().split()] for _ in range(int(input().split()[0]))]

total = 0

for pedido in [[int(x) for x in input().split()] for _ in range(int(input()))]:
    if estoque[pedido[0] - 1][pedido[1] - 1] > 0:
        total += 1
        estoque[pedido[0] - 1][pedido[1] - 1] -= 1

print(total)
