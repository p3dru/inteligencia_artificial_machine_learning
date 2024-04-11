from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as plt

#gera um conjunto de dados de exemplo com outliers
np.random.seed(0)
X = 0.3 * np.random.randn(100, 1)
X_outliers = np.random.uniform(low=-4, high=4, size=(10, 1))
X = np.concatenate((X, X_outliers), axis=0)

#treina o modelo Isolation Forest para detecção de outliers
clf = IsolationForest(contamination=0.1)
clf.fit(X)
y_pred = clf.predict(X)

#plota os dados e os outliers
plt.scatter(X[:, 0], np.zeros(X.shape[0]), c=y_pred, cmap='viridis')
plt.xlabel('Valor')
plt.ylabel('')
plt.title('Detecção de Outliers com Isolation Forest')
plt.show()
