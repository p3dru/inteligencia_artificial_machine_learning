from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#gera um conjunto de dados de exemplo
'''
'make_blobs' gera um conjunto de dados gerados artificialmente
'n_samples' é o número de amostras
centers é a quantidade de centróides/onde os clusters irão se agrupar
cluster_std é o desvio padrão dos clusters
'''
X, y = make_blobs(n_samples=150, centers=3, cluster_std=0.5, random_state=0)

#cria e ajusta o modelo KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

#plota os clusters
'''
X[:, 0] e X[:, 1] são usados para selecionar as colunas 0 e 1 do array
X, que representam as coordenadas x e y dos pontos de dados. Esses pontos
são plotados no gráfico de dispersão.
c=kmeans.labels_ define a cor de cada ponto de dados com base nos rótulos
de cluster atribuídos pelo algoritmo KMeans. Cada cluster terá uma cor
diferente.
cmap='viridis' especifica o mapa de cores a ser usado para as cores dos
pontos de dados. O mapa de cores 'viridis' é um gradiente de verde para azul.
'''
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
'''
kmeans.cluster_centers_[:, 0] e kmeans.cluster_centers_[:, 1] são usados para
selecionar as coordenadas x e y dos centróides dos clusters. Esses centróides
são plotados no gráfico de dispersão.
s=300 define o tamanho dos pontos de centróide. Um valor maior fará os pontos
de centróide aparecerem maiores no gráfico.
c='red' define a cor dos pontos de centróide como vermelho.
'''

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()