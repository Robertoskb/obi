# https://olimpiada.ic.unicamp.br/pratique/ps/2014/f2/voo/

p_A, c_B, p_B, c_A = input().split()
# Dividindo em horas, minutos
p_A = [int(n) for n in p_A.split(":")]
c_B = [int(n) for n in c_B.split(":")]
p_B = [int(n) for n in p_B.split(":")]
c_A = [int(n) for n in c_A.split(":")]

# Transformando todos os horários em minutos
p_A = p_A[0]*60 + p_A[1]
c_B = c_B[0]*60 + c_B[1]
p_B = p_B[0]*60 + p_B[1]
c_A = c_A[0]*60 + c_A[1]

# Igualando os horários de partida
if p_A != p_B:
    tmp = p_B - p_A 
    p_B = p_A
    p_A -= tmp

dif = (c_B-c_A)//2
# Retirando a diferença dos horários do ponto B
c_B, p_B = c_B-dif, p_B-dif
dur = c_B - p_A
dif = dif//60

print(dur, dif)