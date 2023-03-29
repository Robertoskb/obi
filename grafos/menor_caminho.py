# esse algorítimo serve para calcular o menor caminho/custo em um grafo

from queue import PriorityQueue

N, M = (int(i) for i in input().split()) # N = número de adjacentes, M = número de arestas

cidades = [[] for _ in range(N)] # prepara lista de adjacentes, cada sublista representa a lista de destinos de uma cidade

custos = [float('inf') for _ in range(N)] # vai armazenar o custo mínimo de cada cidade, inicialmente o custo é infinito

marcados = [False for _ in range(N)] # vai marcar as cidades não visitadas como False e visitadas como True

for _ in range(M):
    A, B, C = (int(i) for i in input().split()) # o custo para sair da cidade A para B é C
    cidades[A].append((B, C))
    # adiciona uma tupla na lista de destinos da cidade A, indicando index da cidade destino e o custo
    # a lista de adjacentes ficará dessa forma: [..., [(B, C), ...], ...]
    
    
    cidades[B].append((A, C)) # caso o grafo não tenha direção, ou seja, caso seja possível ir de A para B e de B para A


# sendo a cidade 0 o ponto de partida e a cidade N o desto, segue o código

custos[0] = 0 # o custo para chegar até a cidade 0 é 0

pilha = PriorityQueue() # inicia a pilha

pilha.put((0, 0)) # adiciona o index primeira cidade (0) e o custo inicial (0)

while not pilha.empty(): # enquanto tiver cinades para visitar
    acm, cidade = pilha.get() # pega o custo acumulado para ir até a cidade do top da pilha

    if marcados[cidade]: # se a cidade já foi visitada, pula para a próxima
        continue

    marcados[cidade] = True # marca cidade como visitada

    for destino, custo in cidades[cidade]: # percorre a lista de destinos da cidade
        # novo custo está mais relacionado com valor acumulado do que com custo de A -> B 
    
        novo_custo = acm + custo # calcula o novo valor acumulado
        
        if marcados[destino]: # se o destino já foi visitado, pula para o próximo
            continue
        
        if custos[destino] > novo_custo: # se o novo custo for menor que o atual
            custos[destino] = novo_custo # atualiza o custo do destino
            pilha.put((novo_custo, destino)) # adiciona o destino na pilha com o novo custo e destino


print(custos[N-1]) # imprime o menor custo para chegar na cidade N partindo da cidade 0

# Resumo (ChatGPT):

# 1 - Usar uma lista de adjacência para armazenar as conexões entre os vértices do grafo e seus respectivos pesos.
# 2 - Usar duas listas para armazenar o custo mínimo para chegar a cada vértice e se um vértice foi visitado ou não.
# 3 - Usar uma fila de prioridade (PriorityQueue) para visitar os vértices com menor custo primeiro.
# 4 - Ao visitar um vértice, atualizar os custos mínimos para os vértices adjacentes se o custo atual for menor do que o custo armazenado anteriormente.
# 5 - Marcar um vértice como visitado para evitar loops infinitos.
# 6 - Continuar o loop enquanto houver vértices na fila de prioridade