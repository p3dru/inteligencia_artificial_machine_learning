## Capítulo 1 (entendendo problemas):

### Componentes de um problema:
  - Estado Inicial
  - Estado final (objetivo)
  - Espaço de estados (Todos os caminhos possíveis para resolver o resultado)
  - Ações para passar de um estado para outro (Passos bem definidos de cada caminho)
  - Solução (caminho que leva do estado inicial ao final)

### Conceitos Relacionados:
  - _*Heuristica:*_ É um método/processo criado com o objetivo de encontrar soluções mais simples para um problema difícil, mesmo que o resultado gere respostas imperfeitas. São técnicas que indicam escolhas que a máquina deve priorizar, técnicas de ajuda em uma descoberta. Soluções de “menor custo” devem ser priorizadas. Nem sempre uma heurística vai funcionar, ela é apenas uma maneira para descobrir o problema.
  - _*Vetores Ordenados:*_ São basicamente "listas" ordenadas por algum atributo. 
  - _*Big - O:*_ Notação matemática usada para descrever o comportamento limite de uma função à medida que o argumento tende a um valor específico ou ao infinito. É utilizado para analisar a complexidade de tempo ou espaço de um algoritmo, indicando como o tempo de execução ou os requisitos de espaço crescem à medida que o tamanho da entrada aumenta.
      - O(1): Complexidade constante. O tempo de execução ou o espaço necessário não muda com o tamanho da entrada. Exemplo: Acessar um elemento em um array por index.
      - O(log n): Complexidade logarítmica. O tempo de execução ou o espaço necessário cresce logaritmicamente com o tamanho da entrada. Exemplo: Busca binária em arrays/listas ordenados(as).
      - O(n): Complexidade linear. O tempo de execução ou o espaço necessário cresce linearmente com o tamanho da entrada. Exemplo: Percorrer um array ou lista.
      - O(n log n): Complexidade logarítmica linear. O tempo de execução ou o espaço necessário cresce linearmente com o logaritmo do tamanho da entrada. Exemplo: Merge sort ou Heapsort.
      - O(n²): Complexidade quadrática. O tempo de execução ou o espaço necessário cresce com o quadrado do tamanho da entrada. Exemplo: Bubble sort.
      - O(2^n): Complexidade exponencial. O tempo de execução ou o espaço necessário cresce exponencialmente com o tamanho da entrada. Exemplo: Resolução do problema "caixeiro-viajante" por força bruta.
  - _*Busca Gulosa:*_ É uma estratégia de resolução de problemas que faz a escolha que parece ser a melhor no momento, sem considerar consequências futuras. É um algoritmo de otimização e de busca de caminhos, onde encontra uma boa solução para o problema de forma eficiente/rápida, sem garantir que a solução encontrada seja a melhor possível. No exemplo, descrevemos como boa solução, seguir pelo caminho com menor distância até o objetivo.
  - _*Busca A* (estrela):*_ É uma estratégia que combina busca gulosa com heurística (link eurística) para encontrar o caminho mais curto entre dois pontos em um grafo/espaço. Estimando o custo do caminho mais curto de um nó (vértice) até o destino, explorando os nós com menor custo encontrado (estimado). A heurística desse problema é a distância real entre as cidades (colocados nas linhas).

### Problema base:
Encontrar a rota de menor custo, partindo de Arad até Bucharest.
![Problema arad-bucharest](https://slideplayer.com.br/slide/2296557/8/images/6/Rom%C3%AAnia%3A+ir+de+Arad+a+Bucharest.jpg)

[Resolução com Busca Gulosa](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20busca/gulosa.py) <br>
[Resolução com Busca A*](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20busca/busca_a_estrela.py)

### Exercício proposto:
Encontrar uma rota de menor custo, partindo da cidade de Porto União até Curitiba.

[Resolução do exercício](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20busca/exercicio.py)

#

## Chapter 1 (understanding problems):

### Components of a problem:
  - Initial State
  - End state (goal)
  - State space (All possible paths to resolve the result)
  - Actions to move from one state to another (well-defined steps on each path)
  - Solution (path that leads from the initial state to the end)

### Related Concepts:
  - _*Heuristics:*_ It is a method/process created with the aim of finding simpler solutions to a difficult problem, even if the result generates imperfect answers. These are techniques that indicate choices that the machine should prioritize, techniques that help with a discovery. “Least cost” solutions should be prioritized. A heuristic will not always work, it is just a way to discover the problem.
  - _*Ordered Vectors:*_ They are basically "lists" ordered by some attribute.
  - _*Big - O:*_ Mathematical notation used to describe the limiting behavior of a function as the argument tends to a specific value or to infinity. It is used to analyze the time or space complexity of an algorithm, indicating how the execution time or space requirements grow as the input size increases.
      - O(1): Constant complexity. The execution time or space required does not change with the size of the input. Example: Access an element in an array by index.
      - O(log n): Logarithmic complexity. The execution time or space required grows logarithmically with the size of the input. Example: Binary search in ordered arrays/lists.
      - O(n): Linear complexity. The execution time or space required grows linearly with the size of the input. Example: Traverse an array or list.
      - O(n log n): Linear logarithmic complexity. The execution time or space required grows linearly with the logarithm of the input size. Example: Merge sort or Heapsort.
      - O(n²): Quadratic complexity. The execution time or space required grows as the square of the input size. Example: Bubble sort.
      - O(2^n): Exponential complexity. The execution time or space required grows exponentially with the size of the input. Example: Solving the "travelling salesman" problem by brute force.
  - _*Greedy Search:*_ It is a problem-solving strategy that makes the choice that seems to be the best at the moment, without considering future consequences. It is an optimization and path search algorithm, where it finds a good solution to the problem efficiently/quickly, without guaranteeing that the solution found is the best possible. In the example, we describe a good solution as following the path with the shortest distance to the objective.
  - _*Search A* (star):*_ It is a strategy that combines greedy search with heuristics (euristic link) to find the shortest path between two points in a graph/space. Estimating the cost of the shortest path from a node (vertex) to the destination, exploring the nodes with the lowest cost found (estimated). The heuristic of this problem is the real distance between cities (placed on the lines).

### Base problem:
Find the lowest cost route from Arad to Bucharest.
![Problema arad-bucharest](https://slideplayer.com.br/slide/2296557/8/images/6/Rom%C3%AAnia%3A+ir+de+Arad+a+Bucharest.jpg)

[Resolution with Greedy Search](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20busca/gulosa.py) <br>
[Resolution with A* Search](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algorithmos%20de%20busca/busca_a_estar.py)

### Proposed exercise:
Find a lower cost route, leaving from the city of Porto União to Curitiba.

[Exercise resolution](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20busca/exercicio.py)
