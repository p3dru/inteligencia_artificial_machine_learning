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

