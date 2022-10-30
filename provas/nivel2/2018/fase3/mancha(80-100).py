# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f3/mancha/

N = int(input())

matriz = [input() for _ in range(N)]

for i in range(N):
    pele = mancha = False
    for j in range(N):
        if pele and mancha:
            print('N')
            break
        if matriz[i][j] == '*':
            mancha = True

        elif mancha:
            pele = True
            mancha = False

    else:
        continue

    break

else:
    for i in range(N):
        pele = mancha = False
        for j in range(N):
            if pele and mancha:
                print('N')
                break
            if matriz[j][i] == '*':
                mancha = True

            elif mancha:
                pele = True
                mancha = False

        else:
            continue

        break
    else:
        print('S')
