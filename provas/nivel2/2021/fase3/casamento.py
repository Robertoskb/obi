# https://olimpiada.ic.unicamp.br/pratique/p2/2021/f3/casamento/

def casamento(A, B):
    new_a = ''
    new_b = ''

    for ca, cb in zip(A, B):
        if ca >= cb:
            new_a += ca
        if cb >= ca:
            new_b += cb

    return new_a or '-1', new_b or '-1'


a = input()
b = input()

a = ('0'*(len(b)-len(a))) + a
b = ('0'*(len(a)-len(b))) + b

resp = map(int, casamento(a, b))
print(*sorted(resp))
