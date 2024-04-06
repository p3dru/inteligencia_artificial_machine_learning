## Capítulo 7: Associação

### Conceito:
É uma técnica de mineração de dados que busca encontrar relações (que podem ser de interesse) entre diferentes itens em um conjunto de dados. Essas relações podem ser usadas para fazer recomendações, identificar padrões de compra, analisar dados, entre outros. É particularmente útil em aplicações de marketing, onde o objetivo é descobrir quais itens são frequentemente comprados juntos e em sistemas de recomendação.

### Técnicas mais utilizadas:
#### Apriori:
Usa um algoritmo de busca em profundidade para encontrar conjuntos de itens que são frequentemente comprados juntos. Baseia-se na ideia de que, se um conjunto de itens é frequentemente comprado juntos, então qualquer subconjunto desse conjunto também deve ser frequentemente comprado juntos.<br>
Como funciona:
 - Geração de candidatos: Inicialmente, o algoritmo gera conjuntos de um item (frequentemente chamados de "1-itemsets"). Em seguida, gera conjuntos de dois itens que são frequentemente comprados juntos (2-itemsets), e assim por diante.
 - Verificação de Suporte: Para cada conjunto gerado, o algoritmo verifica se o conjunto é frequentemente comprado juntos, ou seja, se a frequência do conjunto é maior ou igual a um limiar de suporte pré-definido.
 - Geração de Conjuntos Frequentes: Se um conjunto é frequentemente comprado juntos, ele é adicionado à lista de conjuntos frequentes. O algoritmo então gera conjuntos de tamanho maior com base nos conjuntos frequentes encontrados até agora.
 - Iteração: O processo de geração de candidatos, verificação de suporte e geração de conjuntos frequentes é repetido até que nenhum novo conjunto frequente seja encontrado.

> Vantagens:
> - Simplicidade e facilidade de implementação.
> - Ser capaz de encontrar todos os conjuntos frequentes em um conjunto de dados.
>
> Desvantagens:
> - Pode ser ineficiente em termos de tempo e memória, especialmente para conjuntos de dados grandes, devido à geração de todos os conjuntos de tamanho k antes de gerar os conjuntos de tamanho k + 1.

[Implementação Apriori](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/apriori.py)

#### Eclat:
Se baseia na ideia de que, se um conjunto de itens é frequentemente comprado juntos, então qualquer subconjunto desse conjunto também deve ser frequentemente comprado juntos.<br>
Como funciona:
 - Geração de Candidatos: Assim como o Apriori, o Eclat começa gerando conjuntos de um item. Em seguida, gera conjuntos de dois itens que são frequentemente comprados juntos, e assim por diante.
 - Verificação de Suporte: Para cada conjunto gerado, o algoritmo verifica se o conjunto é frequentemente comprado juntos, usando a mesma lógica de suporte que o Apriori.
 - Geração de Conjuntos Frequentes: Se um conjunto é frequentemente comprado juntos, ele é adicionado à lista de conjuntos frequentes. O algoritmo então gera conjuntos de tamanho maior com base nos conjuntos frequentes encontrados até agora.
 - Iteração: O processo de geração de candidatos, verificação de suporte e geração de conjuntos frequentes é repetido até que nenhum novo conjunto frequente seja encontrado.

> Vantagens: 
> - Mais eficiente em termos de tempo de execução e uso  de memória do que o Apriori
>
> Desvantagens:
> - Assim como o Apriori, pode ser ineficiente para conjuntos de dados muito grandes

[Implementação Eclat](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/eclat.py)

#### FP-Growth:
É uma alternativa às duas primeiras apresentadas. Ela é mais eficiente em termos de memória e tempo de execução, pois não requer a geração de todos os conjuntos de itens de tamanho ‘k’ antes de gerar os conjuntos de tamanho ‘k+1’.
Como funciona:
 - Construção da Árvore FP-Growth: O algoritmo constrói uma estrutura de dados chamada de "árvore FP-Growth" a partir dos dados de transação. A árvore FP-Growth é uma representação compacta dos dados que permite a geração eficiente de conjuntos frequentes.
 - Geração de Conjuntos Frequentes: A partir da árvore FP-Growth, o algoritmo gera conjuntos frequentes. Isso é feito de forma eficiente, pois não requer a geração de todos os conjuntos de tamanho k antes de gerar os conjuntos de tamanho k+1.

> Vantagens:
> -  Mais efiente em termos de tempo de execução e uso de memória do que o Apriori e o Eclat.<br>
>
> Desvantagens:
> - A contrução da árvore FP-Growth pode ser complexa de se implementar

[Implementação FP-Growth](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/fp_growth.py)

#
## Chapter 7: Association

### Concept:
It is a data mining technique that seeks to find relationships (that may be of interest) between different items in a data set. These relationships can be used to make recommendations, identify purchasing patterns, analyze data, among others. It is particularly useful in marketing applications where the goal is to discover which items are frequently purchased together and in recommendation systems.

### Most used techniques:
#### Apriori:
Uses a depth-first search algorithm to find sets of items that are frequently purchased together. It is based on the idea that if a set of items is frequently purchased together, then any subset of that set should also be frequently purchased together.<br>
How it works:
 - Candidate generation: Initially, the algorithm generates one-item sets (often called "1-itemsets"). It then generates sets of two items that are frequently purchased together (2-itemsets), and so on.
 - Support Check: For each set generated, the algorithm checks whether the set is frequently purchased together, that is, whether the set frequency is greater than or equal to a pre-defined support threshold.
 - Frequent Set Generation: If a set is frequently purchased together, it is added to the frequent set list. The algorithm then generates larger sized sets based on the frequent sets found so far.
 - Iteration: The process of generating candidates, checking support, and generating frequent sets is repeated until no new frequent sets are found.

> Advantages:
> - Simplicity and ease of implementation.
> - Being able to find all frequent sets in a data set.
>
> Disadvantages:
> - Can be time and memory inefficient, especially for large datasets, due to generating all sets of size k before generating sets of size k+1.

[Apriori Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/apriori.py)

#### Eclat:
It is based on the idea that if a set of items is frequently purchased together, then any subset of that set should also be frequently purchased together.<br>
How it works:
 - Candidate Generation: Just like Apriori, Eclat starts by generating sets of one item. It then generates sets of two items that are frequently purchased together, and so on.
 - Support Check: For each set generated, the algorithm checks whether the set is frequently purchased together, using the same support logic as Apriori.
 - Frequent Set Generation: If a set is frequently purchased together, it is added to the frequent set list. The algorithm then generates larger sized sets based on the frequent sets found so far.
 - Iteration: The process of generating candidates, checking support, and generating frequent sets is repeated until no new frequent sets are found.

> Advantages:
> - More efficient in terms of execution time and memory usage than Apriori
>
> Disadvantages:
> - Like Apriori, it can be inefficient for very large data sets

[Eclat Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/eclat.py)

#### FP-Growth:
It is an alternative to the first two presented. It is more efficient in terms of memory and execution time, as it does not require generating all itemsets of size 'k' before generating sets of size 'k+1'.
How it works:
 - FP-Growth Tree Construction: The algorithm builds a data structure called "FP-Growth tree" from the transaction data. The FP-Growth tree is a compact representation of data that allows efficient generation of frequent sets.
 - Generation of Frequent Sets: From the FP-Growth tree, the algorithm generates frequent sets. This is done efficiently as it does not require generating all sets of size k before generating sets of size k+1.

> Advantages:
> - More efficient in terms of execution time and memory usage than Apriori and Eclat.<br>
>
> Disadvantages:
> - The construction of the FP-Growth tree can be complex to implement

[FP-Growth Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/associacao/fp_growth.py)
