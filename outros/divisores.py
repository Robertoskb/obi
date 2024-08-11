# Os divisores de um número n são os números que dividem n sem deixar resto.
# O número 1 é divisor de qualquer número.
# O número n é divisor de n.
# Se n = a * b, então a e b são divisores de n.
# Se a é divisor de n, então n // a é divisor de n.
# O número de divisores de n é no máximo O(sqrt(n)).
# O(sqrt(n)) é a raiz quadrada de n.

def divisores(n):
    divisores = [1]

    i = 2
    while i * i <= n:  # O(sqrt(n))
        if n % i == 0:
            divisores.append(i)
            divisores.append(n // i)

        i += 1

    divisores.append(n)

    return divisores
