## Capítulo 4: Classificação

### Conceito:
É um tipo de aprendizado supervisionado que envolve o uso de algoritmos de machine learning (M.L.) para categorizar dados em diferentes classes ou categorias. Tem como objetivo principal, prever uma classe ou categoria de um novo dado com base em exemplos de treinamentos anteriores.
Funciona da seguinte forma:
 - Coleta de dados: Um conjunto de dados é coletado. Esse conjunto é composto por exemplos de treinamento, onde cada exemplo é um par de “entrada-saída”, onde “entrada” é o conjunto de características do dado e a saída é a classe/categoria a qual o dado pertence.
 - Treinamento do modelo: O algoritmo de aprendizado de máquina é treinado com os dados separados na etapa anterior. Durante o treinamento, o algoritmo aprende a relação entre as características dos dados de entrada e suas classes correspondentes.
 - Teste do modelo: Após o treinamento, o modelo é testado em  um conjunto de dados de teste separado para avaliar sua precisão. Sendo o conjunto de dados de teste, diferentes do conjunto utilizado no treinamento para evitar vieses ou vícios
 - Previsão: O modelo treinado é usado para prever a classe de novos dados. A entrada é processada pelo modelo, que então produz uma saída que representa a classe prevista.

### Alguns tipos:
#### Naïve Bayes:
É um método de machine learning baseado no teorema de Bayes (Naive Bayes: entenda o que é e como funciona esse algoritmo! (voitto.com.br)), que é uma ferramenta estatística para calcular probabilidades condicionais. “Naïve” (ingênuo) é usado pois o algoritmo assume que todas as características (variáveis independentes) em um conjunto de dados são mutuamente independentes, o que na prática raramente acontece. 
Fórmula: P(A/B) = P(B/A) x P(A) / P(B), traduz-se:
 - P(A/B) -> é a probabilidade que a classe A, seja verdadeira dado o conjunto de características (B)
 - P(B/A) -> É a probabilidade de que o conjunto de características (B) ocorra da classe (A) como verdadeira
 - P(A) -> é a probabilidade a priori da classe (A)
 - P(B) -> é a probabilidade do conjunto de características (B)
##### Como funciona:
 - Cálculo da probabilidade A priori: Calcula-se a probabilidade a priori de cada classe. É feito dividindo o número de exemplos de cada classe pelo número total de exemplos.
 - Cálculo da probabilidade condicional: Em seguida, para cada classe, calcula-se a probabilidade condicional dado que a classe é verdadeira, dividindo o número de exemplos que tem a característica e pertencem à classe pelo número total de exemplos que pertencem à classe.
 - Cálculo da Probabilidade do Conjunto de Características: A probabilidade do conjunto de características (B) é calculada como o produto das probabilidades condicionais de cada característica dado que a classe é verdadeira.
 - Classificação: Finalmente, para um novo exemplo (B), o algoritmo calcula a probabilidade de cada classe ser a verdadeira usando a fórmula acima e classifica o exemplo na classe com a maior probabilidade.

É uma abordagem simples e eficaz para muitos problemas de classificação, especialmente quando o conjunto de dados é grande e as características são independentes.

[Implementação Naïve Bayes](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/naive_bayes.py)

#### Árvores de decisão:
São usadas tanto para problemas de classificação quanto de regressão [próximo capítulo](https://github.com/p3dru/inteligencia_artificial_machine_learning/tree/main/regressao). São ferramentas poderosas para modelar decisões e prever resultados com base em um conjunto de regras.
##### Como funcionam:
Uma árvore de decisão é uma estrutura de dados que começa com um nó raiz e se ramifica em vários filhos, cada um representando uma decisão ou uma condição. Cada nó interno na árvore representa uma decisão baseada em uma característica do conjunto de dados e cada nó folha representa uma decisão ou previsão.<br>
O processo de construção de uma árvore de decisão envolve a seleção de características e valores que melhor separam os dados em classes distintas, com o objetivo de minimizar a impureza dos nós. A impureza é medida por métricas como o índice de Gini* ou a Entropia*.
> Índice Gini: É uma medida que varia de 0 à 1, onde 0 indica a separação perfeita dos dados (todos os dados pertencem somente à uma classe) e 1 indica uma separação totalmente aleatória (os dados estão distribuídos igualmente entre as classes, sendo que os dados possuem mais de uma classe).<br>
> Entropia: A entropia é uma medida que também varia de 0 a 1, onde 0 indica uma separação perfeita dos dados e 1 indica uma separação totalmente aleatória. A entropia é baseada no conceito de informação de Shannon.
<br>

[Artigo mais detalhado sobre Árvores de decisão](https://www.vooo.pro/insights/um-tutorial-completo-sobre-a-modelagem-baseada-em-tree-arvore-do-zero-em-r-python/)

[Implementação de Árvores de Decisão](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/arvores%20_de_decisao.py)

#### Aprendizagem por regras:
É um método de aprendizado de máquina que gera um conjunto de regras que podem ser usadas para fazer previsões ou tomar decisões. Essas regras são derivadas de um conjunto de dados de treinamento e são projetadas para capturar padrões e relações entre as características dos dados e a variável de saída. <br>
Essa aprendizagem envolve a identificação de padrões nos dados de treinamento que podem ser usados para formar regras. Essas regras então são aplicadas  a novo dados para fazer previsões ou tomar  decisões. Como funciona:
 - Identificação de padrões: Usando algoritmos de Machine Learning (ML), identifica  padrões nos dados de treinamento.
 - Formulação de regras: Com base nos padrões identificados, formula regras que possam ser usadas para prever a variável de saída.
 - Aplicação das regras: Aplica as regras formuladas a novos dados para fazer previsões ou tomar decisões.

[Implementação de Aprendizagem por Regras](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/aprendizado_por_regras.py)

#### Aprendizagem baseadas em instâncias - KNN: 
É um tipo de machine learning que não faz generalizações a partir de um conjunto de dados de treinamento, mas simplesmente memoriza os exemplos de treinamento.
##### Como funciona:
O KNN encontra os “k” mais próxima do conjunto de treinamento para um novo exemplo e fazendo uma previsão com base na classe mais frequente entre os “k’s” vizinhos. Basicamente define a classe de ‘k’ pela distância da classe vizinha mais próxima, distancia essa medida usando distância euclidiana, além de algumas outras. <br>
É um algoritmo simples e intuitivo, mas pode ser computacionalmente caro para grandes conjuntos de dados, pois requer a comparação do novo exemplo com todos os exemplos de treinamento. Além disso, a escolha do valor de k (o número de vizinhos mais próximos a serem considerados) pode ter um grande impacto no desempenho do modelo.

[Implementação KNN](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/aprendizado_knn.py)

#### Aprendizagem com máquinas de vetores de suporte - SVM:
Funciona tentando maximizar a margem entre as classes, que e feito encontrando um hiperplano (linha em 2d ou um plano em 3d) que separa as classes com o maior espaço possível. Os pontos de dados que estão próximos da fronteira de separação, são chamados de suportes de vetor. O objetivo é encontrar a fronteira de separação que maximize a distância entre os suportes de vetor e a fronteira.<br>
O SVM é um algoritmo poderoso e flexível que pode lidar com problemas de classificação e regressão em uma ampla gama de aplicações. A escolha do kernel (neste exemplo, linear) e do parâmetro de regularização C (explicado no código) são cruciais para o desempenho do modelo. O kernel linear é adequado para problemas linearmente separáveis, enquanto outros kernels podem ser usados para problemas que não são linearmente separáveis.

#### Regressão Logística:
Explicado mais detalhadamente no [próximo capítulo](https://github.com/p3dru/inteligencia_artificial_machine_learning/tree/main/regressao).

#### Validação Cruzada:
É uma técnica estatística usada para avaliar a capacidade de generalização de um modelo de aprendizado de máquina. Ela divide o conjunto de dados em um número específico de subconjuntos (ou "folds"), treina o modelo em um subconjunto e testa o modelo nos outros subconjuntos. Isso é feito várias vezes, com cada subconjunto sendo usado uma vez como conjunto de teste e as outras vezes como conjunto de treinamento. A média das métricas de desempenho obtidas em cada iteração é usada para avaliar o modelo.<br>
É particularmente útil quando o conjunto de dados é pequeno, pois permite que o modelo seja avaliado de forma mais robusta do que simplesmente dividir os dados em conjuntos de treinamento e teste.
##### Tipos:
 - Validação cruzada K-folds: O conjunto de dados é dividido em ‘K’  subconjuntos. O modelo é treinado k vezez e em cada vez k -1 dos subconjuntos é testado no subconjunto restante.
 - Validação cruzada de tempo (time series):  Especificamente para séries temporais, onde a ordem dos dados é importante. Neste caso, os dados são divididos em um conjunto de treinamento e um conjunto de teste, onde o conjunto de treinamento contém dados anteriores ao conjunto de teste.

É uma ferramenta poderosa para avaliar a robustez e a capacidade de generalização de um modelo de aprendizado de máquina. Ela permite que você obtenha uma estimativa mais confiável do desempenho do modelo em dados não vistos.

[Implementação Validação Cruzada](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/validacao_cruzada.py)

#

## Chapter 4: Classification

### Concept:
It is a type of supervised learning that involves using machine learning (ML) algorithms to categorize data into different classes or categories. Its main objective is to predict a class or category of new data based on previous training examples.
It works as follows:
 - Data collection: A set of data is collected. This set is composed of training examples, where each example is an “input-output” pair, where “input” is the set of characteristics of the data and the output is the class/category to which the data belongs.
 - Model training: The machine learning algorithm is trained with the data separated in the previous step. During training, the algorithm learns the relationship between the features of the input data and their corresponding classes.
 - Model testing: After training, the model is tested on a separate test dataset to evaluate its accuracy. Being the test data set, different from the set used in training to avoid biases or vices
 - Prediction: The trained model is used to predict the class of new data. The input is processed by the model, which then produces an output that represents the predicted class.

### Some types:
#### Naïve Bayes:
It is a machine learning method based on Bayes' theorem (Naive Bayes: understand what this algorithm is and how it works! (voitto.com.br)), which is a statistical tool for calculating conditional probabilities. “Naïve” is used because the algorithm assumes that all features (independent variables) in a data set are mutually independent, which in practice rarely happens.
Formula: P(A/B) = P(B/A) x P(A) / P(B), translates as:
 - P(A/B) -> is the probability that class A is true given the set of characteristics (B)
 - P(B/A) -> It is the probability that the set of characteristics (B) occurs in class (A) as true
 - P(A) -> is the a priori probability of class (A)
 - P(B) -> is the probability of the set of characteristics (B)
##### How it works:
 - Calculation of A priori probability: Calculate the a priori probability of each class. It is done by dividing the number of examples of each class by the total number of examples.
 - Calculation of the conditional probability: Then, for each class, the conditional probability is calculated given that the class is true, dividing the number of examples that have the characteristic and belong to the class by the total number of examples that belong to the class.
 - Calculation of the Probability of the Set of Features: The probability of the set of features (B) is calculated as the product of the conditional probabilities of each feature given that the class is true.
 - Classification: Finally, for a new example (B), the algorithm calculates the probability of each class being true using the formula above and classifies the example into the class with the highest probability.

It is a simple and effective approach for many classification problems, especially when the data set is large and the features are independent.

[Naïve Bayes implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/naive_bayes.py)

#### Decision trees:
They are used for both classification and regression problems [next chapter](https://github.com/p3dru/inteligencia_artificial_machine_learning/tree/main/regressao). They are powerful tools for modeling decisions and predicting outcomes based on a set of rules.
##### How they work:
A decision tree is a data structure that starts with a root node and branches into multiple children, each representing a decision or a condition. Each internal node in the tree represents a decision based on a characteristic of the data set, and each leaf node represents a decision or prediction.<br>
The process of building a decision tree involves selecting characteristics and values ​​that best separate data into distinct classes, with the aim of minimizing node impurity. Impurity is measured by metrics such as the Gini index* or Entropy*.
> Gini Index: It is a measure that varies from 0 to 1, where 0 indicates perfect separation of data (all data belongs to only one class) and 1 indicates a completely random separation (data are distributed equally between classes, being data has more than one class).<br>
> Entropy: Entropy is a measurement that also varies from 0 to 1, where 0 indicates a perfect separation of data and 1 indicates a completely random separation. Entropy is based on Shannon's concept of information.
<br>

[More detailed article on Decision Trees](https://www.vooo.pro/insights/um-tutorial-completo-sobre-a-modelagem-baseada-em-tree-arvore-do-zero-em-r-python/)

[Implementation of Decision Trees](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/arvores%20_de_decisao.py)

#### Learning by rules:
It is a machine learning method that generates a set of rules that can be used to make predictions or make decisions. These rules are derived from a training data set and are designed to capture patterns and relationships between data characteristics and the output variable. <br>
This learning involves identifying patterns in the training data that can be used to form rules. These rules are then applied to new data to make predictions or decisions. How it works:
 - Pattern identification: Using Machine Learning (ML) algorithms, identifies patterns in training data.
 - Rule formulation: Based on the identified patterns, formulates rules that can be used to predict the output variable.
 - Application of rules: Apply formulated rules to new data to make predictions or make decisions.

[Implementation of Learning by Rules](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/aprendizado_por_regras.py)

#### Instance-based learning - KNN:
It is a type of machine learning that does not make generalizations from a training data set, but simply memorizes the training examples.
##### How it works:
KNN finds the “k” closest to the training set for a new example and makes a prediction based on the most frequent class among the neighboring “k’s”. Basically it defines the class of ‘k’ by the distance from the nearest neighboring class, distance this measurement using Euclidean distance, in addition to some others. <br>
It is a simple and intuitive algorithm, but it can be computationally expensive for large data sets as it requires comparing the new example with all training examples. Furthermore, the choice of the value of k (the number of nearest neighbors to consider) can have a large impact on model performance.

[KNN implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/aprendizado_knn.py)

#### Learning with support vector machines - SVM:
It works by trying to maximize the margin between classes, which is done by finding a hyperplane (2d line or 3d plane) that separates the classes with as much space as possible. Data points that are close to the separation boundary are called vector supports. The goal is to find the separation boundary that maximizes the distance between the vector supports and the boundary.<br>
SVM is a powerful and flexible algorithm that can handle classification and regression problems in a wide range of applications. The choice of the kernel (in this example, linear) and the regularization parameter C (explained in the code) are crucial for the model's performance. The linear kernel is suitable for linearly separable problems, while other kernels can be used for problems that are not linearly separable.

#### Logistic Regression:
Explained in more detail in the [next chapter](https://github.com/p3dru/inteligencia_artificial_machine_learning/tree/main/regressao).

#### Cross Validation:
It is a statistical technique used to evaluate the generalization ability of a machine learning model. It divides the dataset into a specific number of subsets (or "folds"), trains the model on one subset, and tests the model on the other subsets. This is done multiple times, with each subset being used once as a test set and the other times as a training set. The average of the performance metrics obtained in each iteration is used to evaluate the model.<br>
It is particularly useful when the dataset is small, as it allows the model to be evaluated more robustly than simply splitting the data into training and testing sets.
##### Types:
 - K-folds cross-validation: The dataset is divided into ‘K’ subsets. The model is trained k times and each time k -1 of the subsets is tested on the remaining subset.
 - Time cross-validation (time series): Specifically for time series, where the order of the data is important. In this case, the data is divided into a training set and a test set, where the training set contains data prior to the test set.

It is a powerful tool for evaluating the robustness and generalizability of a machine learning model. It allows you to get a more reliable estimate of model performance on unseen data.

[Cross Validation Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/classificacao/validacao_cruzada.py)
