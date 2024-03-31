## Capítulo 2 (Algoritmos de otimização):

### Conceitos:
  - _*Algoritmos de otimização:*_ São técnicas computacionais usadas para encontrar a melhor solução possível para um problema de otimização. São projetados para resolver problemas objetivando a maximização ou minimização de algo (reduzir custos ou maximizar lucros).
  - _*Metaheurísticas:*_ Técnicas de alto nível usadas para resolver problemas de otimização que são difíceis de serem resolvidos diretamente por algoritmos de otimização tradicionais. funcionam como um “guia” para encontrar soluções ótimas e genéricas, mas não garantem soluções exatas. Semelhante à heurística tradicional.
  - _*Fitness function:*_ Medida usada em algoritmos de otimização e metaheurísticas para avaliar o quão boa é uma solução para um problema. Ela quantifica a qualidade da solução em relação à um objetivo que se deseja alcançar. Ela ajuda a determinar se uma solução é melhor do que outra, permitindo que o algoritmo escolha a melhor solução entre as disponíveis.
  - _*Hill Climb:*_  Algoritmo simples de busca local para encontrar a solução de um problema de otimização, tem como objetivo "descer" ou "subir" a "colina", até que não haja mais melhorias possíveis. No entanto, pode ficar preso à máximos ou mínimos locais, o que siginifica que pode parar em uma solução que não é a mlehor possível, mas é a melhor em relação às soluções vizinhas. Funciona assim:
    - Início: Começa com uma solução apresentada inicialmente (início da colina);
    - Avaliação: Avalia a qualidade da solução atual usando uma função de aptidão (fitness function);
    - Melhoria: Explora as soluções vizinhas (que são pequenas mudanças na solução atual) e escolhe a que tem melhor avaliação de aptidão;
    - Repetição: Repete o processo de avaliação e melhoria até que não seja possível encontrar uma solução melhor;
  - _*Simuladed annealing:*_ Tende a ser melhor que o hill climb, é um algoritmo de otimização que usa a ideia de annealing (refinamento) em metais para encontrar soluções ótimas para problemas de otimização. É eficiente para encontrar soluções ótimas em problemas complexos onde a busca gulosa pode ficar presa em mínimos locais, pois permite explorar o espaço de soluções de forma mais eficaz. Funciona da seguinte forma:
    - Início: Começa com uma solução inicial.
    - Avaliação: Avalia a qualidade da solução atual usando uma função de aptidão.
    - Melhoria: Explora as soluções vizinhas e escolhe uma nova solução, mesmo que não seja melhor, com uma probabilidade que diminui com o tempo ou com base em uma função de aceitação.
    - Temperatura: A "temperatura" controla a probabilidade de aceitar soluções piores. Inicialmente, é alta, permitindo aceitar soluções ruins para explorar o espaço de soluções. Com o tempo, a temperatura diminui, tornando mais difícil aceitar soluções piores, o que ajuda a evitar ficar preso em mínimos locais.
    - Repetição: Repete o processo de avaliação, melhoria e ajuste da temperatura até que o algoritmo decida parar, geralmente quando a temperatura atinge um valor mínimo ou após um número específico de iterações.
  - _*Algoritmo Genético:*_ Técnica de orimização inspirada na evolução natural e na genética. É conhecido por sua capacidade de explorar um amplo espaço de soluções e encontrar boas soluções em problemas complexos, onde outras técnicas podem falhar. Funciona da seguinte forma:
    - População Inicial: Gera uma população inicial de soluções candidatas. Cada solução é representada como um "indivíduo" ou "cromossomo", que é uma sequência de genes.
    - Avaliação: Avalia a qualidade de cada solução na população usando uma função de aptidão.
    - Seleção: Seleciona soluções para reprodução com base em sua aptidão. Soluções com melhor aptidão têm maior probabilidade de serem selecionadas.
    - Crossover (Recombinação): Combina partes de duas soluções selecionadas para criar novas soluções. Isso é feito de forma a preservar os aspectos úteis de ambas as soluções.
    - Mutação: Introduz pequenas alterações aleatórias em algumas soluções para garantir a diversidade na população e evitar quedas em ótimos locais.
    - Substituição: Substitui soluções na população por novas soluções geradas através do crossover e mutação.
    - Repetição: Repete os passos de avaliação, seleção, crossover, mutação e substituição até que uma condição de parada seja atingida, como um número máximo de gerações ou uma solução com aptidão suficientemente alta.
    > Conceitos relacionados à algoritmos genéticos:
    > - População: O conjunto de soluções candidatas que estão sendo avaliadas e evoluídas.
    > - Indivíduo/Cromossomo: Uma solução candidata na população. Cada indivíduo é representado como uma sequência de genes.
    > - Gene: Um componente individual de uma solução. Em muitos problemas, um gene pode representar um elemento específico da solução, como um ponto em um problema de roteirização.
    > - Aptidão (Fitness): Uma medida de quão boa é uma solução candidata. Soluções com melhor aptidão são preferidas durante a seleção e a substituição na população.
    > - Seleção: O processo de escolher soluções para reprodução com base em sua aptidão. Soluções com melhor aptidão têm maior probabilidade de serem selecionadas.
    > - Crossover (Recombinação): O processo de combinar partes de duas soluções selecionadas para criar novas soluções. Isso ajuda a preservar os aspectos úteis de ambas as soluções e introduzir novas combinações.
    > - Mutação: A introdução de pequenas alterações aleatórias em soluções para garantir a diversidade na população e evitar quedas em ótimos locais.
    > - Elitismo: A prática de preservar as melhores soluções de uma geração para a próxima, garantindo que a qualidade geral da população não diminua.
    > - Geração: Um ciclo completo de avaliação, seleção, crossover, mutação e substituição na população.
    > - Fitness Function: A função usada para avaliar a qualidade de uma solução candidata.
    > - Genoma: A sequência completa de genes que compõem uma solução.


### Problema base:
Descobrir quais produtos levar em um caminhão com 3 metros cúbicos de volume, levando em consideração o tamanho e o valor de cada produto, sendo que o espaço não pode ultrapassar os espaço do caminhão.

[Resolução do exercício](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20otimização/exercicio.py)

# 
## Chapter 2 (Optimization Algorithms):

### Concepts:
  - _*Optimization algorithms:*_ These are computational techniques used to find the best possible solution to an optimization problem. They are designed to solve problems aiming to maximize or minimize something (reduce costs or maximize profits).
  - _*Metaheuristics:*_ High-level techniques used to solve optimization problems that are difficult to be solved directly by traditional optimization algorithms. they function as a “guide” to find optimal and generic solutions, but do not guarantee exact solutions. Similar to traditional heuristics.
  - _*Fitness function:*_ Measure used in optimization algorithms and metaheuristics to evaluate how good a solution is to a problem. It quantifies the quality of the solution in relation to the objective you want to achieve. It helps determine whether one solution is better than another, allowing the algorithm to choose the best solution from those available.
  - _*Hill Climb:*_ Simple local search algorithm to find the solution to an optimization problem, its objective is to "go down" or "up" the "hill", until there are no more improvements possible. However, you can get stuck at local maxima or minima, which means you can end up at a solution that is not the best possible, but is the best in relation to neighboring solutions. It works like this:
    - Start: Starts with a solution initially presented (start of the hill);
    - Evaluation: Evaluates the quality of the current solution using a fitness function;
    - Improvement: Explore neighboring solutions (which are small changes to the current solution) and choose the one with the best fitness assessment;
    - Repetition: Repeat the evaluation and improvement process until a better solution cannot be found;
  - _*Simulated annealing:*_ Tends to be better than hill climb, it is an optimization algorithm that uses the idea of ​​annealing (refinement) in metals to find optimal solutions to optimization problems. It is efficient for finding optimal solutions in complex problems where greedy search can get stuck in local minima, as it allows exploring the solution space more effectively. It works as follows:
    - Start: Starts with an initial solution.
    - Evaluation: Evaluates the quality of the current solution using a fitness function.
    - Improvement: Explores neighboring solutions and chooses a new solution, even if it is not better, with a probability that decreases over time or based on an acceptance function.
    - Temperature: "Temperature" controls the probability of accepting worse solutions. Initially, it is high, allowing you to accept bad solutions to explore the solution space. Over time, the temperature decreases, making it harder to accept worse solutions, which helps avoid getting stuck in local minima.
    - Repetition: Repeats the process of evaluating, improving and adjusting the temperature until the algorithm decides to stop, usually when the temperature reaches a minimum value or after a specific number of iterations.
  - _*Genetic Algorithm:*_ Orimization technique inspired by natural evolution and genetics. It is known for its ability to explore a wide solution space and find good solutions in complex problems where other techniques may fail. It works as follows:
    - Initial Population: Generates an initial population of candidate solutions. Each solution is represented as an "individual" or "chromosome", which is a sequence of genes.
    - Evaluation: Evaluates the quality of each solution in the population using a fitness function.
    - Selection: Selects solutions for reproduction based on their aptitude. Solutions with better fitness are more likely to be selected.
    - Crossover: Combines parts of two selected solutions to create new solutions. This is done in order to preserve the useful aspects of both solutions.
    - Mutation: Introduces small random changes to some solutions to ensure diversity in the population and avoid falling into local optima.
    - Replacement: Replaces solutions in the population with new solutions generated through crossover and mutation.
    - Repetition: Repeats the evaluation, selection, crossover, mutation and replacement steps until a stopping condition is reached, such as a maximum number of generations or a solution with sufficiently high fitness.
    > Concepts related to genetic algorithms:
    > - Population: The set of candidate solutions that are being evaluated and evolved.
    > - Individual/Chromosome: A candidate solution in the population. Each individual is represented as a sequence of genes.
    > - Gene: An individual component of a solution. In many problems, a gene can represent a specific element of the solution, such as a point in a routing problem.
    > - Fitness: A measure of how good a candidate solution is. Solutions with better fitness are preferred during selection and replacement in the population.
    > - Selection: The process of choosing solutions for breeding based on their suitability. Solutions with better fitness are more likely to be selected.
    > - Crossover (Recombination): The process of combining parts of two selected solutions to create new solutions. This helps preserve the useful aspects of both solutions and introduce new combinations.
    > - Mutation: The introduction of small random changes in solutions to ensure diversity in the population and avoid falling into local optima.
    > - Elitism: The practice of preserving the best solutions from one generation to the next, ensuring that the overall quality of the population does not decline.
    > - Generation: A complete cycle of evaluation, selection, crossover, mutation and replacement in the population.
    > - Fitness Function: The function used to evaluate the quality of a candidate solution.
    > - Genome: The complete sequence of genes that make up a solution.
      
        
    
### Base problem:
Find out which products to carry in a truck with 3 cubic meters in volume, taking into account the size and value of each product, and the space cannot exceed the truck's space.

[Exercise resolution](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/Algoritmos%20de%20otimização/exercicio.py)
