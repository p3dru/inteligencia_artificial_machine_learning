from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#carrega o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#treina o classificador KNN
#n_neighbors = 3, significa que está definindo 3 classes classificadoras
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

#faz previsões no conjunto de teste
y_pred = classifier.predict(X_test)

#calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")
