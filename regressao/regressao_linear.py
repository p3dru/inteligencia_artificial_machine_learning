import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#arrays numpy
x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5])

#cria o modelo de regressão linear
model = LinearRegression()
#treina o modelo
model.fit(x, y)

#realiza a previsão de valores passando um valor
y_pred = model.predict(x)


#para visualizar os resultados para ver como o modelo se ajusta aos dados
#plota os dados originais
plt.scatter(x, y, color='blue', label='Dados originais')

#cria um plot para a linha de regressão
plt.plot(x, y_pred, color='red', label='Linha de regressão')

#adicionar legenda e título
plt.legend()
plt.title('Regressão Linear')

#mostra em gráfico
plt.show()

'''
Explicando:
Cada ponto azul é a coordenada montada pela junção das coordenadas x e y
A linha é a "linha de previsão", onde define um local "ideal" para futuras
predições de pontos 
'''