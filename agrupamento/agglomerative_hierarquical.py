from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

#gera um conjunto de dados de exemplo
#'make_blobs' gera um conjunto de dados gerados artificialmente
X, y = make_blobs(n_samples=150, centers=3, cluster_std=0.5, random_state=0)

#cria e ajusta o modelo AgglomerativeClustering
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_clustering.fit(X)

#plota os clusters
plt.scatter(X[:, 0], X[:, 1], c=agg_clustering.labels_, cmap='viridis')
plt.show()