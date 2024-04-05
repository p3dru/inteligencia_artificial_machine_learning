from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

#gera um conjunto de dados de exemplo
#'make_blobs' gera um conjunto de dados gerados artificialmente
X, y = make_blobs(n_samples=150, centers=3, cluster_std=0.5, random_state=0)

#cria e ajusta o modelo DBSCAN
'''
'eps=0.3' Este parâmetro define a distância máxima entre dois pontos de dados
para que eles sejam considerados vizinhos. Em outras palavras, se a distância
entre dois pontos for menor ou igual a eps, eles são considerados parte do
mesmo cluster. O valor de eps é crucial para determinar a densidade de um cluster. 
Um valor menor de eps resultará em clusters mais densos, enquanto um valor maior 
pode resultar em clusters mais dispersos.
'min_samples=5' Este parâmetro especifica o número mínimo de pontos de dados que
um cluster deve conter para ser considerado um cluster válido. Se um ponto de 
dados não tiver pelo menos min_samples pontos vizinhos dentro da distância eps, 
ele será considerado ruído e não será atribuído a nenhum cluster.
'''
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X)

# Plotando os clusters
plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_, cmap='viridis')
plt.show()