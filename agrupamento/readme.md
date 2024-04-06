## Capítulo 6: Agrupamento

### Conceito:
O agrupamento é uma técnica de aprendizado de máquina não supervisionada que agrupa dados semelhantes em clusters ou grupos. O objetivo é identificar estruturas ou padrões nos dados que não são facilmente acessíveis por meio de métodos de análises nos padrões que não são facilmente acessíveis por meio de métodos de análises estatísticas tradicionais. Os dados agrupados podem ser usados para análise exploratória, para visualização de dados, para redução de dimensionalidade, entre outros

### Técnicas mais utilizadas:
#### K-means:
Divide os dados em “k” clusters, onde cada ponto de dados pertence ao cluster com a média mais próxima. O algoritmo itera até que os clusters não mudem mais ou até que um número máximo de iterações seja atingido. 
Como funciona:
 - Escolhe k pontos de dados aleatórios como centróides iniciais.
 - Atribui cada ponto de dados ao cluster cujo centróide está mais próximo.
 - Recalcula os centróides como a média dos pontos de dados em cada cluster.
 - Repete os pessoas 2 e 3 até que os centroides não mudem mais ou até que um número máximo de iterações seja atingido (evita loop eterno)

**Quando usar:** Quando conhecemos o números de clusters de antemão e os clusters são separados para serem convexos e de tamanho similar. Particularmente útil em problemas de agrupamento de imagens, onde os clusters representam diferentes objetos ou características.
<br>**Quando evitar:** Não é adequado para clusters de formas irregulares ou de tamanhos diferentes, pois assume que todos os clusters têm a mesma densidade e forma. Além disso, o K-Means pode ser sensível à inicialização dos centróides.

[Implementação k-means](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/k_means.py)

#### Hierárquico:
Constrói uma hierarquia de clusters começando com cada ponto de dados sendo um cluster.
Como funciona:
 - Cada ponto é considerado um cluster individual.
 - Combina os dois clusters mais próximos para formar um novo cluster.
 - Repete o processo até que todos estejam em um único cluster.

**Quando usar:** Em problemas onde os clusters podem ter formas irregulares e quando se deseja identificar clusters de densidade variável. Ele é particularmente útil em problemas de agrupamento de dados espaciais, onde a proximidade física dos pontos de dados é importante.
<br>**Quando evitar:** Pode ser sensível aos parâmetros de densidade e distância, o que pode afetar a qualidade dos clusters formados. Além disso, pode ser menos eficaz em problemas onde os clusters são de tamanho muito diferente.

[Implementação técnica hierárquica](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/agglomerative_hierarquical.py)

#### DBSCAN (Density-Based Spatial Clustering of Applications with Noise):
Técnica baseada em densidade que agrupa pontos de dados que estão próximos uns aos outros e separa pontos que estão isolados.
Como funciona:
 - Define uma região de densidade alta como um cluster.
 - Um ponto de dados é considerado parte de um cluster se estiver dentro da região de densidade de outro ponto de dados.
 - Pontos de dados que não estão próximos o suficiente de outros pontos de dados são considerados ruído e não são atribuídos a nenhum cluster.

**Quando usar:** É uma boa escolha para problemas onde os clusters podem ter formas irregulares e quando se deseja identificar clusters de densidade variável. Ele é particularmente útil em problemas de agrupamento de dados espaciais, onde a proximidade física dos pontos de dados é importante.
<br>**Quando evitar:** Pode ser sensível aos parâmetros de densidade e distância, o que pode afetar a qualidade dos clusters formados. Além disso, pode ser menos eficaz em problemas onde os clusters são de tamanho muito diferente.

[Implementação DBSCAN](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/dbscan.py)

#### Agglomerative Hierarchical Clustering:
É uma variação do agrupamento hierárquico.
Como funciona:
 - Inicialmente, cada ponto de dados é considerado um cluster individual.
 - Combina os dois clusters mais próximos para formar um novo cluster.
 - Repete o processo até que todos os dados estejam em um único cluster.

**Quando usar:** Semelhante ao agrupamento hierárquico, o agglomerative hierarchical clustering é útil quando se deseja uma representação visual dos dados e quando os clusters podem ter diferentes formas e tamanhos. Ele pode ser uma boa escolha quando se deseja uma abordagem mais exploratória para entender a estrutura dos dados.
<br>**Quando evitar:** Assim como o agrupamento hierárquico, pode ser computacionalmente intensivo para grandes conjuntos de dados e a escolha do número de clusters pode ser difícil.

[Implementação Agglomerative](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/agglomerative_hierarquical.py)

#
## Chapter 6: Clustering

### Concept:
Clustering is an unsupervised machine learning technique that groups similar data into clusters or groups. The goal is to identify structures or patterns in the data that are not easily accessible through traditional statistical analysis methods. Grouped data can be used for exploratory analysis, data visualization, dimensionality reduction, among others

### Most used techniques:
#### K-means:
Divides the data into “k” clusters, where each data point belongs to the cluster with the closest mean. The algorithm iterates until the clusters no longer change or until a maximum number of iterations is reached.
How it works:
 - Choose k random data points as initial centroids.
 - Assigns each data point to the cluster whose centroid is closest.
 - Recalculates the centroids as the average of the data points in each cluster.
 - Repeats people 2 and 3 until the centroids no longer change or until a maximum number of iterations is reached (avoids eternal loop)

**When to use:** When we know the number of clusters in advance and the clusters are separated to be convex and of similar size. Particularly useful in image clustering problems, where the clusters represent different objects or features.
<br>**When to avoid:** Not suitable for clusters of irregular shapes or different sizes, as it assumes that all clusters have the same density and shape. Furthermore, K-Means can be sensitive to the initialization of centroids.

[k-means implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/k_means.py)

#### Hierarchical:
Constructs a hierarchy of clusters starting with each data point being a cluster.
How it works:
 - Each point is considered an individual cluster.
 - Combines the two closest clusters to form a new cluster.
 - Repeat the process until everyone is in a single cluster.

**When to use:** In problems where clusters may have irregular shapes and when you want to identify clusters of variable density. It is particularly useful in spatial data clustering problems, where the physical proximity of data points is important.
<br>**When to avoid:** It can be sensitive to density and distance parameters, which can affect the quality of the clusters formed. Furthermore, it may be less effective on problems where the clusters are of very different size.

[Hierarchical technical implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/agglomerative_hierarquical.py)

#### DBSCAN (Density-Based Spatial Clustering of Applications with Noise):
Density-based technique that groups data points that are close to each other and separates points that are isolated.
How it works:
 - Defines a high density region as a cluster.
 - A data point is considered part of a cluster if it is within the density region of another data point.
 - Data points that are not close enough to other data points are considered noise and are not assigned to any cluster.

**When to use:** It is a good choice for problems where clusters may have irregular shapes and when you want to identify clusters of varying density. It is particularly useful in spatial data clustering problems, where the physical proximity of data points is important.
<br>**When to avoid:** It can be sensitive to density and distance parameters, which can affect the quality of the clusters formed. Furthermore, it may be less effective on problems where the clusters are of very different size.

[DBSCAN implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/dbscan.py)

#### Agglomerative Hierarchical Clustering:
It is a variation of hierarchical clustering.
How it works:
 - Initially, each data point is considered an individual cluster.
 - Combines the two closest clusters to form a new cluster.
 - Repeat the process until all data is in a single cluster.

**When to use:** Similar to hierarchical clustering, agglomerative hierarchical clustering is useful when a visual representation of data is desired and when clusters can have different shapes and sizes. It can be a good choice when you want a more exploratory approach to understanding the structure of the data.
<br>**When to avoid:** Like hierarchical clustering, it can be computationally intensive for large data sets and choosing the number of clusters can be difficult.

[Agglomerative Implementation](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/agrupamento/agglomerative_hierarquical.py)
