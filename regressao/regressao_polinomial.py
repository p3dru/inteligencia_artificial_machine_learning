import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#dados de exemplo
x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5])

#transforma x em polinômios
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

#treina o modelo de regressão linear
model = LinearRegression()
model.fit(x_poly, y)

#faz previsões
y_pred = model.predict(x_poly)

#plota os dados originais e a curva polinomial
plt.scatter(x, y, color='blue', label='Dados originais')
plt.plot(x, y_pred, color='red', label='Curva polinomial')
plt.legend()
plt.title('Regressão Polinomial')
plt.show()
