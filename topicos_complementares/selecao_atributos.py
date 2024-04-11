from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

#carrega o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#treina uma floresta aleatória
clf = RandomForestClassifier(random_state=0)
clf.fit(X, y)

#obtém a importância dos atributos
importances = clf.feature_importances_

#plota a importância dos atributos
plt.bar(iris.feature_names, importances)
plt.xlabel('Atributos')
plt.ylabel('Importância')
plt.title('Importância dos Atributos')
plt.show()
