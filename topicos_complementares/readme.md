## Capítulo 8: Tópicos complementares

### Pré-processamento:
É uma etapa crucial o pipeline* de aprendizado de máquina que envolve a limpeza e transformação dos dados brutos para que estejam em um formato adequado para serem usados. Sempre é interessante estudar quais técnicas utilizar.
> Pipeline: Um pipeline em aprendizado de máquina é uma sequência de etapas de processamento de dados que transformam os dados brutos em insights úteis. O pipeline automatiza o fluxo de trabalho de aprendizado de máquina, facilitando a execução de tarefas complexas e melhorando a eficiência e a reprodutibilidade do processo. Pré-processamento -> Seleção de atributos -> Modelagem -> Avaliação -> Implantação.
### Algumas técnicas:
 - _**Valores faltantes:**_ Podemos lidar de diversas formas, como, substituindo  valores faltantes por um específico como média, mediana ou moda dos valores existentes na coluna (imputação), remoção de linhas ou colunas que contêm valores que contém linhas faltantes (deleção), estimação dos valores com base em valores existentes, como interpolação linear* para dados sequenciais (interpolação), utilização de um modelo de aprendizado de máquina para prever os valores faltantes com base em outras características (modelo de previsão). <br>[Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/dados_faltantes.py)
 - _**Normalização:**_ É uma técnica usada para transformar os valores de variáveis numéricas em uma escala comum, sem distorcer as diferenças nos intervalos de valores ou na distribuição dos dados. Se os recursos (dados) estiverem em escalas diferentes, o algoritmo pode dar mais peso a recursos com maiores valores, o que pode levar a resultados relativamente inferiores.<br> [Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/normalizacao.py)
 - _**Discretização:**_ É o processo de transformar variáveis contínuas em variáveis categóricas. É feito dividindo o intervalo de valores possíveis da variável em um número fixo de intervalos (bins). Exemplos: MIN-MAX e Z-Score. <br>[Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/discretizacao.py)
  > Normalização MIN-MAX: Redimensiona os valores para um intervalo específico, geralmente entre 0 e 1. (Buscar a fórmula para a normalização).<br>
  > Normalização Z-Score: Redimensiona os valores para terem uma média de 0 e um desvio padrão de 1.
 - _**Seleção de atributos:**_  Envolve a escolha de um subconjunto de atributos de um conjunto de dados para usar em um modelo de aprendizado de máquina. Pode ser feita por várias razões, incluindo a redução de dimensionalidade, melhoria na eficiência computacional e o risco de overfitting. Pode ser feita tanto manualmente quanto usando técnicas estatísticas. Alguns exemplos:
    - *Seleção de atributos univariados:* Avalia a importância de cada atributo individualmente, sem considerar as interações entre atributos. Uma abordagem comum é usar medidas de correlação, como o coeficiente de correlação de Pearson, para medir a força da relação entre cada atributo e a variável de destino.
    - *Seleção de Atributos Recursivos:* Esta técnica usa algoritmos de aprendizado de máquina para construir um modelo de aprendizado de máquina (como uma árvore de decisão ou uma floresta aleatória) e, em seguida, seleciona os atributos que contribuem mais para a construção do modelo.
    - *Seleção de atributos Multivariados:* Esta técnica considera as interações entre atributos. Uma abordagem comum é usar métodos de importância de atributos que levam em conta as interações entre atributos, como o método de importância de atributos de floresta aleatória.
    - *Seleção de Atributos Baseada em Modelos:* Esta técnica usa modelos de aprendizado de máquina para selecionar os atributos que são mais importantes para a previsão da variável de destino. Por exemplo, o método de importância de atributos de floresta aleatória pode ser usado para selecionar os atributos mais importantes
   <br> [Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/selecao_atributos.py)
 - _**Redução de dimensionalidade:**_ Visa reduzir o número de variáveis em um conjunto de dados, mantendo a maior quantidade possível de informação, é importante pois melhora a eficiência computacional, pois excluindo dados menos relevantes, os algoritmos precisam processar menos dados. Facilita a visualização de dados em espaços com menor dimensão com em 2D e 3D, o que pode ser útil para a análise exploratória e interpretação dos dados. Reduz o risco de overfitting, pois com menos variáveis, os algoritmos são  menos propensos a capturar ruídos nos dados, além de melhorar a interpretabilidade. Existem várias técnicas de redução de dimensionalidade, incluindo:
    - *PCA (Análise de Componentes Principais):* Transforma o conjunto de dados e um novo conjunto, de variáveis não correlacionadas (ortogonais) e que capturam a maior variância nos dados originais.
    - *T-SNE (T- Distributed Stochastic Neighbor Embedding):* Particularmente útil para a visualização de dados de alta dimensão. Preserva as distâncias locais entre os pontos de dados, o que pode ser útil para identificar clusters e estuturas de dados.<br> [Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/reducao_de_dimensionalidade.py)
 - _**Agrupamento:**_ O agrupamento é uma técnica de aprendizado de máquina não supervisionada que agrupa dados semelhantes em grupos ou clusters. O objetivo do agrupamento é identificar estruturas ou padrões nos dados que não são facilmente acessíveis por meio de métodos de análise estatística tradicionais. Os dados agrupados podem ser usados para análise exploratória, para visualização de dados, para redução de dimensionalidade, entre outros. 
 - _**Detecção de outliers:**_ Processo de identificação de pontos de dados que são significativamente diferentes dos outros pontos no conjunto de dados. Outliers podem ser causados por erros de medição, erros de entrada de dados, ou podem representar fenômenos interessantes que merecem análise profunda. É uma etapa importante para o processamento , pois pode afetar significativamente os resultados da machine learning.<br> [Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/deteccao_de_outliers.py)
 - _**Séries temporais:**_ As séries temporais são conjuntos de dados que são coletados ao longo do tempo. Elas são usadas em uma ampla gama de aplicações, incluindo previsão de vendas, análise de tendências, monitoramento de sistemas, entre outros. As séries temporais podem ser observadas (onde os valores são registrados em intervalos regulares) ou não observadas (onde os valores são estimados ou previstos). Componentes das séries temporais, tempo ( o eixo de tempo é crucial para séries temporais pois os dados são coletados ao longo do tempo
), valores (Os valores observados ou estimados na série), frequência de corte (a frequência onde os valores  são coletados (mensamente, semanalmente…). Alguns modelos:
    - *Modelos ARIMA (Autoregressive Integrated Moving Average):* Um modelo estatístico que combina componentes autoregressivos (utiliza os valores anteriores na série temporal para prever o próximo valor), diferenciais (diferencia a série temporal para remover a tendência e a sazonalidade, tornando os dados mais estáveis) e médias móveis (utiliza os erros dos modelos autoregressivos para prever o próximo valor) para prever séries temporais . O modelo ARIMA é uma das abordagens mais populares para modelar séries temporais.
    - *Modelos de Séries Temporais com Redes Neurais:*  Redes neurais podem ser treinadas para prever séries temporais, capturando padrões complexos e não lineares nos dados. As Redes Neurais são uma abordagem poderosa para modelar séries temporais, especialmente quando há padrões complexos e não lineares nos dados. As Redes Neurais podem capturar dependências temporais complexas e não lineares, tornando-as adequadas para uma ampla gama de problemas de séries temporais.
    - *Modelos de Séries Temporais com Máquinas de Vetores de Suporte (SVM):* SVMs podem ser usados para prever séries temporais, especialmente quando há uma estrutura temporal complexa nos dados. As Máquinas de Vetores de Suporte (SVM) são outra abordagem poderosa para modelar séries temporais. Elas são particularmente úteis quando há uma estrutura temporal complexa nos dados, como quando há múltiplas tendências ou sazonalidades. As SVMs podem ser treinadas para prever o próximo valor na série temporal com base em uma combinação de valores anteriores e suas posições temporais.
    - *Modelos de Séries Temporais com Árvores de Decisão e Florestas Aleatórias:* Árvores de decisão e florestas aleatórias também podem ser usadas para modelar séries temporais, especialmente quando os dados são não lineares ou quando há uma estrutura temporal complexa. Esses modelos podem capturar interações complexas entre os valores anteriores e suas posições temporais para prever o próximo valor.
    - *Modelos de Séries Temporais com Métodos de Ensemble:* Métodos de ensemble, como o modelo de previsão de séries temporais baseado em regressão (Prophet) da Facebook, combinam várias técnicas de modelagem para fornecer previsões robustas e precisas. O Prophet, por exemplo, utiliza modelos de tendência, sazonalidade e eventos para prever séries temporais, tornando-o adequado para uma ampla gama de problemas.<br> [Implementação Simples](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/series_temporais.py)
  
#

## Chapter 8: Supplementary Topics

### Preprocessing:
A crucial step is the machine learning pipeline* that involves cleaning and transforming the raw data so that it is in a format suitable for use. It is always interesting to study which techniques to use.
> Pipeline: A pipeline in machine learning is a sequence of data processing steps that transform raw data into useful insights. The pipeline automates the machine learning workflow, making it easier to perform complex tasks and improving process efficiency and reproducibility. Pre-processing -> Attribute selection -> Modeling -> Evaluation -> Deployment.
### Some techniques:
 - _**Missing values:**_ We can deal with them in different ways, such as replacing missing values ​​with a specific one such as the mean, median or mode of the existing values ​​in the column (imputation), removing rows or columns that contain values ​​that contain rows missing values ​​(deletion), estimation of values ​​based on existing values, such as linear interpolation* for sequential data (interpolation), use of a machine learning model to predict missing values ​​based on other characteristics (prediction model). <br>[Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/dados_faltantes.py)
 - _**Normalization:**_ It is a technique used to transform the values ​​of numerical variables into a common scale, without distorting differences in value ranges or data distribution. If the features (data) are at different scales, the algorithm may give more weight to features with higher values, which may lead to relatively inferior results.<br> [Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/normalizacao.py)
 - _**Discretization:**_ It is the process of transforming continuous variables into categorical variables. It is done by dividing the range of possible values ​​of the variable into a fixed number of intervals (bins). Examples: MIN-MAX and Z-Score. <br>[Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/discretizacao.py)
  > MIN-MAX normalization: Resizes the values ​​to a specific range, usually between 0 and 1. (Search for the formula for normalization).<br>
  > Z-Score Normalization: Resizes values ​​to have a mean of 0 and a standard deviation of 1.
- _**Attribute selection:**_ Involves choosing a subset of attributes from a dataset to use in a machine learning model. It can be done for several reasons, including dimensionality reduction, improvement in computational efficiency and the risk of overfitting. It can be done either manually or using statistical techniques. Some examples:
    - *Selection of univariate attributes:* Evaluates the importance of each attribute individually, without considering interactions between attributes. A common approach is to use correlation measures, such as the Pearson correlation coefficient, to measure the strength of the relationship between each attribute and the target variable.
    - *Recursive Attribute Selection:* This technique uses machine learning algorithms to build a machine learning model (such as a decision tree or a random forest) and then selects the attributes that contribute most to the construction of the model.
    - *Multivariate attribute selection:* This technique considers interactions between attributes. A common approach is to use attribute importance methods that take into account interactions between attributes, such as the random forest attribute importance method.
    - *Model-Based Attribute Selection:* This technique uses machine learning models to select the attributes that are most important for predicting the target variable. For example, the random forest attribute importance method can be used to select the most important attributes
   <br> [Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/selecao_atributos.py)
- _**Dimensionality reduction:**_ Aims to reduce the number of variables in a data set, keeping as much information as possible, it is important as it improves computational efficiency, as by excluding less relevant data, algorithms need to process less data. It facilitates data visualization in smaller spaces in 2D and 3D, which can be useful for exploratory analysis and data interpretation. Reduces the risk of overfitting, as with fewer variables, algorithms are less likely to capture noise in the data, in addition to improving interpretability. There are several dimensionality reduction techniques, including:
    - *PCA (Principal Component Analysis):* Transforms the data set into a new set of uncorrelated (orthogonal) variables that capture the greatest variance in the original data.
    - *T-SNE (T- Distributed Stochastic Neighbor Embedding):* Particularly useful for visualizing high-dimensional data. Preserves local distances between data points, which can be useful for identifying clusters and data structures.<br> [Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/reducao_de_dimensionalidade.py)
 - _**Clustering:**_ Clustering is an unsupervised machine learning technique that groups similar data into groups or clusters. The purpose of clustering is to identify structures or patterns in data that are not easily accessible through traditional statistical analysis methods. Grouped data can be used for exploratory analysis, data visualization, dimensionality reduction, among others.
 - - _**Outlier detection:**_ Process of identifying data points that are significantly different from other points in the data set. Outliers can be caused by measurement errors, data entry errors, or they can represent interesting phenomena that deserve in-depth analysis. It is an important step for processing, as it can significantly affect machine learning results.<br> [Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/deteccao_de_outliers.py)
 - _**Time series:**_ Time series are sets of data that are collected over time. They are used in a wide range of applications, including sales forecasting, trend analysis, system monitoring, among others. Time series can be observed (where values ​​are recorded at regular intervals) or unobserved (where values ​​are estimated or predicted). Components of time series, time (the time axis is crucial for time series as data is collected over time
), values ​​(The observed or estimated values ​​in the series), cutoff frequency (the frequency where the values ​​are collected (monthly, weekly…). Some models:
   - *ARIMA (Autoregressive Integrated Moving Average) models:* A statistical model that combines autoregressive (uses the previous values ​​in the time series to predict the next value), differential (differentiates the time series to remove trend and seasonality, making the more stable data) and moving averages (uses the errors of autoregressive models to predict the next value) to predict time series. The ARIMA model is one of the most popular approaches to modeling time series.
    - *Time Series Models with Neural Networks:* Neural networks can be trained to predict time series, capturing complex and non-linear patterns in data. Neural Networks are a powerful approach to modeling time series, especially when there are complex, non-linear patterns in the data. Neural Networks can capture complex, non-linear temporal dependencies, making them suitable for a wide range of time series problems.
    - *Time Series Models with Support Vector Machines (SVM):* SVMs can be used to predict time series, especially when there is a complex temporal structure in the data. Support Vector Machines (SVM) are another powerful approach to modeling time series. They are particularly useful when there is a complex temporal structure in the data, such as when there are multiple trends or seasonalities. SVMs can be trained to predict the next value in the time series based on a combination of previous values ​​and their temporal positions.
    - - *Time Series Models with Decision Trees and Random Forests:* Decision trees and random forests can also be used to model time series, especially when the data is non-linear or when there is a complex temporal structure. These models can capture complex interactions between previous values ​​and their temporal positions to predict the next value.
    - *Time Series Models with Ensemble Methods:* Ensemble methods, such as Facebook's regression-based time series forecasting model (Prophet), combine several modeling techniques to provide robust and accurate forecasts. Prophet, for example, uses trend, seasonality, and event models to forecast time series, making it suitable for a wide range of problems.<br> [Simple Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/topicos_complementares/series_temporais.py)