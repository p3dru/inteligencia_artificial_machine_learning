import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

#gera dados de exemplo
'''
n_samples = número de amostras (linhas) no conjunto de dados gerado
número de recursos (colunas) no conjunto de dados gerado. Isso representa
quantas variáveis independentes existem no conjunto de dados
Especifica a quantidade de ruído (variação aleatória) adicionada ao conjunto de dados gerado.
O ruído é uma forma de adicionar variabilidade ao conjunto de dados, o que pode ser útil para
testar a robustez de um modelo de aprendizado de máquina. Um valor de noise=0.1 significa que
10% do sinal no conjunto de dados é adicionado aleatoriamente.
'''
X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)

#divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#cria e treina o modelo de Regressão de Decisão
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

#faz previsões no conjunto de teste
y_pred = model.predict(X_test)

#imprime as previsões
print("Previsões:", y_pred)
