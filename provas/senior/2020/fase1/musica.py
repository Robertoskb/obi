# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/musica/ 

from collections import defaultdict

INF = float('inf')

N, M, C = (int(n) for n in input().split()) # n.amigos, n.musicas, musica compartilhada
musicas_detestadas = defaultdict(lambda: INF) # [n] => amigo mais antigo que detesta a música 'n'
amigos = defaultdict(int) # [n] => música amada do amigo 'n'
trocas = 0 

for a in range(N):
    A, D = (int(n) for n in input().split())
    amigos[a] = A
    
    msc = musicas_detestadas[D]
    if msc > a: # Define o amigo mais antigo (o de menor índice)
        musicas_detestadas[D] = a

tmp = defaultdict(bool) # [n] => a musica já foi trocada?
while True:
    if tmp[C]:
        trocas = -1 # O ciclo será infinito
        break
    
    tmp[C] = True
    
    amigo = musicas_detestadas[C] # amigo mais antigo que detesta a música 'C'
    if amigo != INF: 
        C = amigos[amigo]
        trocas += 1
    else: # Se a música não for detestada por alguém
        break
    
print(trocas)
