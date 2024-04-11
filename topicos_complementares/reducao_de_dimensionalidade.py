from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

#carrega o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#reduz a dimensionalidade usando PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

#reduz a dimensionalidade usando t-SNE
tsne = TSNE(n_components=2, random_state=0)
X_tsne = tsne.fit_transform(X)

#plota os resultados
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.title('PCA')

plt.subplot(122)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.title('t-SNE')

plt.show()
