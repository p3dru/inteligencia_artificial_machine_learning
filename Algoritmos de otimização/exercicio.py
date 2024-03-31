import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

#lista de produtos com o nome, espaço em m3 e o preço
produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]
#espacço disponível em m3
espaco_disponivel = 3

#acessa os produtos e suas particularidades
produtos[0], produtos[0][0], produtos[0][1], produtos[0][2]

#imprime o produto selecionado (0 e 1) e se for = 1 exiba
def imprimir_solucao(solucao):
  for i in range(len(solucao)):
    if solucao[i] == 1:
      print('%s - %s' % (produtos[i][0], produtos[i][2]))

#cada 0 e 1 aqui, representa um produto, 0 significa não levar e 1, levar
imprimir_solucao([0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])

#cria uma função fitness
def fitness_function(solucao):
  #inicializa o custo em 0
  custo = 0
  #a soma dos espaços também = 0
  soma_espaco = 0
  #para cada item selecionado com 1, incremente o custo e o espaço
  for i in range(len(solucao)):
    if solucao[i] == 1:
      custo += produtos[i][2]
      soma_espaco += produtos[i][1]
  #se ultrapassar o espaço disponível, esse é o pior cenário possível, então retorna 1
  if soma_espaco > espaco_disponivel:
    #usa pra descartar
    custo = 1
  #retorna o custo total
  return custo

fitness_function([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])

#passamos a fitness function para o algoritmo
fitness = mlrose.CustomFitness(fitness_function)

#definimos o problema, passando o tamanho das variáveis a serem consideradas
#length = quantidade de produtos
#fitness_fn = é a função fitnessa a ser utilizada
#maximize = True pois é um problema de maximização (queremos o maior valor possível)
#max_val = 2 pois só queremos definir o intervalo entre 0 e 1
problema = mlrose.DiscreteOpt(length = 14, fitness_fn = fitness,
                             maximize = True, max_val = 2)

#implementação hill climb
melhor_solucao, melhor_custo = mlrose.hill_climb(problema)
melhor_solucao, melhor_custo

print("Implementação Hill Climb")
imprimir_solucao(melhor_solucao)
print()

#implementação simulated annealing
melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema)
melhor_solucao, melhor_custo

print('implementação Simulated Annealing')
imprimir_solucao(melhor_solucao)
print()

#implementação algoritmo genético
#passamos o problema
#o tamanho da população que é a quantidade de soluções a serem consideradas
#e a probabilidade de mutação é a introdução de pequenas alterações aleatórias em soluções para garantir a diversidade na população e evitar quedas em ótimos locais
melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
melhor_solucao, melhor_custo

print('implementação Algoritmo Genético')
imprimir_solucao(melhor_solucao)
print()