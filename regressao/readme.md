## Capítulo 5: Regressão

### Conceito:
As regressões são técnicas estatísticas e de aprendizado de máquina utilizadas para prever valores contínuos ou categorizados com base em variáveis independentes. 

### Alguns tipos:
_**Regressão Linear:**_ Regressão linear: É um método estatístico usado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. Tem como ideia básica, encontrar a linha (ou um hiperplano em múltiplas dimensões) que melhor se ajusta aos dados, traçando uma possível previsão, minimizando a soma dos quadrados das diferenças dos valores observados (em um plano x, y ou x, y, z como exemplo) e os valores previstos pela linha.
  - Fórmula Regressão linear simples: y = a + bx, sendo a uma constante sem a influência a outro coeficiente (é o coeficiente linear) e b sempre multiplicado por x é o coeficiente angular (variável preditora).
  - Fórmula Regressão linear composta: a + b . x + b2 . x2 + b3 . x3 + … + bn . xn, onde cada bx são coeficientes angulares (variáveis preditoras).

[Implementando Regressão Linear](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_linear.py)

_**Regressão Polinomial:**_ Permite modelar relações não lineares entre as variáveis. Ao invés de modelar a relação como uma linha reta, essa regressão modela como uma curva ou superfície.

[Implementando Regressão Polinomial](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_polinomial.py)

![Regressão Polinomial](https://aprenderdatascience.com/wp-content/uploads/2021/02/polinomial.jpeg.webp)

_**Regressão Logística:**_ Método usado para modelar a probabilidade de um evento ocorrer como em uma função de preditores (variáveis independentes). É uma forma de regressão linear que é usada para problemas de classificação binária. A saída é uma probabilidade entre 0 e 1, que pode ser interpretada como a chance de um evento ocorrer.
> Fórmula da regressão logística:
> y = a + b . x + b2 . x2 + b3 . x3 + … + bn . xn + e, onde ‘e’ é o erro do modelo. É bem semelhante à regressão linear, a diferença é que o resultado saem no formato verdadeiro e falso (0, 1) enquanto o modelo linear tenta prever valores literais (não binários)

[Implementando Regressão Logística](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_logistica.py)

_**Regressão de Ridge:**_ É uma técnica de regularização que é usada para prevenir o overfitting em modelos de regressão linear. Ela adiciona um termo de penalidade L2 ao modelo, que é a soma dos quadrados dos coeficientes do modelo. Isso resulta em um modelo com coeficientes menores, o que pode ajudar a evitar que o modelo se ajuste demais aos dados de treinamento e melhore a generalização para dados não vistos.
[link útil para estudo](https://edisciplinas.usp.br/pluginfile.php/8074854/mod_resource/content/1/Regressão%20Ridge.pdf)

[Implementando Regressão de Ridge](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_ridge.py)

_**Regressão de Lasso (Least Absolute Shrinkage and Selection Operator):**_ É uma técnica de regularização que é usada para prevenir o overfitting em modelos de regressão linear. Ela adiciona um termo de penalidade L1 aos coeficientes do modelo, o que resulta em alguns coeficientes sendo exatamente zero. Isso pode ser útil para selecionar automaticamente as variáveis mais importantes e para lidar com a multicolinearidade*.
> Multicolinearidade: definida como a presença de um alto grau de correlação entre as variáveis independentes
 
[Implementando Regressão de Lasso](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_lasso.py)

![Regressão de Ridge e Lasso](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFcbmsnHAhVjMAs7FMDsDXD9r6fqJs_mnBrA&s)

_**Regressão Elástica (Elastic Net):**_ É uma técnica de regularização que combina os termos de penalidade L1 e L2 da Regressão de Lasso e da Regressão de Ridge. Isso resulta em um modelo com coeficientes menores, o que pode ajudar a prevenir o overfitting, e também pode levar a um modelo com alguns coeficientes exatamente zero, o que pode ser útil para selecionar automaticamente as variáveis mais importantes.
![Elastic net](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlXfLQPiEV7fTod3KbYXtdqj9W1UOSBiI5yw&s)

[Implementando Regressão de Elástica](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_elastica.py)

_**Regressão de Decisão:**_: É um método de aprendizado de máquina que combina várias técnicas de aprendizado de máquina para fazer previsões. Ela é baseada na ideia de que diferentes modelos podem ser mais eficazes para diferentes partes do espaço de entrada. A Regressão de Decisão usa uma combinação de modelos de aprendizado de máquina para fazer previsões, escolhendo o modelo mais apropriado para cada ponto de dados com base em seu valor de entrada.
A Regressão de Decisão funciona dividindo o espaço de entrada em regiões e atribuindo a cada região um modelo de aprendizado de máquina diferente. Quando um novo ponto de dados é apresentado, o algoritmo determina qual região ele pertence e usa o modelo de aprendizado de máquina correspondente para fazer a previsão.

[Implementando Regressão de Decisão](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_de_decisao.py)

_**Regressão de Random Forest:**_ É um método de aprendizado de máquina que combina múltiplas árvores de decisão para fazer previsões. Cada árvore de decisão é treinada em um subconjunto aleatório dos dados de treinamento, e a previsão final é a média das previsões de todas as árvores. A Regressão de Random Forest é conhecida por sua robustez e capacidade de lidar com dados com muitas variáveis independentes e dados não lineares.
Como Funciona a Regressão de Random Forest:
 - *Seleção Aleatória de Dados:* Para cada árvore de decisão, um subconjunto aleatório dos dados de treinamento é selecionado.
 - *Seleção Aleatória de Variáveis:* Para cada nó em uma árvore de decisão, um subconjunto aleatório das variáveis independentes é selecionado.
 - *Divisão dos Dados:* Os dados são divididos com base nos valores das variáveis selecionadas, criando novos nós.
 - *Previsão:* A previsão é feita calculando a média das previsões de todas as árvores de decisão.
<br>

[Implementando Random Forest](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_random_forest.py)

![Random Forest](https://cnvrg.io/wp-content/uploads/2021/02/Random-Forest-Algorithm-1024x576.jpg)

_**Regressão de Gradiente:**_ É um método de otimização iterativa usado para encontrar os coeficientes de um modelo de regressão que minimizam a função de perda. A ideia básica é ajustar os coeficientes do modelo em direção à direção que reduz a função de perda. Este processo é repetido até que a função de perda não possa ser reduzida mais ou até que um critério de parada seja atingido.
Como Funciona a Regressão de Gradiente:
 - Inicialização: Os coeficientes do modelo são inicializados com valores aleatórios ou zero.
 - Cálculo do Gradiente: O gradiente da função de perda em relação aos coeficientes é calculado. O gradiente indica a direção de maior aumento da função de perda.
 - Atualização dos Coeficientes: Os coeficientes são atualizados na direção oposta ao gradiente, o que geralmente resulta em uma redução da função de perda.
 - Repetição: O processo de cálculo do gradiente e atualização dos coeficientes é repetido até que a função de perda não possa ser reduzida mais ou até que um critério de parada seja atingido (por exemplo, um número máximo de iterações).

[Implementando Gradiente](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_de_gradiente.py)

_**Regressão de Support Vector:**_ É uma extensão da técnica de Support Vector Machine (SVM) para problemas de regressão. A SVM é um algoritmo de aprendizado de máquina que é usado para classificação e regressão. A ideia central da SVM é encontrar um hiperplano que separa os dados de treinamento de forma otimizada, minimizando o erro entre os pontos de dados e o hiperplano.
A Regressão de Support Vector funciona de maneira semelhante à SVM de classificação, mas com algumas diferenças chave:
 - Definição do Problema: Em vez de encontrar um hiperplano que separa duas classes de dados, a SVR procura encontrar um hiperplano que minimiza o erro quadrático médio (Mean Squared Error - MSE) entre os pontos de dados e o hiperplano.
 - Seleção do Hiperplano: A SVR usa um conceito chamado "margem de tolerância" (tolerance margin) para determinar o hiperplano. A margem de tolerância é uma medida de quão longe os pontos de dados podem estar do hiperplano sem serem considerados erros.
 - Ajuste do Modelo: O modelo é ajustado para minimizar o erro quadrático médio, levando em consideração a margem de tolerância.

[Implementando Support Vector](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_support_vector.py)

_**Regressão de K-Nearest Neighbors (KNN):**_ É um método de aprendizado de máquina não supervisionado que pode ser usado tanto para problemas de classificação quanto de regressão. A ideia básica do KNN é que, para prever o valor de uma variável dependente para um novo ponto de dados, você procura os k pontos de dados mais próximos no conjunto de treinamento e usa a média (para regressão) ou a moda (para classificação) dos valores desses vizinhos mais próximos como previsão.
Como Funciona a Regressão de K-Nearest Neighbors:
- Seleção dos Vizinhos: Para cada ponto de dados no conjunto de teste, os k pontos de dados mais próximos no conjunto de treinamento são identificados. A proximidade é geralmente medida usando a distância euclidiana.
- Previsão: A previsão para o ponto de dados de teste é feita calculando a média dos valores da variável dependente dos k vizinhos mais próximos.

[Implementando KNN](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_knn.py)

#

## Chapter 5: Regression

### Concept:
Regressions are statistical and machine learning techniques used to predict continuous or binned values ​​based on independent variables.

### Some types:
_**Linear Regression:**_ Linear regression: It is a statistical method used to model the relationship between a dependent variable and one or more independent variables. Its basic idea is to find the line (or a hyperplane in multiple dimensions) that best fits the data, tracing a possible prediction, minimizing the sum of the squares of the differences in the observed values ​​(in a plane x, y or x, y, z as an example) and the values ​​predicted by the line.
  - Simple linear regression formula: y = a + bx, with a being a constant without the influence of another coefficient (it is the linear coefficient) and b always multiplied by x is the angular coefficient (predictor variable).
  - Composite linear regression formula: a + b . x + b2 . x2 + b3 . x3 + … + bn . xn, where each bx are angular coefficients (predictor variables).

[Implementing Linear Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_linear.py)

_**Polynomial Regression:**_ Allows you to model non-linear relationships between variables. Rather than modeling the relationship as a straight line, this regression models it as a curve or surface.
![Polynomial Regression](https://aprenderdatascience.com/wp-content/uploads/2021/02/polinomial.jpeg.webp)

[Implementing Polynomial Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_polinomial.py)

_**Logistic Regression:**_ Method used to model the probability of an event occurring as a function of predictors (independent variables). It is a form of linear regression that is used for binary classification problems. The output is a probability between 0 and 1, which can be interpreted as the chance of an event occurring.
> Logistic regression formula:
> y = a + b . x + b2 . x2 + b3 . x3 + … + bn . xn + e, where ‘e’ is the model error. It is very similar to linear regression, the difference is that the results come out in true and false format (0, 1) while the linear model tries to predict literal (non-binary) values.

[Implementing Logistic Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_logistica.py)

_**Ridge Regression:**_ It is a regularization technique that is used to prevent overfitting in linear regression models. It adds an L2 penalty term to the model, which is the sum of the squares of the model coefficients. This results in a model with smaller coefficients, which can help prevent the model from overfitting the training data and improve generalization to unseen data.
[useful link for study](https://edisciplinas.usp.br/pluginfile.php/8074854/mod_resource/content/1/Regressão%20Ridge.pdf)

[Implementing Ridge Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_ridge.py)

_**Lasso Regression (Least Absolute Shrinkage and Selection Operator):**_ It is a regularization technique that is used to prevent overfitting in linear regression models. It adds an L1 penalty term to the model coefficients, which results in some coefficients being exactly zero. This can be useful for automatically selecting the most important variables and for dealing with multicollinearity*.
> Multicollinearity: defined as the presence of a high degree of correlation between the independent variables

[Implementing Lasso Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_lasso.py)

![Ridge and Lasso Regression](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFcbmsnHAhVjMAs7FMDsDXD9r6fqJs_mnBrA&s)

_**Elastic Regression (Elastic Net):**_ It is a regularization technique that combines the L1 and L2 penalty terms of Lasso Regression and Ridge Regression. This results in a model with smaller coefficients, which can help prevent overfitting, and can also lead to a model with some coefficients that are exactly zero, which can be useful for automatically selecting the most important variables.

[Implementing Elastic Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_elastica.py)

![Elastic net](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlXfLQPiEV7fTod3KbYXtdqj9W1UOSBiI5yw&s)


_**Decision Regression:**_: It is a machine learning method that combines various machine learning techniques to make predictions. It is based on the idea that different models may be more effective for different parts of the input space. Decision Regression uses a combination of machine learning models to make predictions, choosing the most appropriate model for each data point based on its input value.
Decision Regression works by dividing the input space into regions and assigning each region a different machine learning model. When a new data point is presented, the algorithm determines which region it belongs to and uses the corresponding machine learning model to make the prediction.

[Implementing Decision Regression](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_de_decisao.py)

_**Random Forest Regression:**_ It is a machine learning method that combines multiple decision trees to make predictions. Each decision tree is trained on a random subset of the training data, and the final prediction is the average of the predictions from all trees. Random Forest Regression is known for its robustness and ability to handle data with many independent variables and non-linear data.
How Random Forest Regression Works:
 - *Random Data Selection:* For each decision tree, a random subset of the training data is selected.
 - *Random Variable Selection:* For each node in a decision tree, a random subset of the independent variables is selected.
 - *Data Division:* The data is divided based on the values ​​of the selected variables, creating new nodes.
 - *Prediction:* The prediction is made by calculating the average of the predictions of all decision trees.

[Implementing Random Forest](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_random_forest.py)

![Random Forest](https://cnvrg.io/wp-content/uploads/2021/02/Random-Forest-Algorithm-1024x576.jpg)

_**Gradient Regression:**_ It is an iterative optimization method used to find the coefficients of a regression model that minimize the loss function. The basic idea is to adjust the model coefficients toward the direction that reduces the loss function. This process is repeated until the loss function cannot be reduced any further or until a stopping criterion is reached.
How Gradient Regression Works:
 - Initialization: Model coefficients are initialized to random values ​​or zero.
 - Gradient Calculation: The gradient of the loss function with respect to the coefficients is calculated. The gradient indicates the direction of greatest increase in the loss function.
 - Coefficient Update: Coefficients are updated in the opposite direction to the gradient, which generally results in a reduction in the loss function.
 - Repetition: The process of calculating the gradient and updating the coefficients is repeated until the loss function cannot be reduced any further or until a stopping criterion is reached (e.g. a maximum number of iterations).

[Implementing Gradiente](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_de_gradiente.py)

_**Support Vector Regression:**_ It is an extension of the Support Vector Machine (SVM) technique for regression problems. SVM is a machine learning algorithm that is used for classification and regression. The central idea of ​​SVM is to find a hyperplane that optimally separates the training data, minimizing the error between the data points and the hyperplane.
Support Vector Regression works in a similar way to classification SVM, but with some key differences:
 - Problem Definition: Instead of finding a hyperplane that separates two classes of data, SVR seeks to find a hyperplane that minimizes the mean squared error (MSE) between the data points and the hyperplane.
 - Hyperplane Selection: SVR uses a concept called "tolerance margin" to determine the hyperplane. The tolerance margin is a measure of how far data points can be from the hyperplane without being considered errors.
 - Model Adjustment: The model is adjusted to minimize the mean squared error, taking into account the tolerance margin.

[Implementando Support Vector](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_support_vector.py)

_**K-Nearest Neighbors Regression (KNN):**_ It is an unsupervised machine learning method that can be used for both classification and regression problems. The basic idea of ​​KNN is that to predict the value of a dependent variable for a new data point, you look for the k closest data points in the training set and use the mean (for regression) or the mode (for classification). ) of the values ​​of these nearest neighbors as a prediction.
How K-Nearest Neighbors Regression Works:
- Neighbor Selection: For each data point in the test set, the k closest data points in the training set are identified. Proximity is usually measured using Euclidean distance.
- Prediction: The prediction for the test data point is made by calculating the average of the dependent variable values ​​of the k nearest neighbors.

[Implementing KNN](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/regressao/regressao_knn.py)
