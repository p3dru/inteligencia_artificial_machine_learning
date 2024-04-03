import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

'''
dados de exemplo conjunto de valores aleatorios que representam
dados se uma pessoa é diabética ou não (arbitrário)
'''
X = np.array([[25, 70], [30, 80], [35, 75], [40, 85], [45, 90]])
#0 para não diabético, 1 para diabético
y = np.array([0, 0, 1, 1, 1])

'''
divide os dados em conjuntos de treinamento e teste, proporção 80/20
sendo 20 os testes, random_state é para salvar o estado da regressão 
para critérios de avaliação futuros
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#criar e treina o modelo de regressão logística
model = LogisticRegression()
model.fit(X_train, y_train)

#faz previsões no conjunto de teste
y_pred = model.predict(X_test)

#imprimi os coeficientes do modelo
print("Coeficientes:", model.coef_)
print("Interceptação:", model.intercept_)

#imprimir as previsões (é ou não diabético)
print("Previsões:", y_pred)
