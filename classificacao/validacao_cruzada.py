from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

#carrega o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#cria o classificador SVM
classifier = SVC(kernel='linear', C=1.0)

#aplica validação cruzada com 5 folds
scores = cross_val_score(classifier, X, y, cv=5)

#imprime a acurácia média
print(f"Acurácia média: {scores.mean()}")
