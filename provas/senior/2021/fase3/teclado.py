teclado = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

cadeias = [teclado[int(i) - 2] for i in input()]
tam = len(cadeias)

cont = 0
for _ in range(int(input())):
    cadeia = input()
    if len(cadeia) == tam and all(c in l for c, l in zip(cadeia, cadeias)):
        # Se a cadeia tem o mesmo tanho do número
        # e cada caracter da cadeia está na lista de caracteres do seu número correspondente

        cont += 1

print(cont)
