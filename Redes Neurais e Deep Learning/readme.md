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

#### Multilayer perceptron (MLP) | Redes Neurais Densas:
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
 Ou Convolutional Neural Networks, são um tipo especializado de redes neurais profundas projetadas para processar e reconhecer padrões em dados de matriz, como imagens. Elas são amplamente utilizadas em tarefas de visão computacional, como classificação de imagens, detecção de objetos, reconhecimento facial, entre outros. Tem como características principais:
- **Camadas Convolucionais:** As CNNs incluem camadas convolucionais que aplicam *operações de convolução* aos dados de entrada. Isso permite que a rede aprenda características importantes da imagem, como bordas, texturas e padrões locais.
- **Camadas de Pooling:** Após as camadas convolucionais, as CNNs frequentemente incluem camadas de pooling, como a camada de max pooling, que reduzem a dimensionalidade dos dados e ajudam a tornar a representação espacialmente invariante.
- **Arquitetura Hierárquica:** As CNNs geralmente têm uma arquitetura hierárquica, onde as primeiras camadas aprendem características de baixo nível, como bordas e texturas, e as camadas posteriores combinam essas características para aprender características de alto nível, como formas e objetos.
- **Camadas Totalmente Conectadas:** Após as camadas convolucionais e de pooling, as CNNs geralmente incluem camadas totalmente conectadas, que combinam as características aprendidas para fazer previsões finais, como classificar a imagem em categorias diferentes.

#### Operador de Convolução:
É usado para aplicar filtros a uma matriz de dados, como uma imagem, para realizar operações como detecção de bordas, suavização ou realce de características. O operador de convolução aplica um filtro (também chamdo de kernel) a uma região de entrada, multiplicando os valores dos pixels pelo filtro e somando os resultados. Esse processo é repetido em todas as regiões de entrada, resultando em uma nova matriz de saída, que geralmente é menor que a entrada, dependendo do tamanho do filtro e das bordas. Exemplo utilizando imagens (2D):
 - **Entrada (iamgem):** Uma matriz 2D de valores de pixels.
 - **Filtro (kernel):** Uma matriz 2D menor que define a operação a ser aplicada.
 - **Convolução:** O filtro é deslizado sobre a imagem (como se movesse uma coluna por vez da esquerda para a direita, de cima para baixo), multiplicando e somando os valores dos pixels conforme definido pela matriz do filtro.
 - **Saída:** Uma nova matriz 2D, resultante das operações de convolução.
 - **Peso Compartilhado:** No contexto das CNNs, os pesos do filtro são compartilhados em todas as regiões da entrada, o que significa que o mesmo filtro é aplicado a todas as partes da imagem. Isso permite que a rede aprenda características espaciais invariantes, como bordas e texturas, independentemente da localização na imagem.
- **Operações Locais:** O operador de convolução é uma operação local, o que significa que ele considera apenas uma região local da entrada em cada etapa. Isso ajuda a reduzir a quantidade de parâmetros necessários para a rede e a capturar padrões locais importantes.
- **Stride e Padding:** O tamanho do passo (stride) controla quantas posições o filtro se move a cada passo, enquanto o preenchimento (padding) adiciona zeros ao redor da borda da entrada para manter o tamanho da saída. Esses parâmetros afetam o tamanho da saída e a quantidade de sobreposição entre as regiões de entrada.

#### Pooling:
O pooling, também conhecido como subamostragem, é uma operação comum em redes neurais convolucionais (CNNs) que reduz a dimensionalidade dos dados, preservando as características mais importantes. Ele é aplicado após as camadas convolucionais e tem como objetivo reduzir o tamanho espacial (largura e altura) da representação da imagem, enquanto mantém as características mais importantes. Existem diferentes tipos de pooling, sendo os mais comuns o Max Pooling e o Average Pooling.
- **Max Pooling:** Em cada região (geralmente quadrada) da entrada, o valor máximo é selecionado para ser retido na saída. Isso significa que apenas a característica mais importante de cada região é mantida. Por exemplo, em uma região 2x2, o valor máximo de quatro pixels é selecionado e mantido na saída.
- **Average Pooling:** Similar ao Max Pooling, mas em vez de selecionar o valor máximo, o valor médio é calculado e retido na saída. Isso geralmente produz uma suavização da imagem e reduz a quantidade de ruído.
Possui algumas propriedades como:
- **Redução de Dimensionalidade:** O pooling reduz a resolução espacial dos dados de entrada, o que diminui a quantidade de parâmetros na rede e, consequentemente, a carga computacional e a probabilidade de overfitting.
- **Invariância a Translações Pequenas:** O pooling torna a representação de entrada invariante a pequenas translações da imagem, tornando o modelo mais robusto a variações de posição dos objetos na imagem.
- **Preservação de Características Importantes:**  Embora reduza a dimensionalidade, o pooling retém as características mais importantes aprendidas nas camadas convolucionais anteriores.

#### Overfitting:
Também conhecido como sobreajuste em português, é um fenômeno comum em modelos de aprendizado de máquina, onde o modelo se ajusta excessivamente aos dados de treinamento, capturando não apenas os padrões genuínos, mas também o ruído ou a aleatoriedade nos dados. Isso resulta em um modelo que tem um desempenho muito bom nos dados de treinamento, mas se generaliza mal para novos dados não vistos. Tem como causa:
- **Modelo Complexo:**  Modelos muito complexos, com alta capacidade de aprendizado, podem capturar padrões sutis nos dados de treinamento, incluindo o ruído, levando ao overfitting.
- **Dados Insuficientes:** Quando o conjunto de dados de treinamento é pequeno em relação à complexidade do modelo, o modelo pode memorizar os exemplos de treinamento em vez de aprender padrões gerais, levando ao overfitting.
- **Treinamento Excessivo:** O treinamento excessivo ocorre quando o modelo é treinado por um número excessivo de épocas, permitindo que ele ajuste demais os pesos aos dados de treinamento.<br>
Sintomas:
- **Desempenho Diferente nos Dados de Treinamento e Teste:** O modelo tem um desempenho muito bom nos dados de treinamento, mas um desempenho significativamente pior nos dados de teste ou validação.
- **Baixa Generalização:** O modelo falha em generalizar padrões aprendidos nos dados de treinamento para novos dados não vistos.<br>
Como lidar com o Overfitting:
- **Regularização:** Técnicas como *L1 ou L2 regularization* adicionam penalidades aos pesos do modelo, reduzindo a complexidade do modelo e prevenindo o overfitting.
- **Validação Cruzada:** Usar técnicas como *validação cruzada* para avaliar o desempenho do modelo em conjuntos de dados diferentes e identificar o overfitting.
- **Redução da Complexidade do Modelo:** Reduzir a complexidade do modelo, como reduzir o número de camadas em uma rede neural ou o número de parâmetros em um modelo de aprendizado de máquina.
- **Aumento de Dados:** Aumentar o tamanho do conjunto de dados de treinamento através de técnicas como geração de dados sintéticos ou aumento de dados pode ajudar a reduzir o overfitting.

#### L1 e L2 Regularization:
São técnicas utilizadas para regularizar modelos de ML, incluindo redes neurais, através da adição de termos de regularização à função de perda. O objetivo desses termos de é evitar o *overfitting*, penalizando os valores extremos dos pesos dos parâmetros do modelo. <br>
**L1:**
- **Definição:** A L1 regularization, também conhecida como "regularização Lasso", adiciona à função de perda um termo que é proporcional à soma dos valores absolutos dos pesos dos parâmetros do modelo.
- **Objetivo:** O termo de regularização L1 incentiva os pesos a se tornarem esparços, ou seja, muitos pesos terão valores próximos de zero, o que pode resultar em seleção automática de características (feature selection).
- **Fórmula:** λ * sum(abs(w)), onde λ é um  hiperparâmetro que controla a força da regularização e w são os pesos dos parâmetros do modelo.

**L2:**
- **Definição:** A L2 regularization, também conhecida como "regularização Ridge", adiciona à função de perda um termo que é proporcional à soma dos quadrados dos valores dos pesos dos parâmetros do modelo.
- **Objetivo:** O termo de regularização L2 penaliza os pesos dos parâmetros do modelo, fazendo com que eles tendam a ser menores, mas sem forçá-los a zero. Isso ajuda a evitar que os pesos cresçam excessivamente.
- **Fórmula:** = λ * sum(w^2), onde λ (lambda) é um hiperparâmetro que controla a força da regularização e w são os pesos dos parâmetros do modelo.<br>

Esparcidade dos Pesos:
L1 regularization tende a produzir pesos esparços (muitos pesos são zero).
L2 regularization tende a produzir pesos menores, mas não necessariamente esparços.<br>
Robustez:
L1 regularization é mais robusta à presença de características irrelevantes ou redundantes, pois pode levar à seleção automática de características.
L2 regularization é menos suscetível a outliers nos dados.

Ambas as regularizações são úteis para evitar o overfitting e melhorar a generalização de modelos de aprendizado de máquina. A escolha entre L1 e L2 regularization depende do problema específico e da natureza dos dados. Em muitos casos, a combinação de ambas, chamada de *Elastic Net*, pode ser benéfica.

#### Validação Cruzada (Cross-Validation):
É uma técnica estatística utilizada para avaliar o desempenho de um modelo de aprendizado de máquina e estimar sua capacidade de generalização para novos dados. Ela é especialmente útil quando se tem um conjunto de dados limitado, pois permite que o conjunto de dados seja utilizado de forma mais eficiente para avaliação do modelo. Como funciona:
- **Divisão do conjunto de dados:** O conjunto de dados é dividido em k subconjuntos (folds) aproximadamente iguais. Geralmente, k é escolhido entre 5 e 10, mas pode variar dependendo do tamanho do conjunto de dados e da preferência do usuário.
- **Treinamento e Avaliação:** O modelo é treinado k vezes, cada vez usando k-1 folds como dados de treinamento e o fold restante como dados de teste. Para cada iteração, o modelo é treinado nos k-1 folds e avaliado no fold que não foi utilizado para treinamento.
- **Avaliação do Desempenho:** Após as k iterações, são obtidas k métricas de desempenho (como precisão, acurácia, F1-score, etc.), uma para cada fold de teste. O desempenho geral do modelo é calculado pela média das métricas obtidas nos k folds.<br>
Benefícios da validação cruzada:
- **Melhor utilização dos dados:** Todos os dados são utilizados tanto para treinamento quanto para teste em algum momento, o que proporciona uma avaliação mais robusta do modelo.
- **Redução do Viés de Avaliação:** A média das métricas obtidas em k folds reduz o viés de avaliação, fornecendo uma estimativa mais confiável do desempenho do modelo.
- **Avaliação de Estabilidade:** A variabilidade do desempenho do modelo entre os diferentes folds fornece uma medida da estabilidade do modelo em relação à variação nos dados de treinamento.<br>
Tipos de validação cruzada:
- **K-Fold Cross-Validation:**  conjunto de dados é dividido em k folds, onde cada fold é usado uma vez como conjunto de teste e os k-1 folds restantes são usados como conjunto de treinamento.
- **Leave-One-Out Cross-Validation (LOOCV):** Cada observação é usada como conjunto de teste uma vez, enquanto os k-1 restantes são usados como conjunto de treinamento. É uma forma extrema de k-fold cross-validation, onde k é igual ao número total de observações.
- **Stratified Cross-Validation:** Garante que a distribuição das classes nos folds de treinamento e teste seja semelhante à distribuição das classes no conjunto de dados original. É útil para conjuntos de dados desbalanceados. 

#### Flatenning:
"Achatamento", é um conceito utilizado em redes neurais, especialmente em redes neurais convolucionais (CNNs), para transformar uma matriz multidimensional em um vetor unidimensional. Essa operação é comumente usada como preparação para a camada de saída de uma rede neural, onde os dados precisam ser transformados em um formato adequado para a classificação ou regressão. Funciona da seguinte forma:
- **Entrada Multidimensional:**  Nas camadas convolucionais de uma CNN, os dados de entrada são tipicamente representados em uma matriz multidimensional, onde cada dimensão corresponde a uma característica ou canal.
- **Transformação em Vetor:** O flattening é realizado aplicando uma operação de "aplanamento" na saída da última camada convolucional, onde todas as dimensões são combinadas em um único vetor unidimensional.
- **Saída Linear:** O resultado é um vetor linear que contém todas as informações das características extraídas pelas camadas convolucionais, pronto para ser alimentado nas camadas totalmente conectadas (densas) da rede neural para a classificação final.<br>
Exemplo:
Suponha que temos uma matriz de características de saída de uma camada convolucional com dimensões 3x3x64, onde:
- 3x3 é a altura e largura da matriz de características.
- 64 é o número de canais (ou características) produzidos por filtros convolucionais.<br>
Para aplicar flattening, transformamos essa matriz 3D em um vetor unidimensional de tamanho 3x3x64 = 576, que é o resultado final do processo de flattening. <br>
O flattening é comumente utilizado em redes neurais, especialmente em CNNs, como uma etapa de pré-processamento antes das camadas densas (totalmente conectadas) para classificação ou regressão. Ele permite que todas as informações extraídas pelas camadas convolucionais sejam achatadas em um único vetor para que possam ser alimentadas nas camadas densas para a tomada de decisão final.

[Implementação de conceitos para classificação de imagens](https://colab.research.google.com/drive/1aybJl8rk7JfDPYgXUCNRIgpoK64uwpYD#scrollTo=OW0Qw73eWg1_)

#

## Chapter 10: Neural Networks and Deep Learning
### Concepts
##### Neural Network:
It is a type of computational model inspired by the functioning of the human brain, processing information through connected neurons. A neural network processes data in a structure of nodes (artificial neurons) connected together, each neuron in a neural network performs simple operations, usually involving weighted summation of the inputs, followed by the application of a non-linear function called *activation function*. These functions help the network understand complex, non-linear patterns. Neural networks are organized into the following layers:
- **Input layer:** Where data is inserted into the network.
- **Hidden layers:** Intermediate layers that transform the input data into something that the output layer can use.
- **Output layer:** Produces the final prediction or classification based on the information provided by the previous layers.

> Examples of activation functions:
  > - _Sigmoid:_ Where maps input values ​​to a range between 0 and 1, useful for binary classification problems (2 classes, 0 or 1, True or False).
  > - _Hyperbolic Tangent (Tanh):_ Similar to the sigmoid, but maps values ​​between -1 and 1.
  > - _ReLU (rectified linear unit):_ Allows only positive values ​​to pass, with zero for all negative values. It is the most used currently due to its computational efficiency and effectiveness in training deep networks.

"Learning a neural network is about defining the best set of weights to use"

#### Deep Learning:
It is a subfield of ML (Machine Learning) that uses neural networks with many hidden layers (in theory, more than 2 layers, it can already be considered deep learning), the depth of these networks is what allows them to learn extremely complex patterns in data . The term *deep* refers to both the number of layers and the ability of these networks to model high-level abstractions in data. For example, in image processing tasks, layers closer to the input can learn to recognize simple edges and textures, while deeper layers can learn to identify complex objects like faces and landscapes.

#### Artificial Neuron:
It is the basic processing unit of an artificial neural network (ANN). It works by receiving inputs, processing them and producing an output. A typical neuron has these main parts:
 - **Inputs:** These are the data received by the neuron from other parts of the system or from the previous layer of the network. Each input is associated with a weight, which indicates the relative importance of that input to the neuron.
 - **Weights:** These are the parameters that adjust the signal strength of each input. They are adjustable and are learned during the neural network training process.
 - **Weighted sum:** The neuron calculates the weighted sum of the inputs, which is basically the sum of each input multiplied by its corresponding weight.
 - **Bias:** An additional term that allows you to adjust the neuron along with the weights. The bias allows the neuron to change the output along the activation function to better fit the data.
 - **Activation function:** After calculating the weighted sum of the inputs and adding the bias, the result is passed through an activation function. This function is crucial as it introduces non-linearity to the model, allowing the neural network to learn and perform more complex tasks.
 - **Output:** The output of the neuron is the result of the activation function. This output can be used as input to the neurons of the next layer of the neural network, or it can be the final output of the network, depending on the position of the neuron within the architecture.
In operation, each neuron receives inputs from several other neurons or an external source (such as training data), multiplies these inputs by their weights, sums the products, adds a bias, and passes the result through an activation function to generate the exit. This process is repeated in all neurons in the network, and can occur in multiple layers, allowing the neural network to perform everything from simple tasks to extremely complex computational functions.

#### Step Functions:
They are mathematical functions that change value at one or more points along their domain. They are characterized by having an abrupt change in value, generally from one constant state to another, which makes them similar to a step on a ladder when visualized on a graph. One of the best known and used functions is Heaviside (or unit step), it basically returns 0 whenever the past value of x is less than 0 and returns 1 if x is greater than or equal to 0, it is very similar to ReLU.

#### Perceptron and its difference from Artificial Neuron:
It consists of a single layer of neurons, where each neuron is connected directly to the inputs and produces a binary output (0 or 1). The perceptron can be used for linearly separable binary classification problems. It uses a step function to determine its output based on the weighted sum of the inputs.
Neurons are a more generic and flexible processing unit inspired by the functioning of biological neurons, they can have multiple layers of neurons (input, hidden and output), they can have more complex activation functions and are the basis for building more complex RNAs. such as MLPs (Multilayer Perceptrons) and CNNs (Convolutional Neural Networks).

#### Multilayer perceptron (MLP) | Dense Neural Networks:
They are a natural evolution of the simple perceptron, designed to overcome some of its limitations, mainly the inability to solve problems that are not linearly separable. MLP is a basic type of artificial neural network that consists of several layers of neurons, including an input layer, one or more hidden layers, and an output layer. These networks are capable of learning more complex data representations and performing classification and regression tasks far beyond the capabilities of a simple perceptron. It has the same structure as a neural network (the neural network layers). The operation of an MLP can be described through the following steps:
- **Forward Propagation:** The input data passes through the input layer, is processed sequentially by the hidden layers, and finally by the output layer. In each layer, data is transformed by the synaptic weights and activation functions of the neurons.
> Forward Propagation (detailed):
> - _Data input:_ The input data is fed into the neural network. Each unit in the input layer represents a characteristic or attribute of the data.
> - _Network Output Calculation:_ The input data is propagated through the hidden layers to the output layer. In each layer, the input values ​​are multiplied by the synaptic weights, summed, and then passed through an activation function to produce the layer's output.
> - _Activation Function:_ Each neuron in a hidden layer and output layer applies an activation function to the summed values. This introduces nonlinearities into the network and allows it to learn complex relationships in the data.
> - _Network Output Calculation:_ The output of the last layer is the output of the neural network, which can be a prediction in regression problems or a probability distribution in classification problems.

- **Backpropagation:** After obtaining the output, the error (the difference between the expected and obtained output) is calculated. This error is then propagated back through the network, from the output layer to the hidden layers. During this process, weights are adjusted to minimize error. This adjustment is typically performed using the *gradient descent* method.
> Error Backpropagation - Backpropagation (detailed):
> - _Error Calculation:_ The difference between the outputs predicted by the network and the actual outputs is calculated using a loss function. This function measures how well the network is performing on the task in question.
> - _Error Backpropagation:_ The calculated error is then backpropagated through the network, from the output layer to the input layer. During this process, the backpropagation algorithm adjusts the synaptic weights in each layer according to the contribution of each weight to the total error.
> - _Weights Update:_ Synaptic weights are updated using an optimization algorithm such as gradient descent. This algorithm adjusts the weights towards the negative gradient of the loss function, in order to minimize the error.
> - _Iteration:_ The process of forward propagation and back propagation of the error is repeated for multiple iterations (epochs) until the error is minimized or until a stopping criterion is reached.

Once the neural network is trained, it can be used to make predictions or classify new data by applying forward propagation with the weights adjusted during training.

Although it is similar to the concept of *Deep Learning*, the latter is broader and encompasses a variety of architectures and concepts while *MLPs* are a specific part.

#### Error calculation:
They are used to evaluate how well a model fits real data. They quantify the discrepancy between the values ​​predicted by a model and the actual observed values, important for tuning and improving models during training, but also for evaluating their performance after training. Some types of these calculations:
- **Mean Squared Error (MSE):** Calculates the mean of the squares of the differences between predicted values ​​and actual values. Widely used in regression problems and is useful because it heavily penalizes large errors.
- **Mean Absolute Error (MAE):** Calculates the mean of the squares of the differences between predicted values ​​and actual values ​​and, like MSE, heavily penalizes large errors.
- **Root Mean Squared Error (RMSE):** The RMSE is simply the square root of the MSE. It has the advantage of being in the same unit as the response variables and is more sensitive to large errors than MAE.
- **Logarithm of the Mean Square Error (Log MSE):** It is a variation of the MSE that uses the logarithm of the errors before calculating their square mean. This can help stabilize scale variations between predicted values ​​and actual values, making it useful when data has a wide range of values.

Some applications of these calculations involve:
- **Model Optimization:** Where during training of machine learning models, error calculations are used to adjust the model parameters (with the weights in neural networks) so as to minimize the error. Algorithms such as gradient descent are often employed for this purpose.
- **Validation and testing:** Where after training, error calculations are used to evaluate the model's performance on new and previously unseen data. This helps you understand how the model is likely to behave when used in practice.
- **Model Comparison:** Different models can be compared based on their error metrics on a common dataset. This allows data scientists to choose the model that best fits the data or problem at hand.

#### Loss Functions:
These are mathematical functions that quantify the discrepancy between the values ​​predicted by a model and the actual values ​​observed in the training data. They play a key role in training machine learning models, especially in optimization algorithms such as gradient descent. Its objective is to minimize this function, that is, to reduce the discrepancy between the model predictions and the real values. There are different types of loss functions, and choosing the right function depends on the type of machine learning problem being addressed. The most common are:
- **Mean Squared Error (MSE)**
- **Cross-Entropy Loss:** Also known as log loss, it is often used in binary or multiclass classification problems. It quantifies the difference between the predicted probability distribution and the actual class distribution.
- **Mean Absolute Error (MAE)**
- **Huber Loss:** A variation of MAE that is less sensitive to outliers. It combines the benefits of MSE and MAE, being quadratic for small errors and linear for large errors.
- **Hinge Loss:** Mainly used in binary classification problems with SVMs (Support Vector Machines). It penalizes incorrect predictions linearly, increasing proportionally to the error.

When training a machine learning model, the loss function is calculated iteratively at each step of the optimization process, comparing the model's predictions with the actual values ​​in the training data. The goal is to adjust the model parameters in such a way as to minimize this loss function, which is usually done using optimization algorithms such as gradient descent.
Although it is related to error calculations, they are not the same thing, since the loss function quantifies the discrepancy between model predictions and actual values, error calculations refer to the process of applying this function to data training method to evaluate model performance.

#### Delta parameter calculations:
Commonly denoted by Δ, it is used in several areas of mathematics and applied sciences to represent changes or differences in quantities. In the context of neural networks and training using the backpropagation algorithm, the delta parameter is often associated with the calculations performed to update the weights during the training process. During error backpropagation, the delta parameter is calculated for each neuron in each hidden layer and the output layer. The calculation of the delta parameter is carried out following the following steps:
- **Output layer:** For each neuron in the output layer, the delta parameter is calculated using the derivative of the activation function (like the sigmoid function, for example) and the gradient of the loss function with respect to the output of the neuron.
- **Hidden layers:** For hidden layers, the delta parameter is calculated using the delta parameter of the next layer (calculated in the previous step) and the synaptic weights connecting the neurons.

Once delta parameters are calculated for each neuron in all layers of the neural network, they are used to update the weights during training. The weights are updated in the opposite direction to the error gradient, allowing the network to learn to minimize error and make more accurate predictions.

#### Gradient Descent:
It is a widely used optimization algorithm to find the minimum of a *loss function*, in relation to the parameters of a model. It works by iteratively updating parameters in the opposite direction of the gradient of the *loss function* with respect to those parameters, which leads to a gradual reduction in the value of the loss function. It works like this:
 - **Initialization:** Model parameters are initialized with random or pre-defined values.
 - **Gradient Calculation:** The gradient of the loss function is calculated in relation to each model parameter. The gradient indicates the direction and magnitude of change required to minimize the loss function.
 - **Parameter Update:** Parameters are updated by moving a small distance in the opposite direction of the gradient. The rate at which parameters are updated is determined by the learning rate.
 - **Iteration:** Steps 2 and 3 are repeated until a stopping criterion is reached, such as a maximum number of iterations or a small change in the loss function.

Types:
- **Batch Gradient Descent:** This method calculates the gradient using the complete dataset at once, it is effective for small datasets but can be computationally expensive for large datasets.
- **Stochastic Gradient Descent (SGD):** In this method, the gradient is calculated and the parameters are updated for each training example individually in a stochastic way (which happens based on probabilities). It is faster and more efficient for large data sets, but can be noisy and less stable.
- **Mini-Batch Gradient Descent:** is a combination of the previous two, where the gradient is calculated and the parameters are updated using a small subset of the data set in each iteration (mini-batch). It combines the efficiency of SGD with the stability of Batch Gradient Descent.

#### Learning Rate:
 It is a fundamental hyperparameter in optimization algorithms such as Gradient Descent, which is widely used in training machine learning models, including neural networks. The learning rate determines the size of the steps the optimization algorithm takes when adjusting the model weights during training. It is a fundamental hyperparameter in optimization algorithms such as Gradient Descent, which is widely used in training machine learning models, including neural networks. <br>
 The learning rate determines the size of the steps the optimization algorithm takes when adjusting the model weights during training. Choosing the learning rate is crucial for effectively training a machine learning model. Too high a learning rate can cause the optimization algorithm to oscillate around the global minimum of the cost function or even diverge, making training unstable. On the other hand, a very low learning rate can cause the optimization algorithm to converge very slowly to the global minimum, significantly increasing training time. Some common methods for adjusting the learning rate during training include:
 - Fixed Learning Rate: Maintain a constant learning rate throughout the training process. This approach is simple but may be sensitive to the choice of initial learning rate.
 - Decreasing Learning Rate: Gradually reduce the learning rate over time as training progresses. This can help ensure smoother convergence of the optimization algorithm.
 - Adaptive Learning Rate: Use adaptive optimization techniques, such as Adam, RMSprop or Adagrad, which automatically adjust the learning rate based on problem characteristics and training progress.

#### Batch Size:
Also known as "batch size", it is an important hyperparameter in machine learning algorithms, especially in deep learning, which involves training neural networks. Refers to the number of training examples that are used in a single iteration (or step) of the training algorithm. Batch size can affect several aspects of the training process and model performance:
- **Training Speed:** Batch size affects the computational efficiency of training. Larger batch sizes generally lead to faster training as fewer weight updates are performed per training epoch.
- **Training Stability:** Smaller batch sizes can result in more frequent weight updates and therefore more stable convergence during training. However, very small batch sizes can introduce noise into the training process.
- **Memory Requirements:** Larger batch sizes require more system memory as more training examples need to be temporarily stored in memory during each training iteration.

The choice of batch size depends on several factors, including the size of the training dataset, model architecture, available computational resources, and desired training stability. Common lot sizes include:
- **Large Batch Size:** Values ​​between 64 and 512 are often used in large datasets and complex model architectures. This provides greater computational efficiency, but may result in less stable convergence.
- **Small Batch Size:** Values ​​between 1 and 32 are common in problems with smaller data sets or when a more stable convergence is desired. This can increase training stability, but often leads to slower training.

#### Epochs:
"Epochs" (or epochs) refer to the number of times the entire training data set is passed through the neural network during the training process. In other words, an epoch is a single pass of all training examples through the model to update the weights and fit it to the data. The number of epochs is an important hyperparameter in training machine learning models and has a significant impact on model performance. Training the model over multiple epochs allows it to more fully learn patterns in the data and improve its generalization ability. <br>
The choice of number of epochs depends on the specific problem, model architecture, dataset size, and other factors. In general, training the model for a sufficient number of epochs is important to ensure that it has enough time to learn patterns in the data. However, it is important to avoid overfitting, where the model learns the training data very well but does not generalize well to new data. This can be done by monitoring model performance on a validation set and stopping training when performance starts to deteriorate.

[Simple implementation of some of the concepts so far](https://colab.research.google.com/drive/1xjey8s1BvlSkszsXm9zSzo2DHOFj1qGi#scrollTo=2XRRlMmY_RQ1)

#### Convolutional Neural Networks (CNN):
 Are a specialized type of deep neural networks designed to process and recognize patterns in matrix data such as images. They are widely used in computer vision tasks, such as image classification, object detection, facial recognition, among others. Its main features are:
- **Convolutional Layers:** CNNs include convolutional layers that apply *convolution operations* to the input data. This allows the network to learn important features of the image, such as edges, textures, and local patterns.
- **Pooling Layers:** After the convolutional layers, CNNs often include pooling layers, such as the max pooling layer, which reduce the dimensionality of the data and help make the representation spatially invariant.
- **Hierarchical Architecture:** CNNs generally have a hierarchical architecture, where the first layers learn low-level features such as edges and textures, and later layers combine these features to learn high-level features such as shapes and objects.
- **Fully Connected Layers:** After the convolutional and pooling layers, CNNs usually include fully connected layers, which combine the learned features to make final predictions, such as classifying the image into different categories.

#### Convolution Operator:
It is used to apply filters to a data matrix, such as an image, to perform operations such as edge detection, smoothing, or feature highlighting. The convolution operator applies a filter (also called a kernel) to an input region, multiplying the pixel values ​​by the filter and summing the results. This process is repeated across all input regions, resulting in a new output matrix, which is generally smaller than the input, depending on the size of the filter and edges. Example using images (2D):
 - **Input (image):** A 2D array of pixel values.
 - **Filter (kernel):** A smaller 2D matrix that defines the operation to be applied.
 - **Convolution:** The filter is slid over the image (as if moving one column at a time from left to right, top to bottom), multiplying and summing the pixel values ​​as defined by the filter matrix.
 - **Output:** A new 2D matrix, resulting from convolution operations.
 - **Shared Weight:** In the context of CNNs, filter weights are shared across all regions of the input, which means that the same filter is applied to all parts of the image. This allows the network to learn spatially invariant features such as edges and textures regardless of location in the image.
- **Local Operations:** The convolution operator is a local operation, which means that it only considers a local region of the input at each step. This helps reduce the number of parameters needed for the network and capture important local patterns.
- **Stride and Padding:** Stride size controls how many positions the filter moves with each step, while padding adds zeros around the edge of the input to maintain the size of the output. These parameters affect the size of the output and the amount of overlap between the input regions.

#### Pooling:
Pooling, also known as subsampling, is a common operation in convolutional neural networks (CNNs) that reduces the dimensionality of data while preserving the most important features. It is applied after the convolutional layers and aims to reduce the spatial size (width and height) of the image representation, while maintaining the most important features. There are different types of pooling, the most common being Max Pooling and Average Pooling.
- **Max Pooling:** In each region (usually square) of the input, the maximum value is selected to be retained in the output. This means that only the most important characteristic of each region is maintained. For example, in a 2x2 region, the maximum value of four pixels is selected and maintained in the output.
- **Average Pooling:** Similar to Max Pooling, but instead of selecting the maximum value, the average value is calculated and retained in the output. This generally produces a smoothing of the image and reduces the amount of noise.
It has some properties such as:
- **Dimensionality Reduction:** Pooling reduces the spatial resolution of the input data, which reduces the number of parameters in the network and, consequently, the computational load and the probability of overfitting.
- **Invariance to Small Translations:** Pooling makes the input representation invariant to small translations of the image, making the model more robust to variations in the position of objects in the image.
- **Preservation of Important Features:** Although it reduces dimensionality, pooling retains the most important features learned in previous convolutional layers.

#### Overfitting:
Also known as overfitting in English, it is a common phenomenon in machine learning models where the model overfits the training data, capturing not only genuine patterns but also noise or randomness in the data. This results in a model that performs very well on the training data, but generalizes poorly to new, unseen data. Its cause is:
- **Complex Model:** Very complex models, with high learning capacity, can capture subtle patterns in the training data, including noise, leading to overfitting.
- **Insufficient Data:** When the training dataset is small relative to the model's complexity, the model may memorize training examples instead of learning general patterns, leading to overfitting.
- **Overtraining:** Overtraining occurs when the model is trained for an excessive number of epochs, allowing it to overfit the weights to the training data.<br>
Symptoms:
- **Different Performance on Training and Test Data:** The model performs very well on training data, but performs significantly worse on test or validation data.
- **Low Generalization:** The model fails to generalize patterns learned in the training data to new unseen data.<br>
How to deal with Overfitting:
- **Regularization:** Techniques such as *L1 or L2 regularization* add penalties to the model weights, reducing model complexity and preventing overfitting.
- **Cross Validation:** Use techniques such as *cross validation* to evaluate model performance on different data sets and identify overfitting.
- **Model Complexity Reduction:** Reduce model complexity, such as reducing the number of layers in a neural network or the number of parameters in a machine learning model.
- **Data Augmentation:** Increasing the size of the training dataset through techniques such as synthetic data generation or data augmentation can help reduce overfitting.

#### L1 and L2 Regularization:
These are techniques used to regularize ML models, including neural networks, by adding regularization terms to the loss function. The objective of these terms is to avoid *overfitting*, penalizing extreme values ​​of the weights of the model parameters. <br>
**L1:**
- **Definition:** L1 regularization, also known as "Lasso regularization", adds to the loss function a term that is proportional to the sum of the absolute values ​​of the weights of the model parameters.
- **Objective:** The L1 regularization term encourages weights to become sparse, that is, many weights will have values ​​close to zero, which can result in automatic feature selection.
- **Formula:** λ * sum(abs(w)), where λ is a hyperparameter that controls the strength of the regularization and w are the weights of the model parameters.

**L2:**
- **Definition:** L2 regularization, also known as "Ridge regularization", adds to the loss function a term that is proportional to the sum of the squares of the weight values ​​of the model parameters.
- **Objective:** The L2 regularization term penalizes the weights of the model parameters, causing them to tend to be smaller, but without forcing them to zero. This helps prevent the weights from growing excessively.
- **Formula:** = λ * sum(w^2), where λ (lambda) is a hyperparameter that controls the strength of the regularization and w are the weights of the model parameters.<br>

Sparseness of Weights:
L1 regularization tends to produce sparse weights (many weights are zero).
L2 regularization tends to produce smaller weights, but not necessarily sparse.<br>
Robustness:
L1 regularization is more robust to the presence of irrelevant or redundant features, as it can lead to automatic feature selection.
L2 regularization is less susceptible to outliers in the data.

Both regularizations are useful for avoiding overfitting and improving the generalization of machine learning models. The choice between L1 and L2 regularization depends on the specific problem and the nature of the data. In many cases, the combination of both, called *Elastic Net*, can be beneficial.

#### Cross-Validation:
It is a statistical technique used to evaluate the performance of a machine learning model and estimate its ability to generalize to new data. It is especially useful when you have a limited dataset, as it allows the dataset to be used more efficiently for model evaluation. How it works:
- **Division of the data set:** The data set is divided into k approximately equal subsets (folds). Generally, k is chosen between 5 and 10, but it can vary depending on the size of the dataset and user preference.
- **Training and Evaluation:** The model is trained k times, each time using k-1 folds as training data and the remaining fold as test data. For each iteration, the model is trained on k-1 folds and evaluated on the fold that was not used for training.
- **Performance Assessment:** After the k iterations, k performance metrics are obtained (such as precision, accuracy, F1-score, etc.), one for each test fold. The overall performance of the model is calculated by averaging the metrics obtained in the k folds.<br>
Benefits of Cross Validation:
- **Better use of data:** All data is used for both training and testing at some point, which provides a more robust evaluation of the model.
- **Evaluation Bias Reduction:** The average of metrics obtained across k folds reduces evaluation bias, providing a more reliable estimate of model performance.
- **Stability Assessment:** The variability of model performance between different folds provides a measure of the stability of the model in relation to variation in the training data.<br>
Types of Cross Validation:
- **K-Fold Cross-Validation:** dataset is divided into k folds, where each fold is used once as test set and remaining k-1 folds are used as training set.
- **Leave-One-Out Cross-Validation (LOOCV):** Each observation is used as test set once, while the remaining k-1 are used as training set. It is an extreme form of k-fold cross-validation, where k is equal to the total number of observations.
- **Stratified Cross-Validation:** Ensures that the distribution of classes in the training and testing folds is similar to the distribution of classes in the original dataset. It is useful for imbalanced datasets.

#### Flattening:
Is a concept used in neural networks, especially in convolutional neural networks (CNNs), to transform a multidimensional matrix into a one-dimensional vector. This operation is commonly used in preparation for the output layer of a neural network, where data needs to be transformed into a format suitable for classification or regression. It works as follows:
- **Multidimensional Input:** In the convolutional layers of a CNN, the input data is typically represented in a multidimensional matrix, where each dimension corresponds to a feature or channel.
- **Vector Transformation:** Flattening is performed by applying a "flattening" operation to the output of the last convolutional layer, where all dimensions are combined into a single one-dimensional vector.
- **Linear Output:** The result is a linear vector that contains all the feature information extracted by the convolutional layers, ready to be fed into the fully connected (dense) layers of the neural network for final classification.<br>
Example:
Suppose we have a feature matrix output from a convolutional layer with dimensions 3x3x64, where:
- 3x3 is the height and width of the feature matrix.
- 64 is the number of channels (or features) produced by convolutional filters.<br>
To apply flattening, we transform this 3D matrix into a one-dimensional vector of size 3x3x64 = 576, which is the final result of the flattening process. <br>
Flattening is commonly used in neural networks, especially CNNs, as a preprocessing step before dense (fully connected) layers for classification or regression. It allows all the information extracted by the convolutional layers to be flattened into a single vector so that it can be fed into the dense layers for final decision making.

[Implementation of concepts for image classification](https://colab.research.google.com/drive/1aybJl8rk7JfDPYgXUCNRIgpoK64uwpYD#scrollTo=OW0Qw73eWg1_)
