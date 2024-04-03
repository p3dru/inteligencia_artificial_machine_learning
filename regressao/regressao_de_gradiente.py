from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import SGDRegressor

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
X, y = make_regression(n_samples=100, n_features=4, noise=0.1, random_state=42)

#divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#cria o modelo de Regressão de Gradiente
model = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)

#treina o modelo
model.fit(X_train, y_train)

#faz previsões
y_pred = model.predict(X_test)

#calcula o erro quadrático médio
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio: {mse}")
