import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

#dados de exemplo
X = np.array([[1200, 3], [1400, 4], [1600, 5], [1800, 6], [2000, 7]])
y = np.array([200000, 250000, 300000, 350000, 400000]) # Renda em dólares

#divide os dados em conjuntos de treinamento e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#cria e treina o modelo de regressão de Ridge com um parâmetro de regularização de 1.0
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

#faz previsões no conjunto de teste
y_pred = model.predict(X_test)

#imprimi os coeficientes do modelo
print("Coeficientes:", model.coef_)
print("Interceptação:", model.intercept_)

#imprimi as previsões
print("Previsões:", y_pred)
