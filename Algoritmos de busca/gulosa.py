'''
cria uma classe Vertice que possui um nome (rotulo), visitado (se passarmos 
por esse vertice), distancia_objetivo (é a distância em linha reta até o 
objetivo) e adjacentes são as cidades vizinhas (vértices vizinhos)
'''
class Vertice:
  #construtores de vértice com o rotulo e a distância em linha reta até o objetivo
  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    #informa se o vértice foi visitado ou não, para não haver duplicação de caminhos
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  #função para tornar um vertice como adjacente de outro
  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  #função que mostra todos os adjacentes
  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

#cria uma classe Adjacente para salvar um vértice (cidade) e o custo dele até o objetivo (Bucharest)
class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

#classe grafo que cria a estrutura semelhante à apresentada na imagem
class Grafo:
  #cria os vértices
  arad = Vertice('Arad', 366)
  zerind = Vertice('Zerind', 374)
  oradea = Vertice('Oradea', 380)
  sibiu = Vertice('Sibiu', 253)
  timisoara = Vertice('Timisoara', 329)
  lugoj = Vertice('Lugoj', 244)
  mehadia = Vertice('Mehadia', 241)
  dobreta = Vertice('Dobreta', 242)
  craiova = Vertice('Craiova', 160)
  rimnicu = Vertice('Rimnicu', 193)
  fagaras = Vertice('Fagaras', 178)
  pitesti = Vertice('Pitesti', 98)
  bucharest = Vertice('Bucharest', 0)
  giurgiu = Vertice('Giurgiu', 77)

  #adiciona seus vértices vizinhos
  arad.adiciona_adjacente(Adjacente(zerind, 75))
  arad.adiciona_adjacente(Adjacente(sibiu, 140))
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

#cria uma instância da classe grafo
grafo = Grafo()

import numpy as np
class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    #mudança no tipo de dados, antes int, agora object, pois salvaremos vertices no vetor (que são objetos)
    self.valores = np.empty(self.capacidade, dtype=object)

  #insere novos vertices no vetor de forma ordenada (de acordo com a distância até a cidade objetivo)
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      #se a distância até a cidade objetivo (bucharest) for maior do que a distância do vertice
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
        #para de procurar
        break
      #se percorreu até o último item, a nova posição é a final (i + 1)
      if i == self.ultima_posicao:
        posicao = i + 1
    #x recebe a última posição do vetor
    x = self.ultima_posicao
    #enquanto x for maior ou iguar que a posição do vetor, desloque todos os valores uma casa à frente
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      #decremente x em 1
      x -= 1
    #assim que sair do while, atribua o vértice à sua posição ordenada
    self.valores[posicao] = vertice
    #incremente a posição final do vetor
    self.ultima_posicao += 1

  #classe que imprime todas as cidades e suas distâncias até a cidade objetivo
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

#cria um vetor ordenado com tamanho 5 e insere as cidades vizinhas (vertices vizinhos)
vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)

#imprime todos os adicionados
vetor.imprime()

vetor.insere(grafo.lugoj)
vetor.imprime()

#apenas acessa atributos direto do vetor, informando seu espaço de memória e o nome
vetor.valores[0], vetor.valores[0].rotulo

#classe implementando a busca gulosa que sempre busca pela menor distância até a cidade objetivo
class Gulosa:
  #inicia o construtor com sua própria instância e o objetivo a ser alcançado
  def __init__(self, objetivo):
    self.objetivo = objetivo
    #atributo para identificar se ele foi encontrado ou não
    self.encontrado = False

  #função de busca
  def buscar(self, atual):
    print('-------')
    print('Atual: {}'.format(atual.rotulo))
    #altera o valor para informar que ele foi visitado
    atual.visitado = True

    #se a cidade objetivo for encontrada, altere o valor para True
    if atual == self.objetivo:
      self.encontrado = True
    #se não
    else:
      #ordena-se um novo vetor ordenado do tamanho das cidades adjacentes da cidade atual (vertices)
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      #para cada adjacente, altere as características para visitado
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado == True
          #insira o vértice para serem ordenados em uma lista de vetores ordenados
          vetor_ordenado.insere(adjacente.vertice)
      #imprima-os ao final
      vetor_ordenado.imprime()

      #se o vetor for diferente de None, faça a busca recursiva
      #como a lista é ordenada pela distância até o objetivo, pesquisando por
      #[0], garante que o valor selecionado seja o que possui a menos distância 
      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0])


#instancia-se a classe, definindo o objetivo a ser encontrado
busca_gulosa = Gulosa(grafo.bucharest)
#inicia a busca em Arad (cidade inicial)
busca_gulosa.buscar(grafo.arad)