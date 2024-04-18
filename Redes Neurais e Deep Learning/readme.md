## Capítulo 10: Redes Neurais e Deep Learning
### Conceitos
##### Rede Neural:
É um tipo de modelo computacional inspirado no funcionamento do cérebro humano, processando informações atravé de neurônio conectados. Uma rede neural processa dados em uma estrutura de nós (neurônios artificiais) conectados entre si, cada neurônio em uma rede neural realiza operações simples, geralmente envolvendo soma ponderada das entradas, seguida pela aplicação de uma função não linear chamada *função de ativação*. Essas funções ajudam a rede a entender padrões complexos e não-lineares. As redes neurais são organizadas nas seguintes camadas:
- **Camada de entrada:** Onde os dados são inseridos na rede.
- **Camadas ocultas:** Camadas intermediárias que transformam os dados de entrada em algo que a camada de saída possa usar.
- **Camada de saída:** Produz a previsão ou classificação final com base nas informações realizadas pelas camadas anteriores.

> Exemplos de funções de ativação:
  > - _Sigmóide:_ Onde mapeia os valores de entrada para um intervalo entre 0 e 1, útil para problemas de classificação binária (2 classes, 0 ou 1, True ou False).
  > - _Tangente Hiperbólica (Tanh):_ Similar à sigmóide, mas mapeia os valores entre -1 e 1.
  > - _ReLU (rectified linear unit):_ Permite que apenas valores positivos passem, sendo zero para todos os valores negativos. É a mais usada atualmente devido à eficiência computacional e eficácia no treinamento de redes profundas.

"A aprendizagem de uma rede neural é definir o melhor conjunto de pesos a serem utilizados"

#### Deep Learning:
É um subcampo da ML (Machine Learning) que utiliza redes neurais com muitas camadas ocultas (em teoria, mais de 2 camadas, já pode se considerar deep learning), a profundidade dessas redes é o que permite que elas aprendam padrões extremamente complexos nos dados. O termo *profundo* refere-se tanto ao número de camadas quanto à capacidade dessas redes de modelar abstrações de alto nível nos dados. Por exemplo, em tarefas de processamento de imagens, as camadas mais ppróximas à entrada podem aprender a reconhecer bordas e texturas simples, enquanto as mais profundas podem aprender a identificar objetos complexos como rostos e paisagens.

#### Neurônio Artificial:
É a unidade básica do processamento de uma rede neural artificial (RNA). Possui o funcionamento de receber entradas, processá-las e produzir uma saída. Um neurônio típico possui essas partes principais:
 - **Entradas (inputs):** São os dados recebidos pelo neurônio de outras partes do sistema ou da camada anterior da rede. Cada entrada está associada à um peso, que indica a importância relativa dessa entrada para o neurônio.
 - **Pesos (weights):** São os parâmetros que ajustama a força do sinal de cada entrada. São ajustáveis e são aprendidos durante o processo de treinamento da rede neural.
 - **Soma ponderada:** O neurônio calcula a soma ponderada das entradas, que é basicamente a soma de cada entrada multiplicada pelo seu peso correspondente.
 - **Viés (bias):** Um termo adicional que permite ajustar o neurônio junto com os pesos. O viés permite que o neurônio mude a saída ao longo da função de ativação para melhor se adequar aos dados.
 - **Função de ativação:** Após calcular a soma ponderada das entradas e adicionar o viés, o resultado é passado por uma função de ativação. Essa função é crucial pois introduz não linearidade ao modelo, permitindo que a rede neural aprenda e realize tarefas mais complexas.
 - **Saída (output):** A saída do neurônio é o resultado da função de ativação. Esta saída pode ser usada como entrada para os neurônios da próxima camada da rede neural, ou pode ser a saída final da rede, dependendo da posição do neurônio dentro da arquitetura.
Em operação, cada neurônio recebe entradas de vários outros neurônios ou de uma fonte externa (como dados de treinamento), multiplica essas entradas pelos seus pesos, soma os produtos, adiciona um viés, e passa o resultado através de uma função de ativação para gerar a saída. Este processo é repetido em todos os neurônios da rede, e pode ocorrer em múltiplas camadas, permitindo que a rede neural execute desde tarefas simples até funções computacionais extremamente complexas.

#### Step Functions:
São funções matemáticas que mudam de valor em um ou mais pontos ao longo do seu domínio. São caracterizadas por terem uma mudança abrupta de valor, geralmente de um estado constante para outro, o que as torna semelhantes a um degrau de escada quando vizualizadas em um gráfico. Uma das funções mais conhecidas e utilizadas é a Heaviside (ou degrau unitário), basicamente retorna 0 sempre que o valor passado de x for menor que 0 e retorna 1 se x for maior ou igual a 0, é muito parecido com o ReLU.

#### Perceptron e sua diferença para o Neurônio Artificial:
Consiste em uma única camada de neurônios, onde cada neurônio está conectado diretamente aos inputs e produz uma saída binária (0 ou 1). O perceptron pode ser usado para problemas de classificação binária linearmente separáveis. Ele usa uma função de ativação degrau (step function) para determinar sua saída com base na soma ponderada dos inputs.
Já os neurônios é uma unidade de processamento mais genérica e flexível inspirada no funcionamento dos neurônios biológicos, pode ter múltiplas camadas de neurônios (entrada, ocultas e saída), podem ter funções de ativação mais complexas e são a base de construção de RNA's mais complexas como MLPs (Multilayer Perceptrons) e CNNs (Convolutional Neural Networks).

#### Multilayer perceptron (MLP):
São uma evolução natural do perceptron simples, projetados para superar algumas das suas limitações, principalmente a incapacidade de resolver problemas que não são linearmente separáveis. O MLP é um tipo básico de rede neural artificial que consiste em várias camadas de neurônios, incluindo uma camada de entrada, uma ou mais camadas ocultas e uma camada de saída. Essas redes são capazes de aprender representações de dados mais complexas e realizar tarefas de classificação e regressão muito além das capacidades de um perceptron simples. Tem a mesma estrutura de uma rede neural (as camadas de rede neural). O funcionamento de um MLP pode ser descrito através dos seguintes passos:
- **Propagação para Frente (Forward Propagation):** Os dados de entrada passam pela camada de entrada, são processados sequencialmente pelas camadas ocultas, e finalmente pela camada de saída. Em cada camada, os dados são transformados pelos pesos sinápticos e funções de ativação dos neurônios.
> Propagação para Frente - Foward Propagation (detalhada):
> - _Entrada dos dados:_ Os dados de entrada são alimentados na rede neural. Cada unidade na camada de entrada representa uma característica ou um atributo dos dados.
> - _Cálculo da Saída da Rede:_ Os dados de entrada são propagados através das camadas ocultas até a camada de saída. Em cada camada, os valores de entrada são multiplicados pelos pesos sinápticos, somados e, em seguida, passados por uma função de ativação para produzir a saída da camada.
> - _Função de Ativação:_ Cada neurônio em uma camada oculta e na camada de saída aplica uma função de ativação aos valores somados. Isso introduz não-linearidades na rede e permite que ela aprenda relações complexas nos dados.
> - _Cálculo da Saída da Rede:_ A saída da última camada é a saída da rede neural, que pode ser uma previsão em problemas de regressão ou uma distribuição de probabilidade em problemas de classificação.

- **Propagação para Trás (Backpropagation):** Após a obtenção da saída, o erro (a diferença entre a saída esperada e a obtida) é calculado. Esse erro é então propagado de volta pela rede, da camada de saída para as camadas ocultas. Durante este processo, os pesos são ajustados para minimizar o erro. Este ajuste é tipicamente realizado usando o método do *gradiente descendente*.
> Retroprogapação do Erro - Backpropagation (detalhada):
> - _Cálculo do Erro:_ A diferença entre as saídas previstas pela rede e as saídas reais é calculada usando uma função de perda (loss function). Esta função mede o quão bem a rede está performando na tarefa em questão.
> - _Retropropagação do Erro:_ O erro calculado é então retropropagado através da rede, da camada de saída até a camada de entrada. Durante esse processo, o algoritmo de backpropagation ajusta os pesos sinápticos em cada camada de acordo com a contribuição de cada peso para o erro total.
> - _Atualização dos Pesos:_ Os pesos sinápticos são atualizados usando um algoritmo de otimização, como o gradiente descendente. Este algoritmo ajusta os pesos em direção ao gradiente negativo da função de perda, de forma a minimizar o erro.
> - _Iteração:_ O processo de propagação para frente e retropropagação do erro é repetido para múltiplas iterações (épocas) até que o erro seja minimizado ou até que um critério de parada seja alcançado.

Uma vez que a rede neural é treinada, ela pode ser usada para fazer previsões ou classificar novos dados, aplicando a propagação para frente com os pesos ajustados durante o treinamento.

Embora seja parecido com o conceito de *Deep Learning*, esse último é mais amplo e engloba uma variedade de arquiteturas e conceitos enquanto *MLPs* são uma parte específica.

#### Cálculo de erro:
São usados para avaliar o quão bem um modelo se ajusta aos dados reais. Eles quantificam a discrepância entre os valores previstos por um modelo e os valores reais observados, importantes para ajustar e melhorar os modelos durante o treinamento, mas também para avaliar seu desempenho após o treinamento. Alguns tipos desses cálculos:
- **Erro quadrático médio (MSE - Mean Squared Error):** Calcula a média dos quadrados das diferenças entre os valores previstos e os valores reais. Muito usado em problemas de regressão e é útil porque penaliza fortemente os erros grandes.
- **Erro absoluto médio (MAE - Mean Absolute Error):** Calcula a média dos quadrados das diferenças entre os valores previstos e os valores reais e assim como o MSE, penaliza fortemente erros grandes.
- **Raiz do Erro Quadrático Médio (RMSE - Root Mean Squared Error):** O RMSE é simplesmente a raiz quadrada do MSE. Ele tem a vantagem de estar na mesma unidade das variáveis de resposta e é mais sensível a erros grandes do que o MAE.
- **Logaritmo do Erro Quadrático Médio (Log MSE):** É uma variação do MSE que utiliza o logaritmo dos erros antes de calcular sua média quadrada. Isso pode ajudar a estabilizar variações de escala entre os valores preditos e os valores reais, tornando-o útil quando os dados têm uma ampla gama de valores.

Algumas aplicações desses cálculos envolvem:
- **Otimização de modelos:** Onde durante o treinamento de modelos de aprendizado de máquina, os cálculos de erro são usados para ajustar os parâmetros do modelo (com os pesos em redes neurais) de modo a minimizar o erro. Algoritmos como o gradiente descendente são frequentemente empregados para este fim.
- **Validação e teste:** Onde após o treinamento, os cálculos de erro são usados para avaliar o desempenho do modelo em dados novos e não vistos anteriormente. Isso ajuda a entender como o modelo provavelmente se comportará quando usado na prática.
- **Comparação de modelos:** Diferentes modelos podem ser comparados com base em suas métricas de erro em um conjunto de dados comum. Isso permite que cientistas de dados escolham o modelo que melhor se ajusta aos dados ou ao problema em questão.

#### Loss Functions:  
São funções matemáticas que quantificam a discrepância entre os valores previstos por um modelo e os valores reais observados nos dados de treinamento. Eles desempenham um papel fundamental no treinamento de modelos de aprendizado de máquina, especialmente em algoritmos de otimização, como a descida do gradiente. Tem como objetivo, minimizar essa função, ou seja, reduzir a discrepância entre as previsões do modelo e os valores reais. Existem diferentes tipos de funções de perda, e a escolha da função correta depende do tipo de problema de aprendizado de máquina abordado. As mais comuns são:
- **Erro Quadrático Médio (MSE - Mean Squared Error)**
- **Cross-Entropy Loss:** Também conhecida como log loss, é frequentemente usada em problemas de classificação binária ou multiclasse. Ela quantifica a diferença entre a distribuição de probabilidade prevista e a distribuição real das classes.
- **Erro Absoluto Médio (MAE - Mean Absolute Error)**
- **Huber Loss:** Uma variação do MAE que é menos sensível a outliers. Ela combina os benefícios do MSE e do MAE, sendo quadrática para erros pequenos e linear para erros grandes.
- **Hinge Loss:** Usada principalmente em problemas de classificação binária com SVMs (Support Vector Machines). Ela penaliza previsões erradas de forma linear, aumentando proporcionalmente ao erro.

Durante o treinamento de um modelo de aprendizado de máquina, a função de perda é calculada iterativamente em cada passo do processo de otimização, comparando as previsões do modelo com os valores reais nos dados de treinamento. O objetivo é ajustar os parâmetros do modelo de forma a minimizar essa função de perda, o que geralmente é feito usando algoritmos de otimização como o gradiente descendente.
Apesa de estar relacionada com os cálculos de erro, não são a mesma coisa, uma vez que a loss function quantifica a discrepância entre as previsões do modelo e os valores reais, os cálculos de erro referem-se ao processo de aplicar essa função aos dados de treinamento para avaliar o desempenho do modelo.

#### Cálculos do parâmetro Delta:
Comumente denotado por Δ, é utilizado em diversas áreas da matemática e ciências aplicadas para representar mudanças ou diferenças em quantidades. No contexto das redes neurais e do treinamento utilizando o algoritmo de retropropagação (backpropagation), o parâmetro delta é frequentemente associado aos cálculos realizados para atualizar os pesos durante o processo de treinamento.  Durante a retropropagação do erro, o parâmetro delta é calculado para cada neurônio em cada camada oculta e na camada de saída. O cálculo do parâmetro delta é realizado seguindo as seguintes etapas:
- **Camada de saída:** Para cada neurônio na camada de saída, o parâmetro delta é calculado usando a derivada da função de ativação (como a função sigmóide, por exemplo) e o gradiente da função de perda em relação à saída do neurônio.
- **Camadas ocultas:** Para as camadas ocultas, o parâmetro delta é calculado usando o parâmetro delta da próxima camada (calculado na etapa anterior) e os pesos sinápticos conectando os neurônios.

Uma vez que os parâmetros delta são calculados para cada neurônio em todas as camadas da rede neural, eles são usados para atualizar os pesos durante o treinamento. Os pesos são atualizados na direção oposta ao gradiente do erro, permitindo que a rede aprenda a minimizar o erro e fazer previsões mais precisas.

#### Gradient Descent:
É um algoritmo de otimização amplamente utilizado para encontrar omínimo de uma *loss function*, em relação aos parâmetros de um modelo. Funciona atualizando iterativamente os parâmetros na direção oposto do gradiente da *loss function* em relação a esses parâmetros, o que leva a uma redução gradual do valor da função de perda. Funciona assim:
 - **Inicialização:** Os parâmetros do modelo são inicializados com valores aleatórios ou pré-definidos.
 - **Cálculo do Gradiente:** O gradiente da função de perda é calculado em relação a cada parâmetro do modelo. O gradiente indica a direção e a magnitude da mudança necessária para minimizar a função de perda.
 - **Atualização dos Parâmetros:** Os parâmetros são atualizados movendo-se uma pequena distância na direção oposta do gradiente. A taxa na qual os parâmetros são atualizados é determinada pela taxa de aprendizado (*learning rate*).
 - **Iteração:** Os passos 2 e 3 são repetidos até que um critério de parada seja alcançado, como um número máximo de iterações ou uma mudança pequena na função de perda.

Tipos:
- **Batch Gradient Descent:** Esse método calcula o gradiente usando o conjunto de dados completo de uma vez, é eficaz para conjunto de dados pequenos mas pode ser computacionalmente caro para conjuntos de dados grandes.
- **Stochastic Gradient Descent (SGD):** Nesse método, o gradiente é calculado e os parâmetros dão atualizados para cada exemplo de treinamento individualmente de forma estocástica (que acontece a partir de probabilidades). É mais rápido e eficiente para grandes conjuntos de dados, mas pode ser ruidoso e menos estável.
- **Mini-Batch Gradient Descent:** é uma combinação dos dois anteriores, onde o gradiente é calculado e os parâmetros são atualizados usando um pequeno subconjunto do conjunto de dados em cada iteração (mini-batch). Ele combina a eficiência do SGD com a estabilidade do Batch Gradient Descent.

#### Learning Rate:
 É um hiperparâmetro fundamental em algoritmos de otimização, como o Gradient Descent, amplamente utilizado no treinamento de modelos de aprendizado de máquina, incluindo redes neurais. A taxa de aprendizado determina o tamanho dos passos que o algoritmo de otimização dá ao ajustar os pesos do modelo durante o treinamento. É um hiperparâmetro fundamental em algoritmos de otimização, como o Gradient Descent, amplamente utilizado no treinamento de modelos de aprendizado de máquina, incluindo redes neurais. <br>
 A taxa de aprendizado determina o tamanho dos passos que o algoritmo de otimização dá ao ajustar os pesos do modelo durante o treinamento. A escolha da taxa de aprendizado é crucial para o treinamento eficaz de um modelo de aprendizado de máquina. Uma taxa de aprendizado muito alta pode fazer com que o algoritmo de otimização oscile em torno do mínimo global da função de custo ou até mesmo divergir, tornando o treinamento instável. Por outro lado, uma taxa de aprendizado muito baixa pode fazer com que o algoritmo de otimização convirja muito lentamente para o mínimo global, aumentando significativamente o tempo de treinamento. Alguns métodos comuns para ajustar a taxa de aprendizado durante o treinamento incluem:
 - Taxa de Aprendizado Fixa: Manter uma taxa de aprendizado constante durante todo o processo de treinamento. Essa abordagem é simples, mas pode ser sensível à escolha da taxa de aprendizado inicial.
 - Taxa de Aprendizado Decrescente: Reduzir gradualmente a taxa de aprendizado ao longo do tempo, à medida que o treinamento progride. Isso pode ajudar a garantir uma convergência mais suave do algoritmo de otimização.
 - Taxa de Aprendizado Adaptativa: Usar técnicas de otimização adaptativa, como o Adam, RMSprop ou Adagrad, que ajustam automaticamente a taxa de aprendizado com base nas características do problema e no progresso do treinamento.

#### Batch Size:
Também conhecido como "tamanho do lote", é um hiperparâmetro importante em algoritmos de aprendizado de máquina, especialmente em deep learning, que envolve o treinamento de redes neurais. Refere-se ao número de exemplos de treinamento que são usados em uma única iteração (ou passo) do algoritmo de treinamento. O tamanho do lote pode afetar diversos aspectos do processo de treinamento e do desempenho do modelo:
- **Velocidade de Treinamento:** O tamanho do lote afeta a eficiência computacional do treinamento. Tamanhos de lote maiores geralmente levam a um treinamento mais rápido, pois menos atualizações de peso são realizadas por época de treinamento.
- **Estabilidade do Treinamento:** Tamanhos de lote menores podem resultar em atualizações de peso mais frequentes e, portanto, em uma convergência mais estável durante o treinamento. No entanto, tamanhos de lote muito pequenos podem introduzir ruído no processo de treinamento.
- **Requisitos de Memória:** Tamanhos de lote maiores exigem mais memória do sistema, pois mais exemplos de treinamento precisam ser armazenados temporariamente na memória durante cada iteração do treinamento.

A escolha do tamanho do lote depende de vários fatores, incluindo o tamanho do conjunto de dados de treinamento, a arquitetura do modelo, os recursos computacionais disponíveis e a estabilidade do treinamento desejada. Tamanhos de lote comuns incluem:
- **Batch Size Grande:** Valores entre 64 e 512 são frequentemente usados em grandes conjuntos de dados e arquiteturas de modelos complexos. Isso proporciona uma eficiência computacional maior, mas pode resultar em uma convergência menos estável.
- **Batch Size Pequeno:** Valores entre 1 e 32 são comuns em problemas com conjuntos de dados menores ou quando se deseja uma convergência mais estável. Isso pode aumentar a estabilidade do treinamento, mas geralmente leva a um treinamento mais lento.

#### Epochs:
As "epochs" (ou épocas) referem-se ao número de vezes que todo o conjunto de dados de treinamento é passado pela rede neural durante o processo de treinamento. Em outras palavras, uma época é uma única passagem de todos os exemplos de treinamento pelo modelo para atualizar os pesos e ajustá-lo aos dados. O número de épocas é um hiperparâmetro importante no treinamento de modelos de aprendizado de máquina e tem um impacto significativo no desempenho do modelo. Treinar o modelo por várias épocas permite que ele aprenda de forma mais completa os padrões nos dados e melhore sua capacidade de generalização. <br>
A escolha do número de épocas depende do problema específico, da arquitetura do modelo, do tamanho do conjunto de dados e de outros fatores. Em geral, treinar o modelo por um número suficiente de épocas é importante para garantir que ele tenha tempo suficiente para aprender os padrões nos dados. No entanto, é importante evitar o sobreajuste (overfitting), onde o modelo aprende os dados de treinamento muito bem, mas não generaliza bem para novos dados. Isso pode ser feito monitorando o desempenho do modelo em um conjunto de validação e interrompendo o treinamento quando o desempenho começa a piorar.

[Implementação simples de algum dos conceitos até aqui](https://colab.research.google.com/drive/1xjey8s1BvlSkszsXm9zSzo2DHOFj1qGi#scrollTo=2XRRlMmY_RQ1 )

#### Redes Neurais Convolucionais (CNN):
